#include <iostream>

using namespace std;

int main()
{   int a,b,c,d,e=1,f,i,j,ar[5][5],ar1[6][6],ct=0;
    cin>>a;
    while(e<=a)
    {
    ct=0;
    cin>>b;
    for(i=1;i<=4;i++)
    {   for(j=1;j<=4;j++)
        {   cin>>ar[i][j];
        }
    }
    cin>>c;
    for(i=1;i<=4;i++)
    {   for(j=1;j<=4;j++)
        {   cin>>ar1[i][j];
        }
    }
    for(i=1;i<=4;i++)
    {   for(j=1;j<=4;j++)
        {   if(ar[b][i]==ar1[c][j])
            {   ar1[5][0]=ar[b][i];
                ct++;
            }
        }
    }
    if(ct==1)
        cout<<"Case #"<<e<<": "<<ar1[5][0]<<endl;
    else if(ct==0)
        cout<<"Case #"<<e<<": Volunteer cheated!"<<endl;
    else
        cout<<"Case #"<<e<<": Bad magician!"<<endl;
    e++;
    }
    return 0;
}
