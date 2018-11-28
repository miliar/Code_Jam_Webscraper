#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    //freopen("fun.in", "r", stdin);
    freopen("fun.out", "w", stdout);

    int a[5][5],b[5][5];
    int T,t;
    int c[5],d[5];
    int ans_one,ans_two,ans;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>ans_one;
        int i,j;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++){
              cin>>a[i][j];
              if((ans_one-1)==i)
                c[j]=a[i][j];
            }
        cin>>ans_two;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++){
              cin>>b[i][j];
              if((ans_two-1)==i)
                d[j]=b[i][j];
            }

        int count=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(c[i]==d[j])
                {
                    ans=d[j];
                    count++;
                }
            }
        cout<<"Case #"<<t<<": ";
        if(count==1)
            cout<<ans<<endl;
        else if(count==0)
            cout<<"Volunteer cheated!"<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
    return 0;
}
