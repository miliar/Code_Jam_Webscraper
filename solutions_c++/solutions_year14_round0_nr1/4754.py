#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int t,c=0;
    cin>>t;
    while(t--)
    {
        c++;
        int arr[17][2];
        int brr[4][4];
        for(int i=1;i<=16;i++){arr[i][0]=-1;arr[i][1]=-1;}
        int ch;
        cin>>ch;
        ch--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>brr[i][j];
            }
        }
        for(int j=0;j<4;j++)
        {
            arr[brr[ch][j]][0]=1;
        }
        cin>>ch;
        ch--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>brr[i][j];
            }
        }
        for(int j=0;j<4;j++)
        {
            arr[brr[ch][j]][1]=1;
        }
        int ans=-1;
        for(int i=1;i<=16;i++)
        {
           if(arr[i][0]==1&&arr[i][1]==1)
           {
               if(ans==-1)ans=i;
               else ans=0;
           }
        }
        if(ans==-1)
        {
            printf("Case #%d: Volunteer cheated!\n",c);
        }
        else if(ans==0)
        {
            printf("Case #%d: Bad magician!\n",c);
        }
        else
        {
            printf("Case #%d: %d\n",c,ans);
        }
    }
}

