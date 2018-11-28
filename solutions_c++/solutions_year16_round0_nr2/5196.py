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
string a;
int main()
{
	ios_base::sync_with_stdio(0); //dont use with EOF
	int t,x=0;
	cin>>t;
	while(t--){
		x++;
		cin>>a;
		int n= a.length();
	//	cout<<a<<" "<<n<<endl;
		int ans=0;
		for(int i=n-1;i>=0;i--){
			if( a[i]=='+' ) continue;
			if( a[0]== '+' ){
				ans++;
				int j=0;
				while( a[j]=='+'){
					a[j]='-';
					j++;
				}
			}
			if( a[i]=='+' ) continue;
			ans++;
			for(int j=0;j<(i+1)/2;j++){
				swap( a[j], a[i-j]);
			}
	//		cout<<i<<" "<<a<<endl;
			for(int j=0;j<=i;j++){
				if( a[j]=='-') a[j]='+';
				else a[j]= '-';
			}
	//		cout<<i<<" "<<a<<endl;
		}
		cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
}