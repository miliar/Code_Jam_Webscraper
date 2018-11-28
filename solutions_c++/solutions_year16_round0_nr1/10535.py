
#include <iostream>
#include <cstdio> 
#include <vector> 
#include <cassert> 
#include <sstream> 
#include <map> 
#include <set> 
#include <climits> 
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace std;

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define INF 1000000000
#define ALL(x) x.begin(),x.end()
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,v.begin(),v.end())

typedef pair<int,int> PI;
typedef vector<int> VI;
typedef long long LL;

int main(){
	int t;
	cin>>t;
	for(int cs = 1;cs<=t;cs++){
		int n;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<cs<<": "<<"INSOMNIA"<<endl;
		} else {
			int h[10]={0};
			for(int i=1;;i++){
				int m = n*i;
				while(m){
					h[m%10]=1;
					m/=10;
				}
				int j=0;
				for(j=0;j<10;j++){
					if(h[j]==0){
						break;
					}
				}
				if(j==10){
					cout<<"Case #"<<cs<<": "<<n*i<<endl;
					break;
				}
			}
		}
	}
	return 0;
}
