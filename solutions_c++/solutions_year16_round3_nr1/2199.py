#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>

using namespace std;
struct env{
	int count;
	int index;
};
bool compar(env a, env b){
	return a.count < b.count;
}
int main(){
	int test;
	cin >> test;
	char temp[26] = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
	for (int k = 1; k <= test; k++){
		int n;
		cin >> n;
		env a[n];
		for (int i = 0;i < n;i++){
			cin >> a[i].count;
			a[i].index = i;
		}
		if(n == 2){
			cout << "Case #"<<k<<": ";
			for (int i = 0;i < a[0].count;i++){
				cout<< "AB" <<" ";
			}
			cout << "\n";
		}
		else if(n != 2){
			cout << "Case #"<<k<<": ";
			while(true){
				sort(a, a + n, compar);
				if(a[n - 1].count != a[0].count){
					cout << temp[a[n - 1].index] <<" ";
					a[n - 1].count -= 1;
				}
				else 
					break;
			}
			int i = 0;
			while(i < n - 2){
				for(int j = 0;j < a[i].count;j++){
					cout<< temp[a[i].index] <<" ";
				}
				i++;
			}
			for(int j = 0;j < a[n - 1].count;j++){
					cout<< temp[a[n - 1].index] <<temp[a[n - 2].index]<<" ";
				}
			cout <<"\n";
		}
	}
}