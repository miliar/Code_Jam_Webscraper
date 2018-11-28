#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("question.txt","r",stdin);
	freopen("B_ans.txt","w",stdout);
	double c,f,x,i,a,b,j,minn;
	int t,count=1;
	scanf("%d",&t);
	while(t--) {
		scanf("%lf%lf%lf",&c,&f,&x);
		minn= x/2;
		a=minn;
		for(i=2;i<=(x/c)*f;i+=f) {
			b=0;
			for(j=2;j<=i;j+=f) {
				
				b+=c/j;
			}
			b+=x/(i+f);
			if(minn<=b) break;
			else minn=b;
		}
		printf("Case #%d: %0.7lf\n",count++,minn);
	}
	fclose(stdout);
}
