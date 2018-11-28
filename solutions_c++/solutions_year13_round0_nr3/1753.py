#include <stdio.h>
#include <stdlib.h>
// Calculate by Mathematica 8.0.4
// PAR[x_] := Module[{str = IntegerDigits[x], len},
// len = Length[str];
// For[i = 1, i <= len, i++,
//  If[str[[i]] != str[[len + 1 - i]],
//   Return[False]]];
// Return [True]
// ]
//
// Module[{i}, For[i = 1, i < 10^12, i++, If[PAR[i], If[PAR[i^2], Print[i^2]]]]]
long long table[10000]={1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,44944LL,1002001LL,1234321LL,4008004LL,
	100020001LL,102030201LL,104060401LL,121242121LL,123454321LL,125686521LL,400080004LL,404090404LL,10000200001LL,
	10221412201LL,12102420121LL,12345654321LL,40000800004LL,1000002000001LL,1002003002001LL,1004006004001LL,
	1020304030201LL,1022325232201LL,1024348434201LL,1210024200121LL,1212225222121LL,1214428244121LL,1232346432321LL,
	1234567654321LL,4000008000004LL,4004009004004LL,100000020000001LL,100220141022001LL,102012040210201LL,102234363432201LL,
	121000242000121LL,121242363242121LL,123212464212321LL,123456787654321LL};
int getres(long long beg,long long end){
	int res=0;
	for(int i=0;table[i]<=end;i++){
		if(table[i]>=beg)
			res++;
	}
	return res;
}
int main(){
	int T;
	long long beg ,end;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%lld%lld",&beg,&end);
		printf("Case #%d: %d\n",t,getres(beg,end));
	}
}