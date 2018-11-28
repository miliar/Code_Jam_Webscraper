/***********************
By : Sujay Kumar
Sat 11 Apr 2015 11:57:12 AM IST

************************/

#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<cstdio>
#include<cstring>
#include<cmath>

#define printexpr(EXPR) cout << #EXPR << " : " << EXPR << endl
#define newline std::cout << std::endl
#define printstr(STR) std::cout << STR << std::endl
#define rep(n) for(int i=0;i<n;++i)
#define reprev(n) for(int i=n-1;i>=0;--i)

typedef long long int ll;
using namespace std;


main()
{
	int cases,i;
	FILE *in = fopen("input.txt","r"),*out = fopen("output.txt","w");
	fscanf(in,"%d",&cases);
	for(i=0;i<cases;++i)
	{
	  int max,ans = 0;
	  char a[1005];
	  fscanf(in,"%d%s",&max,a);
	  int len = strlen(a),j,sum=a[0]-'0';
	  
	  for(j=1;j<len;++j)
	  {
	    if(sum<j){ans+=(j-sum);sum+=(j-sum);}
	    sum += a[j]-'0';
	  }
	  fprintf(out,"Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
