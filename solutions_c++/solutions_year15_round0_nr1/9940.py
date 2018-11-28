#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <string>
#include <limits>

using namespace std;

int solve(){
    int m,pp=0,inv=0;
    string s;
    cin >> m >> s;
    for (int i=0;i<=m;i++){
        if (pp>=i)
           pp+=s[i]-48;
        else if(s[i]-48>0){
             inv+=i-pp;
             pp+=inv;
             pp+=s[i]-48;
             }
        }
    return inv;
    }

int main(void){
    int t;
    cin >> t;
    for (int i=1;i<=t;i++){
        cout << "Case #" << i << ": " << solve() << endl;
        }
    return 0;
    }
