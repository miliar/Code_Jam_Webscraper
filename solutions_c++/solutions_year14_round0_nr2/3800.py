#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("ques.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int t,ctr =0;;
	scanf("%d",&t);
	double min,nextval,val,c,f,x;
	while(t--){
		ctr++;
		scanf("%lf%lf%lf",&c,&f,&x);
		min = x/2;
		val = 0.0;
		for(double i = 2;;i=i+f){
			val = val + c/i;
			nextval = x/(i+f);
			if(min > (val+nextval) ){
				min = val+nextval;
			} else{
				printf("Case #%d: %0.7lf\n",ctr,min);
				break;
			}
		}
	}
	fclose(stdout);
}
