#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;


int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B2.out", "w", stdout);
	int t;
	cin >> t;
	int n, m;
	int a[101][101];
	 for(int i = 0; i < t; i++){
		 cin >> n >> m;
		 int mx1[101] = {0}, mx2[101] = {0};
		 for(int i = 0; i < n; i++){
			 for(int j = 0; j < m; j++){
				 cin >> a[i][j];
				 mx1[i] = max(mx1[i], a[i][j]);
				 mx2[j] = max(mx2[j], a[i][j]);
			 }
		 }
		 int res = 0;
		 for(int i = 0; i < n; i++){
			 for(int j = 0; j < m; j++){
				 int k = min(mx1[i], mx2[j]);
				 if(a[i][j] != k)
					 res = 1;
			 }
		 }
		 cout << "Case #" << i + 1 << ": ";
		 if(res)
			 cout << "NO" << endl;
		 else
			 cout << "YES" << endl;
	 }

	 return 0;
}