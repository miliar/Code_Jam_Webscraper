/*
Problem A. Standing Ovation
link:https://code.google.com/codejam/contest/6224486/dashboard
*/
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define FOR(i,n) for(i=0;i<n;i++)
#define FORJAS(i,j,n) for(i=j;i<n;i++)
#define FORJS(i,j,n) for(i=j;i<=n;i++)
#define MOD 1000000007
#define LEN 1005

int main(){

	int t,n,k,i,j,ans,si;
	cin>>t;

	FOR(j,t){
		cin>>n;
		string ki;
		cin>>ki;
		ans=si=0;
		for(i=0;i<ki.length();i++){
			
			if(si < i){
				ans+=(i-si);
				si=i;
			}
			//cout<<ans<<":"<<si<<endl;
			si+= (ki[i]-'0');
		}
		cout<<"Case #"<<j+1<<": "<<ans<<endl;
	}
	return 0;
}