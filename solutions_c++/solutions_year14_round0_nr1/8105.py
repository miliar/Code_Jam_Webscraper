#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("output.in","wt",stdout);
    int t,x,y,j,j1,a,z,c,i,nb;
    int m1[4][4];
    cin>>t;
    for (i=0;i<t;i++)
    {
        cin>>x;
        for(j=0;j<4;j++)
            for(j1=0;j1<4;j1++)
                {
                    cin>>a;
                    m1[j][j1]=a;
                }
        cin>>y;

        for(j=0;j<y-1;j++){
            for(j1=0;j1<4;j1++)
                cin>>a;
                }
        c=0;
        for(j=0;j<4;j++)
            {
                cin>>a;
                for(j1=0;j1<4;j1++)
                    if(m1[x-1][j1]==a){
                        c=c+1;
                        nb=a;
                    }
            }
        if(c==0)
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        if(c==1)
            cout<<"Case #"<<i+1<<": "<<nb<<endl;
        if(c>1)
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
            for(j=y;j<4;j++){
            for(j1=0;j1<4;j1++)
                cin>>a;
                }
        }
        fclose(stdin);
        fclose(stdout);
    return 0;
}
