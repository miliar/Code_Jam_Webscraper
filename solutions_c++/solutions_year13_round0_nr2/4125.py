#include <stdio.h>
#include <set>
#include <fstream>
#include <iterator>

using namespace std;

int t;
int w,h;
int lawn[105][105];
set<int> heights;
set<pair<int,int> > ok;

bool flag = true;

FILE* file;

int main(){
    
    file = fopen("lawnmower.out", "w");
    
    scanf("%d",&t);
    for(int q=0;q<t;q++){
        flag = true;
        heights.clear();
        
        scanf("%d%d",&h,&w);
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                scanf("%d",&lawn[i][j]);
                heights.insert(lawn[i][j]);
            }
        }
        
        while(!heights.empty()){
            ok.clear();
            
            for(int i=0;i<h;i++){
                if(lawn[i][0] == *heights.begin()){
                    int f = true;
                    for(int j=0;j<w;j++){
                        if(lawn[i][j] == *heights.begin()) continue;
                        f = false;
                        break;
                    }
                    if(f){
                        for(int j=0;j<w;j++) ok.insert(make_pair(i,j));
                    }
                }
            }
            
            for(int i=0;i<w;i++){
                if(lawn[0][i] == *heights.begin()){
                    int f = true;
                    for(int j=0;j<h;j++){
                        if(lawn[j][i] == *heights.begin()) continue;
                        f = false;
                        break;
                    }
                    if(f){
                        for(int j=0;j<h;j++) ok.insert(make_pair(j,i));
                    }
                }
            }
            
            
            for(int i=0;i<h;i++){
                for(int j=0;j<w;j++){
                    if(lawn[i][j] == *heights.begin()){
                        if(ok.find(make_pair(i,j))!=ok.end()){
                            ok.erase(make_pair(i,j));
                            set<int>::iterator begin = heights.begin();
                            advance(begin,1);
                            lawn[i][j] = *begin;
                            continue;
                        }
                        
                        flag = false;
                        break;
                    }
                }
            }
            heights.erase(heights.begin());
        }
        
        fprintf(file,"Case #%d: ",q+1);
        if(flag){
            printf("YES\n");
            fprintf(file,"YES\n");
        }else{
            printf("NO\n");
            fprintf(file,"NO\n");
        }   
    }
}
