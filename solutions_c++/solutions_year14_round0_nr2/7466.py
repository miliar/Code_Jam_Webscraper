#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>

#define REP(i,a,b) for(int i=a;i<=b;i++)
#define sf scanf
#define pf printf

using namespace std;
const int MAXN = 100005;

FILE *fin = fopen("B-large.in","r");
FILE *fout= fopen("data.out","w");

double c,f,x;
double ans,r;

int main(){

	int t; fscanf(fin,"%d",&t);
	REP(it,1,t){
		fscanf(fin,"%lf%lf%lf",&c,&f,&x);
		ans = 0; r = 2.0;
		while (1){
			if( x/r>(x/(r+f)+c/r) ){ 
				ans += c/r; r+=f;
			}
			else break;
		}
		ans += x/r;
		fprintf(fout,"Case #%d: %.7lf\n",it,ans);
	}

	return 0;
}