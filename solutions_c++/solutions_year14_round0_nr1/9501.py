#include <iostream>

using namespace std;

int main()
{
    int n,m=1;
    int a[4][4],b[4][4],t1,c[4],cnt=0,number;
    cin>>n;
    while(n>0)
    {
        cnt=0;
        cin>>t1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }

        for(int i=0;i<4;i++)
        {
            c[i]=a[t1-1][i];
        }

        cin>>t1;

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }

        for(int k=0;k<4;k++)
        {
            for(int i=0;i<4;i++)
            {
                if(c[k]==b[t1-1][i])
                {
                    cnt++;
                    number=c[k];
                }
            }
        }
        if(cnt==1)
            cout<<"Case #"<<m<<": "<<number<<"\n";
        else if(cnt==0)
            cout<<"Case #"<<m<<": "<<"Volunteer cheated!"<<"\n";
        else if(cnt>0)
            cout<<"Case #"<<m<<": "<<"Bad magician!"<<"\n";

        n--;
        m++;
    }



    return 0;
}
