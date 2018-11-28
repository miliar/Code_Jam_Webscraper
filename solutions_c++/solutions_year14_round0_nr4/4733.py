#include <iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;

int main() {
freopen("D-large.in","r",stdin);
     freopen("b.txt","w",stdout);
	int T,p,q,t,i,N,count_1=0,count_2=0;
	double a[1001],b[1001];
	scanf("%d",&T);
	t=1;
	while(t<=T){
		scanf("%d",&N);
		for(i=1;i<=N;i++)
			scanf("%lf",&a[i]);

			for(i=1;i<=N;i++)
			scanf("%lf",&b[i]);
			sort(a+1,a+N+1);
		    sort(b+1,b+N+1);
		    p=q=1;
		    count_1=count_2=0;
	while(1)
		{


	if(b[q]<a[p])
			{	count_1++;
             p++;
             q++;
			}


else
            p++;
			if(p==N+1||q==N+1)
            break;
		}
 p=q=1;
 count_2=0;
	while(1)
		{
			if(b[q]>a[p])
			{
	         	count_2++;
                p++;
                q++;
}
			else
            q++;
			if(p==N+1||q==N+1)
            break;
		}

		printf("Case #%d: %d %d\n",t,count_1,N-count_2);
		t++;
	}

	return 0;
}
