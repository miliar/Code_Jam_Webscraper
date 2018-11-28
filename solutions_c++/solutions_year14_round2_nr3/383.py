#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <stack>

#define N 10

int d[N][N];

using namespace std;
int main(){
    int nc;
    scanf("%d", &nc);
    for(int caso = 1; caso <= nc; caso++){
        int n, m;
        scanf("%d %d", &n, &m);
        
        vector<string> vs;
        for(int i = 0; i < n; i++){
            string s;
            cin>>s;
            vs.push_back(s);
        }
        
        for(int i = 0; i < m; i++){
            int u, v;
            scanf("%d %d", &u, &v);
            u--, v--;
            d[u][v] = 1;
            d[v][u] = 1;
        }
        
        vector<int> ord;
        for(int i = 0; i < n; i++) ord.push_back(i);
        
        string smin = "";
        do{
            string temp = "";
            bool val = true;
            stack<int> st;
            st.push(ord[0]);
            temp = temp + vs[ord[0]];
            for(int i = 1; i < n; i++){
                
                while(st.size() > 0 && d[ord[i]][st.top()] == 0) st.pop();
                if(st.size() == 0){
                    val = false;
                    break;
                }
                
                temp = temp + vs[ord[i]];
                st.push(ord[i]);
            }
            if(!val) continue;
            else{
                if(smin == "") smin = temp;
                else{
                    if(temp < smin) smin = temp;
                }
            }
            
        }while(next_permutation(ord.begin(), ord.end()));
        
        printf("Case #%d: ", caso);
        cout<<smin<<endl;
        
        memset(d, 0, sizeof(d));
    }
}
