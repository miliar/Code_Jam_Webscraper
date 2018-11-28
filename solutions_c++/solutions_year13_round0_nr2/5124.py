#include <iostream>

using namespace std;
int m[200][200];
int x,y;

int main()
{
    int t;
    int n;
    int i,j,k;
    int mark;
    cin>>n;
    t=1;
    while(t<=n)
    {
        cin>>x>>y;
        for(i=0; i<x; i++)
            for(j=0; j<y; j++)
                cin>>m[i][j];
        mark = 1;
        for(i=0; i<x; i++)
        {
            for(j=0; j<y; j++)
            {
                for(k=0; k<y; k++)
                    if(m[i][k] > m[i][j])
                        break;
                if(k==y)
                    continue;
                for(k=0; k<x; k++)
                    if(m[k][j] > m[i][j])
                        break;
                if(k==x)
                    continue;
                mark = 0;
                break;
            }
            if( mark==0)
                break;
        }
        cout<<"Case #"<<t<<": ";
        if(mark == 0)
        {
            cout<<"NO"<<endl;
        }
        else
        {
            cout<<"YES"<<endl;
        }
        t++;
    }
    return 0;
}
