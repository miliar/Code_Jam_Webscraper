#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
using namespace std;


int testcase, N;
string str;
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> testcase;
    for(int caseid = 1; caseid <= testcase; caseid ++){
        cin >> N;
        cin >> str;
        int cnt = str[0]-'0';
        int ans = 0;
        for(int i=1; i< N+1; i++){
            int x = str[i]-'0';
         //   cout << i << " " << x << " " << cnt << " " << ans << endl;
            if(i > cnt && x!= 0){
                int d = i - cnt;
                ans += d;
                cnt += d;
          //      cout << ans << endl;
            }
            cnt += x;
        }
        printf("Case #%d: %d\n", caseid, ans);
    }
    return 0;
}
