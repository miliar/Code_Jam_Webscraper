#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t1,x1,y1,j1,j11,a1,z1,c1,i1,nb1;
    int M[4][4];

    freopen("A-small-attempt5.in","rt",stdin);
    freopen("output.in","wt",stdout);

    cin>>t1;
    for (i1=0;i1<t1;i1++)
    {
        cin>>x1;
        for(j1=0;j1<4;j1++)
            for(j11=0;j11<4;j11++)
                {
                    cin>>a1;
                    M[j1][j11]=a1;
                }
        cin>>y1;

        for(j1=0;j1<y1-1;j1++){
            for(j11=0;j11<4;j11++)
                cin>>a1;
                }
        c1=0;
        for(j1=0;j1<4;j1++)
            {
                cin>>a1;
                for(j11=0;j11<4;j11++)
                    if(M[x1-1][j11]==a1){
                        c1=c1+1;
                        nb1=a1;
                    }
            }
        if(c1==0)
            cout<<"Case #"<<i1+1<<": Volunteer cheated!"<<endl;
        if(c1==1)
            cout<<"Case #"<<i1+1<<": "<<nb1<<endl;
        if(c1>1)
            cout<<"Case #"<<i1+1<<": Bad magician!"<<endl;
            for(j1=y1;j1<4;j1++){
            for(j11=0;j11<4;j11++)
                cin>>a1;
                }
        }
}
