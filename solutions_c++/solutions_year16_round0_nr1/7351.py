#include<stdio.h>
#include<iostream.h>
#include<vector>
#define TEST int t;scanf("%d",&t);int T = t;while(t--)
using namespace std;
int main(){
    int N,n,i,digfound; vector<int> v(10);
    TEST{
         scanf("%d",&N);
         printf("Case #%d: ",T-t);
         if(N==0){
                  printf("INSOMNIA\n");
         }
         else{
              std::fill(v.begin(), v.end(), 0);
              i = digfound = 0;
              while(1){
                       i++;
                       n = N*i;
                       while(n){
                                v[n%10]++;
                                if(v[n%10] == 1){
                                           digfound++;
                                }
                                n /= 10;
                       }
                       if(digfound == 10){
                                   break;
                       }
              }
              printf("%d\n",N*i);
         }
    }
}
