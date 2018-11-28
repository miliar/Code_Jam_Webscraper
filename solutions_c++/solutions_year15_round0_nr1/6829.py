//@l0os3r

#define _CRT_SECURE_NO_DEPRECATE
#include<bits/stdc++.h>
using namespace std;
//data types

#define ll long long
#define vi vector<int>
#define pii pair<int, int>
#define vpii vector<pii> 
#define si set<int> 
#define msi map<string, int>
//loops
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define TRvi(c, it) for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 
#define MEMSET_INF 127 
#define MEMSET_HALF_INF 63 
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); 

#define sci(z) scanf("%d",&z)
#define scli(z) scanf("%ld",&z)
#define sclli(z) scanf("%lld",&z)
#define scc(z) scanf("%c",&z);


int main()
{
//prime();
int t,cass=1;
sci(t);
//precompute

while(t--)
{
int smax;
sci(smax);
//int son[smax+1];
string son;
cin>>son;
int summ=0,nti=0;
for(int i=0;i<son.length();i++)
{
//printf("%d %d ",i,summ);
if(summ<i)
{nti+=i-summ;
summ=i;
}

summ+=(son[i]-'0');
//printf(" %d \n",nti);
}

printf("Case #%d: %d\n",cass++,nti);
}

return 0;
}

