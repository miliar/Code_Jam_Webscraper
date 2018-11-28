
#include <vector>
#include <queue>
#include <deque>
#include <map>
#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define s1(x) scanf("%d",&x)
#define sll(x) scanf("%lld",&x)
#define sf(x) scanf("%lf",&x)
#define ss(x) scanf("%s",&x)
#define f(i,a,b) for(int i=a;i<b;i++)
#define fr(i,n)  f(i,0,n)

typedef long long ll;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
   int T;
    s1(T);
    int r1,r2;
    int A[16],B[16];
   for(int i=1;i<=T;i++)
   {
       s1(r1);
       for(int j=0;j<16;j++) s1(A[j]);
       s1(r2);
       for(int j=0;j<16;j++) s1(B[j]);
       int found=0;
       int val;
       for(int j=4*(r1-1);j<4*r1;j++)
       {
           for(int k=4*(r2-1);k<4*r2;k++)
           {
                if(A[j]==B[k]) 
                {
                    found++;
                    val=A[j];
                }
           }
       }
       if(found==0) cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
       if(found==1) cout<<"Case #"<<i<<": "<<val<<endl;
       if(found>1) cout<<"Case #"<<i<<": Bad magician!"<<endl;

   } 
    return 0;
}
