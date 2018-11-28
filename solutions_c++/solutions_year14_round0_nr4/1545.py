#include <fstream> // You should include this library
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector <double> naomi;
vector <double> ken;
vector <double> naomi2;
vector <double> ken2;
int n;

int items_less_than(double num) {
	int res = 0;
	for (int i = 0; i < n; i++) {
		if (ken[i] < num) {
			res++;
		}
		else
			return res;
	}
	return res;
}

int calculate_war() {
	int j = 0;
	for (int i = 0; i < n; i++) {
		while (naomi[i] > ken[j]) {
			j++;
			if (j >= n) {
				return n-i;
			}
		}
		j++;
	}
	return 0;
}

int calculate_war2() {
	int res = 0;
	for (int i = 0; i < n; i++) {
		bool found = false;
		for (int j = 0; j < naomi2.size(); j++) {
			if (naomi2[j] > ken2[i]) {
				if (found) {
					naomi2.erase(naomi2.begin()+j-1);
				} else {
					res++;
				}
				break;
			} else {
				found = true;
			}
		}
	}
	return res;
}

int calculate_deceived_war() {
	int j = 0;
	for (int i = 0; i < n; i++) {
		while (ken[i] > naomi[j]) {
			j++;
			if (j >= n) {
				return n-i;
			}
		}
		j++;
	}
	return 0;
}

int calculate_deceived_war2() {
	int res = 0;
	for (int i = 0; i < n; i++) {
		bool found = false;
		bool added = false;
		for (int j = 0; j < ken2.size(); j++) {
			if (naomi[i] < ken2[j]) {
				if (found) {
					ken2.erase(ken2.begin()+j-1);
					res++;
					added = true;
				}
				break;
			}
			else {
				found = true;
			}
		}
		if (found && !added)
			res++;
	}
	return res;
}

int main()
{
     freopen("D-large.in","r",stdin); // For reading input
     freopen("D-large.out","w",stdout); // for writing output
     int t,x,y;
     cin >> t;
     for (int i = 0; i < t; i++) {
    	 cin >> n;
    	 naomi.resize(n);
    	 ken.resize(n);
    	 for (int j = 0; j < n; j++) {
    		 cin >> naomi[j];
    	 }
    	 for (int j = 0; j < n; j++) {
			 cin >> ken[j];
		 }
    	 sort(naomi.begin(),naomi.end());
    	 sort(ken.begin(),ken.end());
    	 naomi2 = naomi;
    	 ken2 = ken;
/*
    	 for (int j = 0; j < n; j++) {
    		 cout << naomi[j] << " ";
    	 }
    	 cout << endl;
    	 for (int j = 0; j < n; j++) {
			 cout << ken[j] << " ";
		 }
*/
    	 x = calculate_war2();
    	 y = calculate_deceived_war2();
    	 cout << "Case #" << i+1 << ": ";
    	 cout << y << " " << x;
    	 cout << endl;
     }
     return 0;
}
