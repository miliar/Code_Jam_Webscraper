#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<cctype>
#define mn(a,b) a>b?b:a
#define loop(n,i) for(int i=0;i<n;i++)
#define mx(a,b) a>b?a:b
#define PI 3.14159
#define start int main(){
#define put printf
#define get scanf
#define end return 0;}
typedef long long int ll;
typedef unsigned long long int ull;
using namespace std;
/* CODER: prassi */
/* If its hard to write, it should be hard to read.. */
start
	int t,i;
	ull rings,r,pnt;
	FILE *in,*out;
	in=fopen64("in.txt","r");
	out=fopen64("out.txt","w");
	fscanf(in,"%d",&t);
	loop(t,i)
	{
		fscanf(in,"%lld %lld",&r,&pnt);
		int j=1;
		ull sum=0,cnt=0;
		while(sum<pnt)
		{
			sum+=((r+j)*(r+j)-(r+j-1)*(r+j-1));
			//put("%lld\t",sum);
			j+=2;
			if(sum<=pnt)
			cnt++;
		}
		//put("\n");
		fprintf(out,"Case #%d: %d\n",i+1,cnt);
	}
end
