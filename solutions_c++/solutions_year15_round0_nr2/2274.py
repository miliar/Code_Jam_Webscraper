#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int t,k=1;
    cin>>t;
    while(t--)
    {
        int n,i,count,x,v=0;
        cin>>n;
        int a[1000],p[1000];
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        sort(a,a+n);
        for(x=1;x<=a[n-1];x++)
        {   count=0;
            for(i=0;i<n;i++)
            {   
                if(a[i]>x)
                {
                    if(a[i]%2==0)
                    count+=(a[i]-1)/x;
                    else
                    count+=(a[i]-1)/x;
                }
                
            }
            p[v++]=count+x;
        }
        sort(p,p+v);
        cout<<"Case #"<<k++<<": ";
        cout<<p[0]<<endl;
    }
    return 0;
}
