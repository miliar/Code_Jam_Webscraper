#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
using namespace std;

double s1[1100],s2[1100];
int T,t;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            cin>>t;
            for(int j=0;j<t;j++)
            cin>>s1[j];
            for(int j=0;j<t;j++)
            cin>>s2[j];
            sort(s2,s2+t);
            sort(s1,s1+t);
            int x=0,y=0,c1=0,c2=0;
            while (x<t&&y<t)
            {
               if (s1[x]<s2[y])
                 x++;
              else{
                 x++;
                 y++;
                 c1++;
                 }
            }
            x=0;y=0;
            while (x<t&&y<t){
                if (s2[y]<s1[x])
                y++;
                else{
                  x++;
                  y++;
                  c2++;
                }
            } 
              
            printf("Case #%d: %d %d\n",i,c1,t-c2);
    }
    fclose(stdout);
} 
