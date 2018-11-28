#include <bits/stdc++.h>

using namespace std;

int myarray[100005];

int main()
{
    freopen("jam1.txt","r",stdin);
    freopen("jamout.txt","w",stdout);

    int t,n,ttest,i,cnter,pink,jvd,summer,k;
    scanf("%d",&t);
    for(ttest=1;ttest<=t;ttest++)
    {
        cin>>n;
         int maxi=-1;
        for(i=0;i<n;i++)
        {
         scanf("%d",&myarray[i]);
        if(myarray[i]>maxi)
            maxi=myarray[i];
        }
         cnter=0;
        for(i=1;i<n;i++)
         {
           if(myarray[i]<myarray[i-1])
            cnter+=(myarray[i-1]-myarray[i]);
         }
        printf("Case #%d: %d ",ttest,cnter);
		 pink=0;
         jvd=0;
          summer=0;
         for(int k=0;k<=maxi;k++)
          {
		    int f=0;
             pink=0;
              summer=0;
        for(int i=0;i<n-1;i++)
        {
          if(myarray[i]<pink)
            {
               f=1;
            break;
            }
            else
            {
            if(myarray[i]<k)
            {
            pink=0;
            summer+=myarray[i];
            }
            else
            {
              summer+=k;
              pink=myarray[i]-k;
            }
            }
         }
          if(f==0 && myarray[n-1]>=pink)
          	    {
                printf("%d\n",summer);
          	    	   break;
          	    }
          }
    }
}
