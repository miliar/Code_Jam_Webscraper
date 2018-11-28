#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
int main()
{
    int T,x,y,num,k;
    int s1[4][4],s2[4][4];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
              cin>>x;
              for(int i=0;i<4;i++)
                 for(int j=0;j<4;j++)
                     cin>>s1[i][j];
              cin>>y;
              for(int i=0;i<4;i++)
                 for(int j=0;j<4;j++)
                     cin>>s2[i][j];
              num=0;
              x--;y--;
              for(int i=0;i<4;i++)
                if(num<=1)
                 for(int j=0;j<4;j++)
                 {
                         if(s1[x][i]==s2[y][j])
                            num++,k=s1[x][i];
                 }
                 else break;
              if(num==0)
                 cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
              else if(num==1)
                     cout<<"Case #"<<t<<": "<<k<<endl;
                     else cout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
    }
    fclose(stdout);
} 
