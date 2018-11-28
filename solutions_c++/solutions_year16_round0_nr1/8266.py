#include <iostream>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <iomanip>
#define  fi(i,a,b)  for(int i=a;i<b;i++)
#define  fd(i,a,b)  for(int i=a;i>b;i--)
#define  si(n)      scanf("%d",&n);
#define  sc(n)      scanf("%c",&n);
#define  sll(n)     scanf("%lld",&n);
#define  TC         int T; si(T);

using namespace std;
int length(int n);
int genMax(int n);
bool checkResult();
int H[10] = {0};
int main(){
   TC
   int t = T;
   while(T--){
     fi(i,0,10)
        H[i] = 0;
     int n;
     cin >> n;
     if(n == 0)
        cout << "Case #" << t - T << ": " << "INSOMNIA"  << endl;
     else{
        int l = length(n);
        int maxNum = genMax(l+1);
        int noOfIteration = maxNum/n;
        int flag = 0;
        int ans = 0;
        fi(i,1,noOfIteration+1){
           int t = n*i;
           int len_t = length(t);
           fd(j,len_t-1,-1){
              int d = t/pow(10.0,j);
              H[d] = 1;
              t = t - d*pow(10.0,j);
           }
           if(checkResult()){
              ans = n*i;
              break;
           }
        }
       cout << "Case #" << t - T << ": " << ans  << endl;
     }
   }
   return 0;
}

int genMax(int n){
   int sum = 0;
   fi(i,0,n)
      sum += (9*pow(10.0,i));
   return sum;
}

int length(int n){
   int i = 1;
   while(pow(10.0,i) <= n)
      i++;
   return i;
}

bool checkResult(){
    if (H[0] == 1 && H[1] == 1 && H[2] == 1 && H[3] == 1 && H[4] == 1 && H[5] == 1 && H[6] == 1 && H[7] == 1 && H[8] == 1 && H[9] == 1)
        return true;
    else
        return false;
}
