#include<cstdio>
#include<cstring>
#include<iostream>

using namespace std;

int main(){
	
	int t,i,cas=1;
	double c,f,x,ans,t1,t2,cur;
	
	scanf("%d",&t);
	
	while(t--){
		scanf("%lf%lf%lf",&c,&f,&x);
		
		ans=0;
		cur=2;
		
		while( (x>c)&& ((t1=x/cur)>(t2=(c/cur)+x/(f+cur)))){
			ans+=(c/cur);
			cur+=f;
			}
			
		ans+=(x/cur);
		
		printf("Case #%d: %.7lf\n",cas,ans);
		cas++;
	}
	
	return 0;
	}
		
		