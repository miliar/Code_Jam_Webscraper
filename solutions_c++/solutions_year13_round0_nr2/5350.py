#include <iostream>

using namespace std;

int m[200][200];
int x,y;

int main()
{
    int i,j,k;
    int t=1;
    int n;
    cin>>n;
    while(t<=n)
    {
        cin>>x>>y;
        for(i=0;i<x;i++)
            for(j=0;j<y;j++)
                cin>>m[i][j];
        int mark = 1;
        for(i=0;i<x;i++)
        {
            for(j=0;j<y;j++)
            {
                mark = 1;
                for(k=0; k<y; k++)
                {
                    if(m[i][k]>m[i][j])
                    {
                        mark = 0;
                        break;
                    }
                }
                if(mark == 1)
                    continue;
                mark = 1;
                for(k=0; k<x; k++)
                {
                    if(m[k][j]>m[i][j])
                    {
                        mark=0;
                        break;
                    }
                }
                if(mark == 1)
                    continue;
                break;
            }
            if(mark == 0)
                break;
        }
        cout<<"Case #"<<t<<": ";
        if(mark == 0)
            cout<<"NO"<<endl;
        else
            cout<<"YES"<<endl;
        t++;
    }
    return 0;
}
