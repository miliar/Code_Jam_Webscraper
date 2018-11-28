#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    for(int d=1;d<=t;d++)
    {
            int n;
            cin>>n;
            double a[n],b[n];
            for(int i=0;i<n;i++)
            scanf("%lf",&a[i]);
            for(int i=0;i<n;i++)
            scanf("%lf",&b[i]);
            
            sort(a,a+n);
            sort(b,b+n);
            
            
            int k1=0,n1=0,j=0;
            for(int i=0;i<n;i++)
            {
                    
                    
                    if(a[i]>b[j])
                    {
                                 n1++;
                                 j++;
                    }
                    
            }
            for(int i=0;i<n;i++)
            {
                    for(int j=0;j<n;j++)
                    {
                            if(a[i]<b[j])
                            {k1++;b[j]=0;break;
                            }
                    }
            }
                            
            printf("Case #%d: %d %d\n",d,n1,n-k1);
    }
    return 0;
}
            
