#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;
int mat[102][102];
int main(){
    int N, T;
    string s;
    cin>>T;
    for(int t = 1; t <= T; t++){
        cin>>N;
        vector<string>S, C;
        memset(mat, 0, sizeof(mat));
        for(int i = 0; i < N; i++){
            cin>>s;
            S.push_back(s);
            char last = s[0];
            string x = "";
            int cnt = 1, idx = 0;
            for(int j = 1; j < (int)s.size() ; j++){
                if(s[j] == last)cnt++;
                else{
                    x += last;
                    mat[i][idx++] = cnt;
                    last = s[j], cnt = 1;
                }
            }
            x += last;
            mat[i][idx++] = cnt;
            C.push_back(x);
            //cout<<x<<endl;
        }

        //for(int i=0;i<(int)C.size();i++)cout<<C[i]<<" ";puts("");

        int ok = 1;
        for(int i = 1; i < (int)C.size() && ok; i++){
            if( !(C[0] == C[i]) )ok = 0;
        }
        if(ok){
            int len = C[0].size(), ans = 0;
            for(int i = 0; i < len; i++){
                int M = 1, ope = 1000000000;

                for(int j = 0; j < N; j++)
                    M = max (M, mat[j][i]);

                for(int k = 1; k <= M; k++){
                    int sum = 0;
                    for(int j = 0; j < N; j++){
                        sum += abs(mat[j][i] - k);
                    }
                    ope = min(ope, sum);
                }

                ans += ope;
            }
            printf("Case #%d: %d\n",t,ans);
        }
        else{
            printf("Case #%d: Fegla Won\n", t);
        }
    }
    return 0;
}
