#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
//#define TANVIR
#define N 1000
int test,Case,n,war,deceit;
double naomi[N],ken[N];
int main(){
#ifdef TANVIR
//	freopen("in.txt","r",stdin);
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	register int i,start,Ke;
	scanf("%d",&test);
	for(Case=1;Case<=test;Case++){
		deceit=war=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%lf",&naomi[i]);
		for(i=0;i<n;i++)scanf("%lf",&ken[i]);
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		for(start=0,i=Ke=n-1;i>=0;i--){
			if(naomi[i]>ken[Ke])
				start++,war++;
			else
				Ke--;
		}
		int Ns,Ne,Ks;
		for(Ks=Ns=i=0,Ne=Ke=n-1;i<n;i++){
			if(ken[Ke]>naomi[Ne])
				Ke--,Ns++;
			else{
				if(naomi[Ns]>ken[Ks])
					deceit++,Ns++,Ks++;
				else
					Ke--,Ns++;
			}
		}
		printf("Case #%d: %d %d\n",Case,deceit,war);
	}
}