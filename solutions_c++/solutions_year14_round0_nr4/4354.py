#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>

using namespace std;

pair <double,int> girl[1005];
pair <double,int> boy[1000];
pair <double,int> noob_girl[1005];
pair <double,int> noob_boy[1000];

int igotu (int id, int bricks){
    int ans;
    ans=1004;
    for (int c=0;c<bricks;c++){
        if (boy[id].first<girl[c].first&&girl[c].second==1){
           if (girl[c].first<girl[ans].first){
              ans=c;
              }
           }
        }
    
return ans;
    }

int igotuu (int id, int bricks){
    int ans;
    ans=1004;
    for (int c=0;c<bricks;c++){
        if (noob_girl[id].first<noob_boy[c].first&&noob_boy[c].second==1){
           if (noob_boy[c].first<noob_boy[ans].first){
              ans=c;
              }
           }
        }
    
return ans;
    }

int main (){

girl[1004] = make_pair(1,0);
noob_boy[1004] = make_pair(1,0);
int T, bricks, final, hola, help;
double aux;
scanf("%d", &T);

for (int i=0;i<T;i++){
    final=0;
    scanf("%d", &bricks);
    help=bricks;
    
    for (int k=0;k<bricks;k++){
        cin>>aux;
        girl[k]=make_pair(aux,1);
        noob_girl[k]=make_pair(aux,1);
        }
    for (int k=0;k<bricks;k++){
        cin>>aux;
        boy[k]=make_pair(aux,1);
        noob_boy[k]=make_pair(aux,1);
        }
        
    sort (girl,girl+bricks);
    sort (boy,boy+bricks);
    
    for (int s=0;s<bricks;s++){
        hola=igotu(s,bricks);
        if (hola!=1004){
           girl[hola].second=0;
           final++;
           }
        
        }

        sort (noob_girl,noob_girl+bricks);
        sort (noob_boy,noob_boy+bricks);

        for (int s=bricks-1;s>=0;s--){
            hola=igotuu(s,bricks);
            if (hola!=1004){
               noob_boy[hola].second=0;
               help--;
               }
            
            }

printf("Case #%d: %d %d\n", i+1, final, help);

    }  

return 0;
    }
