#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

char str[101];

char filp[2][2] = {{'+','-'},{'-','+'}};

void solve(int t){
    cin >> str;
    int len = strlen(str);
    int start = 0;
    int end = len - 1;
    int ind = 0;
    int ans = 0;
    while(end >= start){
        int pos = ind % 2;
        int postive = filp[pos][0];
        int negative = filp[pos][1];
        if(pos == 0){
            if(str[end] == negative){
                if(str[start] == postive){
                    while(str[start] == postive && start < end){
                        start += 1;
                    }
                    ans += 1;
                }else{
                    while(str[start] == negative && start < end){
                        start += 1;
                    }
                }
                ans += 1;
                ind += 1;
            }
            else
                end--;
        }else{
            if(str[start] == negative){
                if(str[end] == postive){
                    while(str[end] == postive && end > start){
                        end--;
                    }
                    ans += 1;
                }else{
                    while(str[end] == negative && end > start){
                        end--;
                    }
                }
                ans += 1;
                ind += 1;
            }else
                start += 1;
        }
    }
    cout << "Case #" << t << ": " << ans << endl;
    return;
}

using namespace std;
int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;++t){
        solve(t);
    }

    return 0;
}
