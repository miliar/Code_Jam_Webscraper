#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    int t,p[4][4],q[4][4],x=1,i,j,c_no,a_no;
    int a,b;
    freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        c_no=0;
        cin>>a;
        a=a-1;
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            cin>>p[i][j];
        }
        cin>>b;
        b=b-1;
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
            cin>>q[i][j];
        }
        for(i=0;i<4;++i)
        {
            for(j=0;j<4;++j)
                if(p[a][i]==q[b][j])
            {
                c_no=1+c_no;
                a_no=p[a][i];
            }
        }
            if(c_no==1)
            {
                cout<<"Case #"<<x<<": "<<a_no<<"\n";

            }
            else if(c_no>1)
            {
                cout<<"Case #"<<x<<": "<<"Bad magician!"<<"\n";

            }
            else
            {
                cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<"\n";

            }
            x=x+1;
    }


    return 0;
}
