#include <iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int cases=1;cases<=T;cases++)
    {
        int a[4][4], b[4][4];
        int ans1,ans2;
        cin>>ans1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>ans2;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }
        int count=0;
        int rownum=ans1-1;
        int columnum=0;
        int sol=0;
        for(;columnum<4;columnum++)
        {
            int element = a[rownum][columnum];
            for(int i=0;i<4;i++)
            {
                if(b[ans2-1][i]==element)
                {
                    sol=element;
                    count++;
                }
            }
        }
        if(count==0)
        {
            cout<<"Case #"<<cases<<": "<<"Volunteer cheated!\n";
        }
        else if(count==1)
        {
            cout<<"Case #"<<cases<<": "<<sol<<"\n";
        }
        else
        {
            cout<<"Case #"<<cases<<": "<<"Bad magician!\n";
        }
    }
    return 0;
}
