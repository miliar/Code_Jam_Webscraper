#include<iostream>
#include<cstdio>
using namespace std;
int a[10];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        char s[2500];
        scanf("%s",&s);
        for(i=0;s[i]!='\0';i++)
        {
            if(s[i]=='Z')
                {
                    a[0]++;
                    a[1]--;
                }
            else if(s[i]=='O')
                a[1]++;
            else if(s[i]=='W')
                {
                    a[2]++;
                    a[3]--;
                    a[1]--;
                }
            else if(s[i]=='T')
                a[3]++;
            else if(s[i]=='S')
                a[7]++;
            else if(s[i]=='U')
               {

                  a[4]++;
                  a[5]--;
                  a[1]--;
               }
            else if(s[i]=='F')
                a[5]++;
           // else if(s[i]=='V')

            else if(s[i]=='G')
                {
                    a[8]++;
                    a[3]--;
                }
            else if(s[i]=='X')
                {
                    a[6]++;
                    a[7]--;
                    //a[9]--;
                }
            else if(s[i]=='I')
            {
                a[9]++;
            }


        }
        if(a[6]>0)
                a[9]-=a[6];
            if(a[5]>0)
                a[9]-=a[5];
            if(a[8]>0)
                a[9]-=a[8];
        printf("Case #%d: ",k);
        for(j=0;j<=9;j++)
            {
                if(a[j]>0)
                {
                    while(a[j]>0)
                       {
                            printf("%d",j);
                            a[j]--;
                       }

                }
                else
                    a[j]=0;
            }
        printf("\n");
    }
}
