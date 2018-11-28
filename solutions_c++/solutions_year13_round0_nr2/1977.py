#include<iostream>
#include<cstdio>
int input[101][101],m,n;
using namespace std;
int check()
{
    int i,j,k1,k2;
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
                k1=k2=0;
              for(int p=0;p<m;p++)
              {
                  if(input[p][j]<=input[i][j])
                  k1++;
              }
              for(int q=0;q<n;q++)
              {
                  if(input[i][q]<=input[i][j])
                  k2++;
              }
              if(k1!=m&&k2!=n)
              return 0;
        }
    }
    return 1;
}
int main()
{
    int i,j,x=1;
    int t;
    cin>>t;
    while(t--)
    {
        cin>>m;
        cin>>n;
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>input[i][j];
            }
        }
        if(check())
        {
            printf("Case #%d: YES\n",x);
        }
        else
        {
            printf("Case #%d: NO\n",x);
        }
        x++;
    }
    return 0;
}
