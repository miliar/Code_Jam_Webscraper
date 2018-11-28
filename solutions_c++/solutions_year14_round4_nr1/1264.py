#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int T;

void solve(int t){
     int n,x;
     vector<int> s;
     scanf("%d %d",&n,&x);
     for (int i=0;i<n;i++){
         int filesize;
         scanf("%d",&filesize);
         s.push_back(filesize);
         }
     sort(s.begin(),s.end());
     int res=0;
     int l=0;
     int d=n-1;
     while (l<d){
           if (s[l]+s[d]<=x){
               l++;
               d--;              
               } else d--;
           res++;
           }   
     if (l==d) res++;       
     printf("Case #%d: %d\n",t,res);
     }


int main(){
    scanf("%d",&T);
    for (int i=0;i<T;i++) solve(i+1);
    return 0;
    }
