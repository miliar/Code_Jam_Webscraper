/*
 * =============================================================
 *
 *       Filename:  grass.cpp
 *    Description:  
 *         Author:  Shitikanth Kashyap (), shitikanth1@gmail.com
 *   Organization:  University of Waterloo
 *
 * ==============================================================
 */

#include <cstdio>
#include <cstdlib>
#include <set>
#include <algorithm>

using namespace std;

int main() {
    int T, N, M;
    int pattern[10005];
    bool valid[10005];
    int h;
    set<int> heights;
    scanf("%d",&T);
    for (int t=1; t<=T; t++){
        scanf("%d %d", &N,&M);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++){
                scanf("%d",&h);
                pattern[i*100+j]=h;
                heights.insert(h);
            }
        set<int> :: iterator it = heights.begin();

        bool possible = true;
        while(++it != heights.end()){
            int large = *it;
            it--;
            int small = *it;
            it++;
//            printf("> %d %d\n",small,large);


            for (int i = 0; i < N; ++i)
                for (int j = 0; j < M; ++j)
                    valid[i*100+j]=false;

            // Row cuts
            for (int i = 0; i < N; ++i){
                bool flag=true;
                for (int j = 0; j < M; ++j) {
                    if(pattern[i*100+j]!=small){
                        flag= false;
                        break;
                    }
                }
                if(flag){
        //            printf(">>> Row %d\n",i);
                    for (int j = 0; j < M; ++j)
                        valid[i*100+j]=true;
                }
            }

            // Column cuts
            for (int j = 0; j < M; ++j){
                bool flag=true;
                for (int i = 0; i < N; ++i) {
                    if(pattern[i*100+j]!=small){
                        flag= false;
                        break;
                    }
                }
                if(flag){
                    //printf(">>> Column %d\n",j);
                    //printf(">>>>");
                    for (int i = 0; i < N; ++i){
                        //printf(" %d",pattern[i*100+j]);
                        valid[i*100+j]=1;
                    }
                }
            }

            for (int i = 0; i < N; i++)
                for (int j=0; j < M; j++) 
                    if(pattern[i*100+j]==small){
                        if(valid[i*100+j])
                            pattern[i*100+j]=large;
                        else {
                            possible=false;
                            break;
                        }
                    }

            if(!possible){
                break;
            }
        }
        printf("Case #%d: ",t);
        if(possible)
            printf("YES\n");
        else
            printf("NO\n");
    }
}

