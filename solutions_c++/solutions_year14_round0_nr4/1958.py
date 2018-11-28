#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
float a[1005],b[1005];
int n;
int dwar()
{
    int i,j,k,l,cnt=0;
    for(j=n-1;j>=0;j--)
    {
     for(i=0;i<n;i++)
     if(b[j]<a[i])
     {
         cnt++;
         b[j]=0;
         a[i]=0;
         break;
     }
     if(i==n)
     {
         b[j]=0;
         k=0;
         while(a[k]==0)
         k++;
         a[k]=0;
     }

    }
    return cnt;

}

int war()
{
    int i,j,k,l,cnt=0,e=n-1;
    for(j=n-1;j>=0;j--)
    {
        if(a[j]>b[e])
        {
            cnt++;
        }
        else
        e--;
    }
    return cnt;
}


int main()
{
	int j,t,i,k;

	scanf("%d",&t);
	k=1;//printf("%.7f\n",500.0/6);
	while(t--)
	{
	    cin>>n;
	    for(i=0;i<n;i++)
	    scanf("%f",&a[i]);
	    for(i=0;i<n;i++)
	    scanf("%f",&b[i]);
	    sort(a,a+n);
	    sort(b,b+n);

	    /*for(i=0;i<n;i++)
	    printf("%f ",a[i]);
	    cout<<"\n";
	    for(i=0;i<n;i++)
	    printf("%f ",b[i]);

        */
         //cout<<dwar()<<"\n";
        printf("Case #%d: %d %d\n",k,dwar(),war());
        k++;
     }
return 0;
}
