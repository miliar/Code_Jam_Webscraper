#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int t,k,n,i,j,c,c1;
    float a[11],b[11];
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>n;
        c=c1=0;
        for(i=0;i<n;i++)
            cin>>a[i];
        for(i=0;i<n;i++)
            cin>>b[i];

        sort(a,a+n);
        sort(b,b+n);

        i=j=n-1;
        while(i>-1)
        {
            if(a[i]>b[j])
            {
                i--;
                c++;
            }
            else
            {
                j--;
                i--;
            }
        }

        i=j=0;
        while(i<n)
        {
            if(a[i]>b[j])
            {
                i++;
                j++;
                c1++;
            }
            else
            {
                i++;
            }
        }
        cout<<"Case #"<<k<<": "<<c1<<" "<<c<<endl;
    }
    return 0;
}
