#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    freopen ("google.txt","w",stdout);
    int tT;
    scanf("%d",&tT);
    int m=0;
    while(tT!=0)
    {
        char a[4][5];
        for(int i=0;i<4;i++)
        {
            scanf("%s",&a[i]);
        }

        int cc=0;
        for(int i=0;i<4;i++)
        {
            if((strcmp(a[i],"XXXX")==0) || (strcmp(a[i],"XXXT")==0) || (strcmp(a[i],"XXTX")==0) || (strcmp(a[i],"XTXX")==0) || (strcmp(a[i],"TXXX")==0))
            {
                cout<<"Case #"<<m+1<<": X won"<<endl;
                cc=1;
                break;
            }
           else if((strcmp(a[i],"OOOO")==0) || (strcmp(a[i],"OOOT")==0) || (strcmp(a[i],"OOTO")==0) || (strcmp(a[i],"OTOO")==0) || (strcmp(a[i],"TOOO")==0))
            {
                cout<<"Case #"<<m+1<<": O won"<<endl;
                cc=1;
                break;
            }

            else if((a[0][i]=='T' || a[0][i]=='O')&&(a[1][i]=='T' || a[1][i]=='O')&&(a[2][i]=='T' || a[2][i]=='O')&&(a[3][i]=='T' || a[3][i]=='O'))
            {
                cout<<"Case #"<<m+1<<": O won"<<endl;
                cc=1;
                break;
            }

             else if((a[0][i]=='T' || a[0][i]=='X')&&(a[1][i]=='T' || a[1][i]=='X')&&(a[2][i]=='T' || a[2][i]=='X')&&(a[3][i]=='T' || a[3][i]=='X'))
            {
                cout<<"Case #"<<m+1<<": X won"<<endl;
                cc=1;
                break;
            }

        }
        if(cc!=1)
        {
        int aa=0,b=0,c=0,d=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(i==j)
                {
                    if(a[i][j]=='X' || a[i][j]=='T')
                    aa++;
                    if(a[i][j]=='O' || a[i][j]=='T')
                    b++;
                }

                if(i+j==3)
                {
                    if(a[i][j]=='X' || a[i][j]=='T')
                    c++;
                    if(a[i][j]=='O' || a[i][j]=='T')
                    d++;
                }
            }
        }

        if(aa==4 || c==4)
        {
            cout<<"Case #"<<m+1<<": X won"<<endl;
            cc=1;

        }

        else if(b==4 || d==4)
        {
            cout<<"Case #"<<m+1<<": O won"<<endl;
            cc=1;

        }

        }

        if(cc!=1)
        {
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[i][j]=='.')
                {
                    cc=1;
                    cout<<"Case #"<<m+1<<": Game has not completed"<<endl;
                    break;
                }

            }
            if(cc==1)
            {
                break;
            }
        }
        }

        if(cc==0)
        {
            cout<<"Case #"<<m+1<<": Draw"<<endl;
        }

    m++;
    tT--;
    }

}
