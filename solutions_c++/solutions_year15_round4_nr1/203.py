#include <iostream>
using namespace std;
char t[200][200];
int main() {
    int tt;
    cin>>tt;
    for(int i = 1; i <= tt; ++i) {
        cout<<"Case #"<<i<<": ";
        int r,c;
        cin>>c>>r;
        for(int i = 0; i < c; ++i) {
            for(int j = 0; j < r; ++j) {
                cin>>t[i][j];
            }
        }
        int ans = 0;
        for(int i = 0; i < c; ++i) {
            for(int j = 0; j < r; ++j) {
                if(t[i][j] != '.') {
                int lol = 0;
                if(t[i][j] == '^') {
                    for(int k = i-1; k >= 0; --k) {
                        if(t[k][j] != '.') {
                            lol = 1;
                        }
                    }
                }
                if(t[i][j] == '>') {
                    for(int k = j+1; k < r; ++k) {
                        if(t[i][k] != '.') {
                            lol = 1;
                        }
                    }

                }
                if(t[i][j] == 'v') {
                    for(int k = i+1; k < c; ++k) {
                        if(t[k][j] != '.') {
                            lol = 1;
                        }
                    }
                }
                if(t[i][j] == '<') {
                    for(int k = j-1; k >= 0; --k) {
                        if(t[i][k] != '.') {
                            lol = 1;
                        }
                    }
                }
                int lul = 0;
                for(int k = i-1; k >= 0; --k) {
                    if(t[k][j] != '.') {
                        lul = 1;
                    }
                }
                for(int k = j+1; k < r; ++k) {
                    if(t[i][k] != '.') {
                        lul = 1;
                    }
                }
                for(int k = i+1; k < c; ++k) {
                    if(t[k][j] != '.') {
                        lul = 1;
                    }
                }
                for(int k = j-1; k >= 0; --k) {
                    if(t[i][k] != '.') {
                        lul = 1;
                    }
                }
                if(!lol) {
                    if(!lul) {
                        cout<<"IMPOSSIBLE\n";
                        goto ohi;
                    }
                    else {
                        ++ans;
                    }
                }
                }
            }
        }
        cout<<ans<<'\n';
        ohi:;
    }

}
