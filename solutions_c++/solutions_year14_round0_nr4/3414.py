#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int t,k,i,j,n,war,dwar,x,y,lx,rx,ly,ry;
    double q1[1000],q2[1000];
    cin>>t;
    t++;
    for(k=1;k<t;k++)
    {
        war=0;
        dwar=0;
        cin>>n;
        for(i=0;i<n;i++)
            cin>>q1[i];
        for(i=0;i<n;i++)
            cin>>q2[i];
        sort(q1,q1+n);
        sort(q2,q2+n);
        for(x=0,y=0;x<n;x++)
        {
            if(q1[x]>q2[y])
            {
                dwar++;
                y++;
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(q1[i]<q2[j])
                {
                    q2[j]=0;
                    war++;
                    break;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<dwar<<" "<<n-war<<"\n";
    }
    return 0;
}
