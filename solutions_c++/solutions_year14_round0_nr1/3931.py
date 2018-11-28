#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int ans1,ans2,arr[5][5],brr[5][5],num,count=0,t;
 //   freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
    cin>>t;
    int t1=1;
    while(t1<=t)
    {
        count=0;
        cin>>ans1;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>arr[i][j];

        cin>>ans2;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>brr[i][j];

        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(arr[ans1][i]==brr[ans2][j])
                {
                    count++;
                    num=arr[ans1][i];
                    break;
                }
            }
        }

        if(count==1)
            cout<<"Case #"<<t1<<": "<<num<<"\n";
        else if(count==0)
            cout<<"Case #"<<t1<<": "<<"Volunteer cheated!"<<"\n";
        else
            cout<<"Case #"<<t1<<": "<<"Bad magician!"<<"\n";
        t1++;
    }
//getch();
    return 0;
}
