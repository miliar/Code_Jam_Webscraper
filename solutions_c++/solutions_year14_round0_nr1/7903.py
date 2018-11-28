#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("ab.txt","r",stdin);
    freopen("cd.txt","w",stdout);
    int t,r1,r2,a[4][4],b[4][4],c1[16],c2[16],ans,res,x=1;
    cin>>t;
    while(t-->0)
    {
        res=0;
        cin>>r1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        }
         cin>>r2;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                cin>>b[i][j];
        }
        for(int i=0;i<16;i++)
        {
            c1[i]=0;
            c2[i]=0;
        }
        for(int i=0;i<4;i++)
            c1[a[r1-1][i]-1]++;
        for(int i=0;i<4;i++)
            c2[b[r2-1][i]-1]++;
        for(int i=0;i<16;i++)
        {
            if(c1[i]==c2[i] && c1[i]!=0)
                {
                    res++;
                    ans=i+1;
                }
        }
        if(res==1)
            cout<<"Case #"<<x<<": "<<ans<<"\n";
        else if(res==0)
            cout<<"Case #"<<x<<": Volunteer cheated!\n";
        else
            cout<<"Case #"<<x<<": Bad magician!\n";
        x++;
    }
}
