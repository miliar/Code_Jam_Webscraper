#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <limits.h>
#define ll long long int
#define mod 1000000009
using namespace std;

int a[6][6];
int b[6][6];
int t[20];

int main()
{

 // freopen("C:\\Users\\jack\\Desktop\\in.txt","r",stdin);
 //freopen("C:\\Users\\jack\\Desktop\\out.txt","w",stdout);

   
    int test=1,ca;
    scanf("%d",&ca);
    
    while(test<=ca)
    {
         int c1,c2;
         for(int i=1;i<=16;i++)t[i]=0;
         
         scanf("%d",&c1);
         
         for(int i=1;i<=4;i++)
         for(int j=1;j<=4;j++)
         {
          scanf("%d",&a[i][j]);       
          if(i==c1)t[a[i][j]]++;
          }



        scanf("%d",&c2);
         
         for(int i=1;i<=4;i++)
         for(int j=1;j<=4;j++)
         {
          scanf("%d",&b[i][j]);  
          if(i==c2)t[b[i][j]]++;     
                 
          }
          
          int two=0,gg;
          for(int i=1;i<=16;i++)
          {
                  if(t[i]>1){two++;gg=i;}
            }
          if(two==1){printf("Case #%d: %d\n",test,gg);}
          else if(two==0){printf("Case #%d: Volunteer cheated!\n",test);}
          else {printf("Case #%d: Bad magician!\n",test);}
          test++;
                 }

    }
