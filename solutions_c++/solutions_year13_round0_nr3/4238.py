/*Author : Anupam Kanyal : GAMBIT */
// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>

using namespace std;

#define FOR(i,a,b) 	for(int i= (int )a ; i < (int )b ; ++i)
#define fill(x,v)	memset(x,v,sizeof(x))
#define	sd(n)		scanf("%d",&n)
#define slld(n)		scanf("%lld",&n)
#define sf(n)		scanf("%lf",&n)
#define ss(n)		scanf("%s",n)
#define MOD 1000000007

typedef long long LL;

#define SORT(A) sort(A.begin(),A.end())


int main()
{
	int n;
	long long a,b;
	long long int arr[47] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321};
	cin>>n;
	for(int j =1;j<=n;j++){
		cin>>a>>b;
		int count= 0;
		for(int i=0;i<47;i++){
			if(arr[i] >= a  && arr[i] <= b)
				count ++;
		}
		cout<<"Case #"<<j<<": "<<count<<endl;
	}
	return 0;
}
