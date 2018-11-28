
// aymos (Somya Mehdiratta , IIIT Hyderabad)

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<map>
#include<climits>
#include<stack>
#include<queue>
#include<algorithm>

using namespace std;

#define PB push_back
#define FOR(i,s,n) for(int i=(s),_n=(n);i<_n;i++)

typedef long long LL;

int main(int argc, char *argv[]){
	int t,n;
	cin>>t;
	n=t;
	while(t--){
		cout<<"Case #"<<n-t<<": "; 		
		long double time = 0 ,c,f,x , r=2;
		cin>>c>>f>>x;
		while(1){
			if ( x/r > ( c/r + x/(r+f) ) ){
				time += c/r ;
				r += f;
			}
			else {
				time += x/r;
				break;
			}
		}
		printf("%LF\n",time);
		}
	
	return 0;
}
