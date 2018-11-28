#include<iostream>
#include<stdio.h>
#include<string>
#include<algorithm>
#include<string.h>
#include<stdlib.h>
using namespace std;

int main()
{
    freopen("q.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {
        int xc=0,yc=0,dc=0,tc=0,flag=0;
        int arr[7][7];
        char stri[5][5];
        for(int h=1;h<=7;h++)
        {
            memset(arr[h],0,sizeof(arr[h]));
        }
        cout<<"Case #"<<i<<": ";
        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                cin>>stri[j][k];
                if(stri[j][k]=='X') arr[j][1]++;
                if(stri[j][k]=='O') arr[j][2]++;
                if(stri[j][k]=='T') arr[j][3]++;
                if(stri[j][k]=='.') dc++;
            }
        }

        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                if(stri[k][j]=='X') arr[j][4]++;
                if(stri[k][j]=='O') arr[j][5]++;
                if(stri[k][j]=='T') arr[j][6]++;
            }
        }

        int h=1;
        for(int p=1;p<=4;p++)
        {
            if(arr[p][1]==3 && arr[p][3]==1)
            {
                cout<<"X won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][2]==3 && arr[p][3]==1)
            {
                cout<<"O won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][1]==4)
            {
                cout<<"X won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][2]==4)
            {
                cout<<"O won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][4]==3 && arr[p][6]==1)
            {
                cout<<"X won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][5]==3 && arr[p][6]==1)
            {
                cout<<"O won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][4]==4)
            {
                cout<<"X won"<<endl;
                flag=1;
                break;
            }
            else if(arr[p][5]==4)
            {
                cout<<"O won"<<endl;
                flag=1;
                break;
            }
        }

        if(flag==0)
        {
            int g=1;
            for(int o=1;o<=4;o++)
            {
                if(stri[o][g]=='X') xc++;
                if(stri[o][g]=='O') yc++;
                if(stri[o][g]=='T') tc++;
                g++;
            }
            if(xc==4 || xc==3 && tc==1)
            {
                cout<<"X won"<<endl;
                flag=1;
            }
            else if(yc==4 || yc==3 && tc==1)
            {
                cout<<"O won"<<endl;
                flag=1;
            }
            g=4;
            xc=0,yc=0,tc=0;
            for(int o=1;o<=4;o++)
            {
                if(stri[o][g]=='X') xc++;
                if(stri[o][g]=='O') yc++;
                if(stri[o][g]=='T') tc++;
                g--;
            }
            if(xc==4 || xc==3 && tc==1)
            {
                cout<<"X won"<<endl;
                flag=1;
            }
            else if(yc==4 || yc==3 && tc==1)
            {
                cout<<"O won"<<endl;
                flag=1;
            }
        }

        if(flag==0 && dc>0) cout<<"Game has not completed"<<endl;
        else if(flag==0) cout<<"Draw"<<endl;
        //getchar();
    }
    return 0;
}
