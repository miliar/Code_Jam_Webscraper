#include<stdio.h>
#include<algorithm>
#include<map>
#include<list>
#include<queue>
#include <iostream>
#include<memory.h>
#define MAXN 500050
using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(false);
    //freopen("C:\\A.in", "r", stdin);
    //freopen("C:\\A.out", "w", stdout);
    int TC;
    int n; string s;
    cin >> TC;
    for(int test_case = 1; test_case<=TC; ++test_case){
        cin >> n >> s;
        int res = 0;
        int curr_count = 0;
        curr_count = s[0]-'0';
        for(int i=1; i<s.size(); ++i){
            if(curr_count < i){
                int friends_to_bring = i-curr_count;
                res+= friends_to_bring;
                curr_count+= friends_to_bring;
            }
            curr_count+= s[i]-'0';
        }
        cout << "Case #" << test_case << ": " << res << "\n";
    }
    return 0;
}
