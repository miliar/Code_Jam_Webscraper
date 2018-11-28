#include <iostream>
#include <cstdio>
#include <set>
#include <map>
#define debug
using namespace std;

struct evento{
       int pi,pf,qnt;};

bool compi(evento a,evento b){
     return a.pi < b.pi;}

bool compf(evento a,evento b){
     return a.pf < b.pf;}

evento ei[1010];
evento ef[1010];



set<int> pass;

map<int,int> qnt;


int calc(int a,int b,int c){
    
    
 int d = 0;
 
 for(int i=a+1;i<=b;i++)
         d -=  (i-a);
 
 return c*d;
    
}

main(){
       
       int te,resp,resp2;
       scanf("%d",&te);
       
       for(int t=1;t<=te;t++){
               
               int n,m;
               scanf("%d%d",&n,&m);
               resp = resp2 = 0;
                       
               for(int i=0;i<m;i++){
                       scanf("%d%d%d",&ei[i].pi,&ei[i].pf,&ei[i].qnt);
                       ef[i].pi=ei[i].pi;
                       ef[i].pf=ei[i].pf;
                       ef[i].qnt=ei[i].qnt;
                       resp += calc(ei[i].pi,ei[i].pf,ei[i].qnt);
                       }
               sort(ei,ei+m,compi);
               sort(ef,ef+m,compf);
               
               int ptri=0,ptrf=0;
               
               debug("ok");
               
               while(ptri != m || ptrf != m){
                          
                          debug("%d-%d\n",ptri,ptrf);
                          if((ei[ptri].pi <= ef[ptrf].pf || ptrf == m) && ptri!=m){//entra
                                         
                                         pass.insert(ei[ptri].pi);
                                         qnt[ei[ptri].pi] += ei[ptri].qnt;
                                         
                                         ptri++;
                                         }
                          else {//sai
                               
                                   int k = ef[ptrf].qnt;
                               debug("* %d\n",k);
                               while(k){
                                        
                                        
                                        int y = qnt[*(--pass.end())];
                                        debug("y=%d\n",y);
                                        if(!y){
                                               pass.erase(--pass.end());
                                               continue;
                                               }
                                        
                                        int tira = min(y,k);
                                        k -= tira;
                                        qnt[*(--pass.end())] -= tira;
                                        
                                        resp2 += calc(*(--pass.end()),ef[ptrf].pf,tira);
                                        
                                        }
                               
                               ptrf++;
                               }
                          
                          
                          
                          
                          
                          }
                       
               
               printf("Case #%d: %d\n",t,resp-resp2);
               
               }
               
               
               
       
       
       }
