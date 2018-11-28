#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        int n,win=0,warwin=0,ip=0,u;
        double x,y;
        vector<double>nmi;
        vector<double>nmi0;
        vector<double>ken;
        vector<double>ken0;

        cin>>n;
        for(int j=1;j<=n;j++)
        {
            cin>>x;
            nmi.push_back(x);
            nmi0.push_back(x);
        }

        for(int j=1;j<=n;j++)
        {
            cin>>y;
            ken.push_back(y);
            ken0.push_back(y);
        }

        sort(nmi.begin(), nmi.end());
        sort(nmi0.begin(), nmi0.end());
        sort(ken.begin(), ken.end());
        sort(ken0.begin(), ken0.end());

        for(int y=0;y<n;y++)
        {
            for(int h=0;h<n;h++)
            {
                if(ken[y]>nmi[h])
                {
                    nmi[h]=100;
                    warwin++;
                    break;
                }
            }
        }

        u=n-1;

        for(int y=0;y<n;y++)
        {
            ip=0;

            for(int h=0;h<n;h++)
            {
                if(nmi0[y]<ken0[h] && h==u)
                {
                    ken0[h]=-1;
                    ip=1;
                    u-=1;
                    break;
                }
                else if(nmi0[y]>ken0[h] && ken0[h]!=-1)
                {
                    ken0[h]=-1;
                    break;
                }
            }
            if(ip==1) win++;
        }

        warwin=n-warwin;
        win=n-win;

        cout<<"Case #"<<i<<": "<<win<<" "<<warwin<<endl;
    }

    return 0;
}

