#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int t,m,n,tmp,cas=0;
int map[100][100];
bool ok(int a,int b){

     int pre=map[a][b],i;
     for(i=0; i<n; ++i){
             if(map[a][i]>pre) break;
             }
     if(i==n) return true;
     for(i=0; i<m; ++i){
             if(map[i][b]>pre) break;
             }
     if(m==i) return true;
     return false;
     }
struct node{
       int h,x,y;
       bool operator < (node other) const{
            return h < other.h;
            }
       }map2[10000];
int main(){
    freopen("1.txt","w",stdout);
   
    scanf("%d",&t);
    while(t--){
               scanf("%d%d",&m,&n);
               for(int i=0; i<m; ++i){
                       for(int j=0; j<n; ++j){
                               scanf("%d",&tmp);
                               map[i][j]=tmp;
                               map2[i*n+j].x=i;
                               map2[i*n+j].y=j;
                               map2[i*n+j].h=tmp;
                               }
                       }
               bool OK=true;
               sort(map2,map2+m*n);
               for(int i=0; i<m*n; ++i){
                       if(ok(map2[i].x,map2[i].y)==0) { OK=false; break;}
                       }
               printf("Case #%d: ",++cas);
               if(OK) printf("YES\n");
               else printf("NO\n");
               
               }
    }
