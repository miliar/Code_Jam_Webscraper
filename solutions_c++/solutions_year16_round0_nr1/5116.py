#include <iostream>
#include <fstream>
#include <cstdio>
#include <math.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <climits>
#include <stack>
#include <queue>
#include <set>
#include <map>
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a>b?b:a
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR_X(i,x,n) for(i=x;i<n;i++)
#define BACK(i,n) for(i=n;i>=0;i--)
#define BACK_X(i,n,x) for(i=n;i>=x;i--)
#define fill(a,v) memset(a,v,sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) a*b/gcd(a,b)
#define pb push_back
#define pp pair<int,int>
typedef long long int lld;
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0); //dont use with EOF
	int t,x=0;
	cin>>t;
	while(t--){
		x++;
		lld n;
		cin>>n;
		if( n==0 ){
			cout<<"Case #"<<x<<": INSOMNIA\n";
			continue;
		}
		lld bitMask=0,curr=n;
		while( curr>0){
			int pos= curr%10;
			bitMask|= (1<<pos);
			curr/=10;
		}
		curr=n;
		while( bitMask!= (1<<10)-1 ){
			curr+=n;
			lld tmp= curr;
			while( tmp>0 ){
				int pos= tmp%10;
				bitMask |= (1<<pos);
				tmp/=10;
			} 
		}
		cout<<"Case #"<<x<<": "<<curr<<endl;
	}
	return 0;
}