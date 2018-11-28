#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int m,n;
int c[100];
char str[100][1000];
int sum;
int md;

void dfs(int x){
    if(x==m){
        int d = 0;
        for( int i=0; i<n; i++ ){
            vector<string> a;
            for( int j=0; j<m; j++ ){
                if(c[j]==i){
                    a.push_back(str[j]);
                }
            }
            if(a.size()){
                d++;
                sort(a.begin(),a.end());
                d += a[0].size();
                for( int k=1; k<a.size(); k++ ){
                    d+= a[k].size();
                    for( int j=0; j<a[k].size() && j<a[k-1].size(); j++ ){
                        if(a[k][j]==a[k-1][j]){
                            d--;
                        }else break;
                    }
                }
            }
        }
        if(d>md){
            md = d;
            sum = 1;
        }else if(d==md){
            sum++;
        }
    }else{
        for( int i=0; i<n; i++ ){
            c[x] = i;
            dfs(x+1);
        }
    }
}

int main(){
    int TT;
    scanf("%d",&TT);
    for( int tt=0; tt<TT; tt++ ){
        scanf("%d %d",&m,&n);
        for( int i=0; i<m; i++ ){
            scanf("%s",str[i]);
        }
        md = 0;
        sum = 0;
        dfs(0);
        printf("Case #%d: %d %d\n",tt+1,md,sum);
    }
    return 0;
}
