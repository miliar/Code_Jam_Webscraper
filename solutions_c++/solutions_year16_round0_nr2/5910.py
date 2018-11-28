#include <bits/stdc++.h>
using namespace std;


string s;
int n , d[1<<16] , dir[1<<16] , len[1<<16];

int brute(){

    int inicial = 0;
    for(int i = 0; i < n; ++i){
        if(s[i] == '-'){
            inicial|=(1<<i);
        }
    }
    for(int i = 0; i < 1<<n; ++i){
        d[i] = 1e9;
    }

    d[inicial] = 0;
    queue<int> q; q.push(inicial);
    while(!q.empty()){
        int mask = q.front(); q.pop();

        vector<int> c(n , 0);
        for(int i = 0; i < n; ++i){
            if(mask & (1<<i)){
                c[i] = 1;
            }
        }

        for(int pos = 0; pos < n; pos++){
            vector<int> tmp = c;
            for(int i = 0; i < (pos+1) / 2; ++i){
                swap(tmp[i] , tmp[pos - i]);
            }
            for(int i = 0; i <= pos; ++i){
                tmp[i] = !tmp[i];
            }
            int new_mask = 0;
            for(int i = 0; i < n; ++i){
                if(tmp[i] == 1){
                    new_mask |=(1<<i);
                }
            }
            if(1 + d[mask] < d[new_mask]){
                dir[new_mask] = mask;
                len[new_mask] = pos;
                d[new_mask] = 1 + d[mask];
                q.push(new_mask);
            }
        }
    }
    /*
    vector<int> answer;
    int current = 0;
    while(current != inicial){
        answer.push_back(len[current]);
        current = dir[current];
    }
    reverse(answer.begin() , answer.end());
    for(int elem : answer){
        cout << elem <<" ";
    }
    cout << endl;*/

    return d[0];
}
int solve(){

    int answer = 0;
    while(true){
        bool ok = true;
        for(char elem : s){
            if(elem == '-'){
                ok = false;
            }
        }
        if(ok){
            break;
        }
        answer++;
        int i = 0;
        while( i < n && s[i] == s[0]){
            i++;
        }
        for(int j = 0; j < i; ++j){
            if(s[j] == '+'){
                s[j] = '-';
            }else{
                s[j] = '+';
            }
        }
    }
    return answer;
}

int main(){
    freopen("in.c","r",stdin);
   freopen("on.c","w",stdout);

    int tc , number_case = 1;
    cin >> tc;

    while(tc--){
        cin >> s;
        n = s.size();
        printf("Case #%d: %d\n",number_case++,solve());
    }





    return 0;
}
