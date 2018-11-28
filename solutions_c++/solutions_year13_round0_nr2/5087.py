
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <stack>
#include <cctype>
#include <complex>
#include <vector>
#include <algorithm>

using namespace std;


bool solve(){
	
	int n,m;
	cin>> n>> m;
	int a[110][110]={0};
	int max=1;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>> a[i][j];
			if(max < a[i][j]) max = a[i][j];
		}
	}
	
	for(int k=1;k<max;k++){
		
		int res[2][110]={0};	//0‰¡A1c
		//‰¡
		for(int i=0;i<n;i++){
			if(a[i][0]==k){
				int cnt=0;
				for(int j=0;j<m;j++){
					if(a[i][j]!=k) cnt++;
				}
				if(!cnt) res[0][i]++;
			}
		}
		//c
		for(int j=0;j<m;j++){
			if(a[0][j]==k){
				int cnt=0;
				for(int i=0;i<n;i++){
					if(a[i][j]!=k) cnt++;
				}
				if(!cnt) res[1][j]++;
			}
		}
				
		//‚‚³‚ð1‚‚­‚·‚éA‚ ‚è“¾‚È‚¢‰ÓŠŒŸo
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(a[i][j]==k){
					if(res[0][i] || res[1][j]){
						a[i][j]++;
					}else{
						return false;
					}
				}
			}
		}
		
	}
	
	return true;
}

int main(){
	cout.setf(ios::fixed);
	cout.precision(10);

	int n;
	cin>> n;
	for(int k=0;k<n;k++){
		int ans = solve();
		if(ans){
			cout<<"Case #"<< k+1<< ": YES"<<endl;
		}else{
			cout<<"Case #"<< k+1<< ": NO"<<endl;
		}

	}

	return 0;
}

 