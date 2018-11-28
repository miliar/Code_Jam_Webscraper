#include<iostream>

using namespace std;
main()
{
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        int a,j,k,x;
        cin>>a;
        int aa[5];
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(j==a-1)
                    cin>>aa[k];
                else
                    cin>>x;
            }
        }
        cin>>a;
        int bb[5];
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(j==a-1)
                    cin>>bb[k];
                else
                    cin>>x;
            }
        }
        int y[5],cc=-1;
        for(j=0;j<4;j++)
        {
            x=aa[j];
            for(k=0;k<4;k++)
            {
                if(x==bb[k])
                    {cc++;y[cc]=x;}
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(cc==-1)
            cout<<"Volunteer cheated!";
        else if(cc==0)
            cout<<y[cc];
        else
            cout<<"Bad magician!";
        cout<<endl;
    }
}
