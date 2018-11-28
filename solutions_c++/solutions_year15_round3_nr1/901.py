#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>
#define forn(i, n) for(int i=0; i<n; i++)
#define for1(i, n) for(int i=1; i<=n; i++)
#define N 1000243
using namespace std;
int main(){
	int n, a, b, c;
	cin>>n;
	forn(i, n){
		cin>>a>>b>>c;
		cout<<"Case #"<<i+1<<": "<<((b+c-1)/c) + (b/c)*(a-1) + c-1<<endl;
	}
	
	return 0;
}
