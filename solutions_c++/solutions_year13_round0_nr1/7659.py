#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
    int t;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("test.out","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++)
    {
         string s[5];
         for(int i=0;i<4;i++)
         cin>>s[i];
         int a[4][4];
         for(int i=0;i<4;i++)
         {
             for(int j=0;j<4;j++)
             {
                 if(s[i][j]=='X')
                 a[i][j]=5;
                 if(s[i][j]=='O')
                 a[i][j]=7;
                 if(s[i][j]=='T')
                 a[i][j]=0;
                 if(s[i][j]=='.')
                 a[i][j]=111;
             }
         }
         int x=0;int y=0;
         int m=0,n=0;
         for(int i=0;i<4;i++)
         {
             int ans1=0,ans2=0;
             for(int j=0;j<4;j++)
             {
                 ans1+=a[i][j];
                 ans2+=a[j][i];
             }
            // cout<<"i "<<i<<" "<<ans1<<" "<<ans2<<endl;
             m+=a[i][i];
             n+=a[3-i][i];
             if(ans1==20||ans1==15)
             {x=1;break;}
             if(ans1==21||ans1==28)
             {y=1;break;}
             if(ans2==20||ans2==15)
             {x=1;break;}
             if(ans2==21||ans2==28)
             {y=1;break;}
          }
         // cout<<m<<" "<<n<<endl;
             if(m==20||m==15)
             x=1;
             if(m==21||m==28)
             y=1;
             if(n==20||n==15)
             x=1;
             if(n==21||n==28)
             y=1;
             int bo=0;
             if((x||y)==0)
             {
                 for(int i=0;i<4;i++)
                 {
                     for(int j=0;j<4;j++)
                     if(a[i][j]==111)
                     bo=1;
                 }
             }
            // cout<<x<<" "<<y<<endl;
             if(x==1)
             printf("Case #%d: X won\n",cas);
             else if(y==1)
             printf("Case #%d: O won\n",cas);
             else if (bo==1)
             printf("Case #%d: Game has not completed\n",cas);
             else
             printf("Case #%d: Draw\n",cas);
    }
   return 0;

}
