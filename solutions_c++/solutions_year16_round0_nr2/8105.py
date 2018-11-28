#include<stdio.h>
#include<iostream>
#include<vector>
#define gc getchar
#define TEST int t;scanf("%d",&t);gc();int T = t;while(t--)
using namespace std;
int main(){
    int N,i,rotations; char status,c; vector<char> v;
    TEST{
                       v.clear();
                  while((c = gc()) != '\n'){
                          v.push_back(c);
                  }
                  rotations = 0;
                  if(v[0] == '-'){
                          status = '-';
                  }
                  else status = '+';
                  for(i = 1;i<v.size();i++){
                        if(status == v[i]) continue;
                        if(v[i] == '-' && status == '+'){
                                rotations++;
                                status = '-';
                                continue;
                        }
                        if(v[i] == '+' && status == '-'){
                                rotations++;
                                status = '+';
                                continue;
                        }
                  }
                  printf("Case #%d: ",T-t);
                  if(status == '+')
                  printf("%d\n",rotations);
                  else
                  printf("%d\n",rotations+1);
         }
}
