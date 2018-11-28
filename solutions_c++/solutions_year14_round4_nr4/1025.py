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
int N,M;
vector<string> s;



int number_of_nodes(vector<string> s){
    if (s.size()==0) return 0;
    int res=0;
    int obdelan[10];
    memset(obdelan,0,sizeof obdelan);
    vector<string> t;
    for (int i=0;i<s.size();i++){
        if (obdelan[i]==0){
           t.clear();
           for (int j=i;j<s.size();j++){
               if (s[j][0]==s[i][0]){
                  obdelan[j]=1;
                  string g=s[j];
                  g.erase(0,1);
                  if (g.size()>0) t.push_back(g);                   
                  }
               }
           res=res+1+number_of_nodes(t);    
          }
        }
    return res;
    }
     

int evaluate(vector<int> a,int m){
    int num=0;
    if (a[M-1]==m) num++;
    if (m+num!=N) return -1;
    
    int number=0;
    vector<string> t;
    for (int i=0;i<N;i++){
        t.clear();
        for (int j=0;j<a.size();j++) if (a[j]==i) t.push_back(s[j]);
        number=number+number_of_nodes(t)+1;
        }
    
    return number;
    }

void solve(int t){
     int res=0;
     int number_res=0;
     s.clear();
     
     scanf("%d %d",&M,&N);
     
     for (int i=0;i<M;i++){
         char s1[100];
         scanf("%s",s1);
         string t=s1;
         s.push_back(t);
         }
     if (M==1){
               printf("Case #%d: %d %d\n",t,s[0].size()+1,1);
               return;
               }
     
     // generate partitions
     
     vector<int> a(M,0);
     vector<int> b(M,1);
     int m=1;
     
     while (true){
           
           
           int tr=evaluate(a,m);
           
           /* for (int i=0;i<M;i++) printf("%d ",a[i]);
           
           printf("\n");
           
           for (int i=0;i<M;i++) printf("%d ",b[i]);
           printf("\n%d\n",m);*/
           
           if (tr==res) number_res++;
           if (tr>res){
                       res=tr;
                       number_res=1;
                       }
           
           if (a[M-1]!=m){
              a[M-1]++;
              continue;            
              }
           int j=M-2;
           while (a[j]==b[j]) j--;
           if (j==0) break;
           a[j]++;
           m=b[j];
           if (a[j]==b[j]) m++;
           j++;
           for (int i=j;i<M;i++){
               a[i]=0;
               b[i]=m;
               }
           a[M-1]=0;    
           }
     
     // compute the number for partitions
     
     for (int i=1;i<=N;i++) number_res=number_res*i;
     printf("Case #%d: %d %d\n",t,res,number_res);
     }





int main(){
    int T;
    scanf("%d",&T);
    for (int i=0;i<T;i++) solve(i+1);
    return 0;
    }
