//Abhishek Paliwal
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<malloc.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<climits>
#include<map>

#define FOR(i,s,n) for(i=s;i<n;i++)
#define FORD(i,s,n) for(i=s;i>n;i--)
#define LL long long

using namespace std;

int main()
{
	LL ar[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321};
	int t;
	cin >> t;
	int sz=sizeof(ar)/sizeof(ar[0]);
	for (int cs=1;cs<=t;cs++) {
		LL a,b;
		cin >> a >> b;
		int ans=0;
		for (int i=0;i<sz;i++) {
			if (ar[i]>=a && ar[i]<=b) ans++;
		}
		cout << "Case #" << cs << ": " << ans << endl;
	}
	return 0;
}
