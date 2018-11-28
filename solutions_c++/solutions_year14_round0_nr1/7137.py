#include <iostream>
#include <stdio.h>

using namespace std;
const int MAX_N = 5;
const int N = 4;
int a[MAX_N][MAX_N];
int b[MAX_N][MAX_N];
int main()
{
    int t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin>>t;
    int copt=t;
    while(t--)
    {
        int ans1,ans2;
        cin>>ans1;
        int i,j;
        for(i=1;i<=N;i++)
        {
            for(j=1;j<=N;j++)
            cin>>a[i][j];
        }
        cin>>ans2;
        for(i=1;i<=N;i++)
        {
            for(j=1;j<=N;j++)
                cin>>b[i][j];
        }
        int temp, num, counum;
        num=counum=temp=0;
        for(i=1;i<=N;i++)
        {
            temp=a[ans1][i];
            for(j=1;j<=N;j++)
            {
                if(b[ans2][j]==temp)
                {
                    num++;
                    counum=temp;
                    break;
                }
            }
        }
        cout<<"Case #"<<copt-t<<": ";
        if(num==1)
            cout<<counum<<endl;
        else if(num==0)
            cout<<"Volunteer cheated!"<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
