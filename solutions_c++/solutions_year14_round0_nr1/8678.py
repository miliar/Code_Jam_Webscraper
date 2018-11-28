#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<vector>
#define LL long long
#define DEBUG if(0)

using namespace std;

int main()
{
    int t;
    int a[4][4], b[4];
    scanf("%d",&t);
    for (int casen=1;casen<=t;casen++)
    {
        int choice;
        scanf("%d",&choice);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);
        }
        choice--;
        for (int i=0;i<4;i++)
        b[i]=a[choice][i];

        scanf("%d",&choice);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            scanf("%d",&a[i][j]);
        }

        choice--;
        int flag=0;
        int ans;
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
            if (a[choice][i]==b[j]&&flag==0)
            {
                flag=1;
                ans=b[j];
            }
            else if (a[choice][i]==b[j]&&flag==1)
            {
                flag=-1;
                break;
            }
            }

        }

        DEBUG
        {
            for (int i=0;i<4;i++)
            cout<<a[choice][i]<<"   ";
            cout<<endl;
            for (int i=0;i<4;i++)
            cout<<b[i]<<"   ";
            cout<<endl;
        }
        if (flag==1)
        printf("Case #%d: %d\n",casen,ans);
        else if(flag==0)
        printf("Case #%d: Volunteer cheated!\n",casen);
        else
        printf("Case #%d: Bad magician!\n",casen);

    }
}
