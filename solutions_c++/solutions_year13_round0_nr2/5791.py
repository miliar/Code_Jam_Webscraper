#include<cstring>
#include<set>
#include<cstdio>
#include<iostream>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int c=1; c<=T; c++){
        int n,m;
        scanf("%d %d",&n,&m);
        int grass[n][m];
        int vL[n],vC[m];
        int minimo = 0x3f3f3f3f;
        set<int> values;
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                scanf("%d",&grass[i][j]);
                values.insert(grass[i][j]);
//                minimo = min(minimo,grass[i][j]);
            }
        }
        if(n==1 || m==1){
            printf("Case #%d: YES\n",c);
        }
        else{
            bool possible = true;
            set<int>::iterator it = values.end();
            --it;
            values.erase(it);
            for(set<int>::iterator it=values.begin(); it!=values.end(); it++){
                minimo = *it;
                memset(vL,0,sizeof(vL));
                memset(vC,0,sizeof(vC));
                for(int i=0;i<n;i++){
                    int j=0;
                    while(grass[i][j]==minimo && j<m) j++;
                    if(j==m) vL[i] = 1;
                }
                for(int j=0;j<m;j++){
                    int i=0;
                    while(grass[i][j]==minimo && i<n) i++;
                    if(i==n) vC[j] = 1;
                }
                for(int i=0; i<n; i++){
                    for(int j=0; j<m; j++){
                        if(grass[i][j] == minimo && (vL[i]==0 && vC[j]==0))
                            possible = false;
                    }
                    if(!possible) break;
                }
                if(!possible) break;
            }
/*            int mij[2][8] = {{-1,-1,-1,0,0,1,1,1},{-1,0,1,-1,1,-1,0,1}};
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    for(int k=0; k<7; k++){
                        for(int l=k+1; l<8; l++){
                            if(mij[0][k]!=mij[0][l] && mij[1][k]!=mij[1][l]){
                                int ik = i+mij[0][k];
                                int il = i+mij[0][l];
                                int jk = j+mij[1][k];
                                int jl = j+mij[1][l];
                                if(ik>=0 && ik<n && il>=0 && il<n && jk>=0 && jk<m && jl>=0 && jl<m){
                                    if(grass[i][j]<grass[ik][jk] && grass[i][j]<grass[il][jl] && (grass[i][j]>=grass[ik][jl] || grass[i][j]>=grass[il][jk])){
                                        possible = false;
//                                        printf("%d %d, %d %d, %d %d\n",i,j,ik,jk,il,jl);
                                    }
                                }
                            }
                        }
                    }*/
/*                    if(i==0){
                        if(j==0){
                            if(grass[i][j] < grass[i+1][j] && grass[i][j] < grass[i][j+1])
                                possible = false;
                        }
                        else if(j==(m-1)){
                            if(grass[i][j] < grass[i+1][j] && grass[i][j] < grass[i][j-1])
                                possible = false;
                        }
                        else{
                            if(grass[i][j] < grass[i+1][j] && (grass[i][j] < grass[i][j+1] || grass[i][j] < grass[i][j-1]))
                                possible = false;
                        }
                    }
                    else if(i==(n-1)){
                        if(j==0){
                            if(grass[i][j] < grass[i-1][j] && grass[i][j] < grass[i][j+1])
                                possible = false;
                        }
                        else if(j==(m-1)){
                            if(grass[i][j] < grass[i-1][j] && grass[i][j] < grass[i][j-1])
                                possible = false;
                        }
                        else{
                            if(grass[i][j] < grass[i-1][j] && (grass[i][j] < grass[i][j+1] || grass[i][j] < grass[i][j-1]))
                                possible = false;
                        }
                    }
                    else{
                        if(j==0){
                            if((grass[i][j] < grass[i-1][j] || grass[i][j] < grass[i+1][j]) && grass[i][j] < grass[i][j+1])
                                possible = false;
                        }
                        else if(j==(m-1)){
                            if((grass[i][j] < grass[i-1][j] || grass[i][j] < grass[i+1][j]) && grass[i][j] < grass[i][j-1])
                                possible = false;
                        }
                        else{
                            if((grass[i][j] < grass[i-1][j] || grass[i][j] < grass[i+1][j]) && (grass[i][j] < grass[i][j+1] || grass[i][j] < grass[i][j-1]))
                                possible = false;
                        }
                    }*/
               // }
//            }
            printf("Case #%d: %s\n",c,(possible)? "YES" : "NO");
        }
    }
    return 0;
}
