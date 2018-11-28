/*Magic Trick*/
#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out1_small.txt","w",stdout);
    int t;
    cin>>t;
    //cout<<t<<endl;
    int cas=1;
    while(t--)
    {   int a[4][4],b[4][4],c,d,count1[17]={0},i,j;
        cin>>c;
        for(i=0;i<4;i++)
        {   for(j=0;j<4;j++)
            {   cin>>a[i][j];
                if(i==c-1)
                    count1[a[i][j]]++;
            }
        }
        cin>>d;
        for(i=0;i<4;i++)
        {   for(j=0;j<4;j++)
            {   cin>>b[i][j];
                if(i==d-1)
                    count1[b[i][j]]++;
            }
        }
        int flag=0,ans=0;
        for(i=1;i<=16;i++)
        {   if(count1[i]==2)
            {   if(flag==1)
                {   ans=-1;
                    break;
                }
                else
                {   flag=1;
                    ans=i;
                }
            }
        }
        cout<<"Case #"<<cas<<": ";
        if(ans==0)
            cout<<"Volunteer cheated!\n";
        else if(ans==-1)
            cout<<"Bad magician!\n";
        else
            cout<<ans<<endl;
        cas++;
    }
    return 0;
}
