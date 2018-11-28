// Author : Muhammad Rifayat Samee
// Problem :
// Algorithm:
#pragma warning (disable : 4786)
#pragma comment(linker, "/STACK:16777216")

#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#define MAX(a,b) (a>b)?a:b
#define MIN(a,b) (a<b)?a:b

#define pi (2*acos(0.0))
#define eps 1e-7

#ifdef ONLINE_JUDGE
#define i64 long long
#else
#define i64 __int64
#endif

using namespace std;
i64 INF;
i64 A[1000005];
i64 s,n;
i64 min(i64 a,i64 b){
	if(a<b)return a;
	return b;
}
int main(){

	//freopen("in.txt","r",stdin);
	freopen("A-small-attempt7.in","r",stdin);
	freopen("A14.out","w",stdout);
	INF = 1000000;
	INF = INF * INF;
	i64 cases,res,i,j,k,ts,ct=1;
	scanf("%I64d",&cases);
	while(cases--){
		scanf("%I64d %I64d",&s,&n);
		for(i=0;i<n;i++){
			scanf("%I64d",&A[i]);
		}
		sort(A,A+n);
		res = INF;
		
		for(k=0;k<n;k++){
			i64 r = 0;
			ts = s;
			for(i=0;i<=k;i++){
				i64 t = 0;
				if(ts<=A[i]){
					if(ts-1<=0){
						r = INF;
						break;
					}
					while(ts<=A[i]){
						ts = ts + ts - 1;
						t++;
					}
					r = r + t;
					ts = ts + A[i];
				}
				else{
					ts = ts + A[i];
				}
			}
			r  = r + n-k-1;
			if(r>=INF)r = n;
			res = min(res,r);
			res = min(res,n);
			//if(res>=INF)res = n;
		}
		printf("Case #%I64d: %I64d\n",ct++,res);
	}
	return 0;
}
