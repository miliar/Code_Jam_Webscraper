#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int f[101][101];

int getFreq(char *s, int n, int* arr){
    char ch = s[0];
    int x = 1;
    int ptr = 0;
    for(int i = 1; i < n; i++){
        if(s[i] == s[i-1]){
            x++;
        }
        else {
            ch = s[i];
            arr[ptr] = x;
            x = 1;
            ptr++;
        }
    }
    arr[ptr] = x;
    ptr++;
    return ptr;
}
int getNS(char *s, int n, char *ns){
    int np = 1;
    ns[0] = s[0];
    for(int i = 1; i < n; i++){
        if(s[i] == s[i-1])
            continue;
        else {
            ns[np++] = s[i];
        }
    }
    return np;
}
int main(){
    int tt;
    cin >> tt;
    for(int t = 1; t <= tt; t++){
        bool won = true;
        int n;
        char s[101];
        char ns[101];
        int np = 0;
        int sc = 0;
        int v1 = 0, v = 0;
        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> s;
            if(!v){
               v = getFreq(s, strlen(s), f[i]);
               np = getNS(s, strlen(s), ns);
            }
            else{
                v1 = getFreq(s, strlen(s), f[i]);
            }
            if(v1 && v != v1){
                won = false;
            }
            if(v1){
                char nn[101];
                int tx = getNS(s, strlen(s), nn);
                if(tx != np){
                    won = false;
                }
                if(won)
                    for(int x = 0; x < np; x++){
                        if(nn[x] != ns[x]){
                            won = false;
                            break;
                        }
                    }
            }
        }
        int sa[101] = {0};
        if(won){
            for(int i = 0; i < v; i++){
                int mn = f[0][i], mx = f[0][i];
                for(int j = 1; j < n; j++){
                    if(f[j][i] < mn)
                        mn = f[j][i];
                    else if(f[j][i] > mx)
                        mx = f[j][i];
                    
                }
                sa[i] = mx-mn;
                sc += mx - mn;
            }
        }
        if(won)
            cout << "Case #" << t << ": " << sc << endl;
        else cout << "Case #" << t << ": Fegla Won" << endl;
    }
    return 0;
}

