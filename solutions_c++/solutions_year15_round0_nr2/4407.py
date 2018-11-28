#include <bits/stdc++.h>
using namespace std;

vector <int> v2 ;
int main(){
    int T , D , P , cas = 0 ;
    freopen("B-small-attempt4.in", "rt", stdin);
    freopen("By3out.txt", "wt", stdout);
    scanf("%d",&T);
    while(T--){
        v2.clear();
        scanf("%d",&D);
        for(int i = 0 ; i < D ; i++){
            scanf("%d",&P);
            v2.push_back(P);
        }
        sort(v2.begin(),v2.end());
        int Min = 12 ;
        for(int i = 0 ; i <(1<<9) ; i++){
            int cnt = 0 ;
            vector <int>v = v2;
            for(int j = 0 ; j < 9 ; j++){
                if(((1<<j)&i)){
                    if(v[v.size()-1] <= 3){
                        continue;
                    }
                    cnt++;
                    int a = v[v.size()-1];
                    if(a == 9){
                        v[v.size()-1] = 3;
                        v.push_back(6);
                        sort(v.begin(),v.end());
                        continue;

                    }
                    v[v.size()-1] = (a+1)/2;
                    v.push_back(a/2);
                    sort(v.begin(),v.end());
                }else{
                    if(v[v.size()-1] <= 0){
                        continue;
                    }
                    cnt++;
                    for(int k = 0 ; k < v.size() ; k++){
                        v[k]--;
                    }
                }
            }
            if(v[v.size()-1] > 0){
                 cnt += v[v.size()-1];
            }
            Min = min(Min,cnt);
        }
        printf("Case #%d: %d\n",++cas,Min);
    }
}
