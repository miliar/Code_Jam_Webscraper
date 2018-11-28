#include<stdio.h>
#include<string.h>
#include<vector>
#include<iostream>

#include<algorithm>
#include<set>
#define max 200000
using namespace std;

typedef long long int ll;

char str1[200];
char str2[200];
int len[200];
int cal(int i,int j)
{
    if(i>=strlen(str1) && j>=strlen(str2))
       return 0;
  else if(str1[i]!=str2[j] && str1[i]==str1[i-1])
        return(1+cal(i+1,j));
        
        else if(str1[i]!=str2[j] && str2[j]==str2[j-1])
        return(1+cal(i,j+1));
          else if(str1[i]==str2[j])
         return(cal(i+1,j+1));
           else if(str1[i]!=str2[j])
        return(-1);
            }
int main()
{int i,j,k,t,n,mini;
scanf("%d",&t);
for(j=1;j<=t;j++)
{
          scanf("%d",&n);
 scanf("%s",str1);
 scanf("%s",str2);
 mini=cal(0,0);
 if(mini<0)
  printf("Case #%d: Fegla Won\n",j); 
  else
  printf("Case #%d: %d\n",j,mini); 
                        


                          
          }
          return 0;
    }
