#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int n[4][4];
    int m[4],b[4];
    int t,c;
    scanf("%d",&t);
    for(int r=1;r<=t;r++)
    {
        int f=0,k=0;
        scanf("%d",&c);
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
                cin>>n[x][y];
        }
        for(int x=0;x<4;x++)
        {
            m[x]=n[c-1][x];
        }
        cin>>c;
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
                cin>>n[x][y];
        }
        for(int x=0;x<4;x++)
        {
            b[x]=n[c-1][x];
        }
        for(int x=0;x<4;x++)
        {
            for(int y=0;y<4;y++)
            {
                if(m[x]==b[y])
                {   k=m[x];
                    f++;
                    break;
                }
            }
        }
        if(f==1)
        cout<<"Case #"<<r<<": "<<k<<endl;
        else if(f>1)
        cout<<"Case #"<<r<<": Bad magician!\n";
        else if(f==0)
            cout<<"Case #"<<r<<": Volunteer cheated!\n";

    }


}
