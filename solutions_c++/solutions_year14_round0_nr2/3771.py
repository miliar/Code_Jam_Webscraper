#include<stdio.h>
#include<iostream>
using namespace std;
#include<conio.h>
double c,f,x,time,rate;
int test,Case;
int main(){
//	freopen("B-large.in","r",stdin);
//	freopen("out.txt","w",stdout);
	scanf("%d",&test);
	for(Case=1;Case<=test;Case++){
		cin>>c>>f>>x;
		for(rate=2,time=0;;){
			if(c/rate+x/(rate+f)>x/rate){
				time+=x/rate;
				break;
			}else{
				time+=c/rate;
				rate+=f;
			}
		}
		printf("Case #%d: %.7lf\n",Case,time);
	}
//	getch();
}