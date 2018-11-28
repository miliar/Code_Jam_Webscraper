#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<map>

#define rep(i, s, n) for(i = (s); i < (n); i++)
#define LIM 1000000000

using namespace std;

ostringstream op;

int main(int argc, char** argv){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(0);
	int t;
	cin >> t;
	double ken[1001];
	double naomi[1001];
	double ken2[1001];
	double naomi2[1001];
	for(int kk = 1; kk <= t; kk++){
		int n;
		cin >> n;
		for(int i = 0; i < n; i++){
			cin >> naomi[i];
			
		}
		for(int i = 0; i < n; i++){
			cin >> ken[i];
		}
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		for(int i = 0; i < n; i++){
			naomi2[i] = naomi[i];
			ken2[i] = ken[i];
		}
		
		int np = 0, kp = 0;
		for(int i = n-1; i >= 0; i--){
			int sm=-1, mx=-1;
			for(int j = n-1; j >= 0; j--){
				if(ken[j] == 0)
					continue;
				if(ken[j] > naomi[i])
					mx = j;
				else sm = j;
			}
			if(mx >= 0 && naomi[i] < ken[mx]){
				kp++;
				ken[mx] = 0;
			}
			else {
				np++;
				ken[sm] = 0;
			}
		}

		
		int np2 = 0, kp2 = 0;
		for(int i = n-1; i >= 0; i--){
			int sm=-1, mx=-1;
			for(int j = n-1; j >= 0; j--){
				if(naomi2[j] == 0)
					continue;
				if(naomi2[j] > ken2[i])
					mx = j;
				else sm = j;
			}
			if(mx >= 0 && ken2[i] < naomi2[mx]){

				np2++;
				naomi2[mx] = 0;
			}
			else {
				kp2++;
				naomi2[sm] = 0;
			}
		}
		cout << "Case #" << kk << ": " << np2 << " " << np << endl;
	}

	return 0;
}

