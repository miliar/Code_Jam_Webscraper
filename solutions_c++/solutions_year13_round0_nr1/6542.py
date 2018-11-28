#include <fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
int main()
{
    int t, i, j, k, flag, ans;
    fin>>t;
    int res[t];
    for(i=0;i<t;i++)
                    res[i]=3;
    char a[t][4][4];
    for(i=0;i<t;i++)
    {
                     for(j=0;j<4;j++)
                     {
                                     for(k=0;k<4;k++)
                                     {
                                                     fin>>a[i][j][k];
                                                     if(a[i][j][k]=='.')
                                                                        res[i] = 4;
                                     }
                     }
    }
    for(i=0;i<t;i++)
    {
                    for(j=0;j<4;j++)
                    {
                                    flag=1;
                                    for(k=0;k<4;k++)
                                    {
                                                    if(a[i][j][k]!='X' && a[i][j][k]!='T')
                                                    {
                                                                       flag = 0;
                                                                       break;
                                                    }
                                    }
                                    if(flag==1)
                                               break;
                    }
                    if(flag==1)
                    {
                               res[i]=1;
                               continue;
                    }
                    for(j=0;j<4;j++)
                    {
                                    flag=1;
                                    for(k=0;k<4;k++)
                                    {
                                                    if(a[i][k][j]!='X' && a[i][k][j]!='T')
                                                    {
                                                                       flag = 0;
                                                                       break;
                                                    }
                                    }
                                    if(flag==1)
                                               break;
                    }
                    if(flag==1)
                    {
                               res[i]=1;
                               continue;
                    }
                    flag=1;
                    for(j=0;j<4;j++)
                    {
                                    if(a[i][j][j]!='X' && a[i][j][j]!='T')
                                    {
                                                       flag = 0;
                                                       break;
                                    }
                    }
                    if(flag==1)
                    {
                               res[i]=1;
                               continue;
                    }
                    flag=1;
                    for(j=0, k=3;j<4;j++, k--)
                    {
                               if(a[i][j][k]!='X' && a[i][j][k]!='T')
                                    {
                                                       flag = 0;
                                                       break;
                                    }
                    }
                    if(flag==1)
                    {
                               res[i]=1;
                               continue;
                    }
//--------------------------------------------------End of X-----------------------
                    for(j=0;j<4;j++)
                    {
                                    flag=1;
                                    for(k=0;k<4;k++)
                                    {
                                                    if(a[i][j][k]!='O' && a[i][j][k]!='T')
                                                    {
                                                                       flag = 0;
                                                                       break;
                                                    }
                                    }
                                    if(flag==1)
                                               break;
                    }
                    if(flag==1)
                    {
                               res[i]=2;
                               continue;
                    }
                    for(j=0;j<4;j++)
                    {
                                    flag=1;
                                    for(k=0;k<4;k++)
                                    {
                                                    if(a[i][k][j]!='O' && a[i][k][j]!='T')
                                                    {
                                                                       flag = 0;
                                                                       break;
                                                    }
                                    }
                                    if(flag==1)
                                               break;
                    }
                    if(flag==1)
                    {
                               res[i]=2;
                               continue;
                    }
                    flag=1;
                    for(j=0;j<4;j++)
                    {
                                    if(a[i][j][j]!='O' && a[i][j][j]!='T')
                                    {
                                                       flag = 0;
                                                       break;
                                    }
                    }
                    if(flag==1)
                    {
                               res[i]=2;
                               continue;
                    }
                    flag=1;
                    for(j=0, k=3;j<4;j++, k--)
                    {
                               if(a[i][j][k]!='O' && a[i][j][k]!='T')
                                    {
                                                       flag = 0;
                                                       break;
                                    }
                    }
                    if(flag==1)
                    {
                               res[i]=2;
                               continue;
                    }
//------------------------------------End of Y---------------------------------
    }
    for(i=0;i<t;i++)
    {
                    if(res[i]==1)
                                 fout<<"Case #"<<i+1<<": X won \n";
                    else if(res[i]==2)
                                 fout<<"Case #"<<i+1<<": O won \n";
                    else if(res[i]==3)
                                 fout<<"Case #"<<i+1<<": Draw \n";
                    else if(res[i]==4)
                                 fout<<"Case #"<<i+1<<": Game has not completed \n";
    }
    return 0;
}
