#include <bits/stdc++.h>
#pragma comment(linker, "/stack:256000")

using namespace std;

int main(){

    freopen("in.c","r",stdin);
    freopen("on.c","w",stdout);

    string s;
    int tc , n;
    cin >> tc;

    for(int nc = 1; nc <= tc; nc++){
        cin >> n >> s;

        int answer = 0 , tot = 0;
        for(int i = 0; i <= n; ++i){
            if(s[i] != '0' && tot < i){
                answer += i - tot;
                tot += i - tot;
            }
            tot += s[i] - '0';
        }


        printf("Case #%d: %d\n",nc,answer);
    }


	return 0;
}




