#include<bits/stdc++.h>

using namespace std;

int main(){
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("AOUT.txt", "w", stdout);

    int T;
    cin>>T;
    for(int line = 1; line <= T; line++){
        int fr;
        cin>>fr;
        map<int, bool> mp;
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                int num;
                cin>>num;
                if(i == fr) mp[num] = true;
            }
        }

        int sr, cnt = 0, ans;
        cin>>sr;
        for(int i=1; i<=4; i++){
            for(int j=1; j<=4; j++){
                int num;
                cin>>num;
                if(i == sr)
                    if(mp[num] == true){
                        cnt++;
                        ans = num;
                    }
            }
        }
        printf("Case #%d: ", line);
        if(cnt == 1)printf("%d\n", ans);
        else if(cnt == 0) puts("Volunteer cheated!");
        else if(cnt > 1) puts("Bad magician!");
    }
    return 0;
}
