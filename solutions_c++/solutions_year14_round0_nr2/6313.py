#include<cstdio>
#include<iostream>
#define gc getchar_unlocked
using namespace std;
void inline scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
int main(){
	int t;
	double c,f,x;
	double coo_per_sec=2.0;
	int total_coo=0;
	double time1=0.0;
	scanint(t);
	int count=0,count1=1;
	while(t--){
	scanf("%lf",&c);
	scanf("%lf",&f);
	scanf("%lf",&x);
	time1+=x/coo_per_sec;
	while((c/coo_per_sec)+(x/(coo_per_sec+f))<x/coo_per_sec)
	{
		if(time1>1.0*c/coo_per_sec&&count==0){
			time1=0;
		}
		time1+=1.0*c/coo_per_sec;
		coo_per_sec+=f;
		count++;
	}
	if(count>0)
	time1+=1.0*x/coo_per_sec;
	printf("Case #%d:",count1);
	printf(" %.7lf\n",time1);
	count=0;
	time1=0.0;
	coo_per_sec=2;
	count1++;
}
	return 0;
}
