#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define pb(VALUE) push_back(VALUE)
#define pob() pop_back()
#define mp(FST,SEC) make_pair(FST,SEC)
#define len(STR) STR.length()
#define F first
#define S second
#define INF 2000000000

#define refresh(ARRAY,TARGET,VALUE) frdn(DEFINED_I,0,TARGET)ARRAY[DEFINED_I]=VALUE
#define watch(VALUE) {cout<<#VALUE;printf("=");cout<<VALUE;printf("\n");}
#define stop exit(0)

using namespace std;

int a[100000];
int x,y,n,m,p,t,ans;



int main(){ 
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   scanf("%d",&t);
    for(int p=1;p<=t;p++)
       {
          scanf("%d%d",&x,&n);
          for(int i=0;i<n;i++)
           scanf("%d",&a[i]);
          sort(a,a+n);     
          if (x==1)
             {
                cout << "Case #" << p << ": " << n << endl;
                continue;
             }
          ans=INF;      
          for(int i=0;i<n;i++)
           {
              int tt=x;
              int temp=0;
              for(int j=0;j<n-i;j++)
               if (a[j]<tt) tt+=a[j]; else
                  {
                         while (tt<=a[j])
                         {
                         temp++;
                         tt=tt*2-1;   
                         }
                         tt+=a[j];
                  }
              ans=min(temp+i,ans);
           }
          ans=min(ans,n);
           cout << "Case #" << p << ": " << ans << endl;
       }
    
  
return 0;
}
