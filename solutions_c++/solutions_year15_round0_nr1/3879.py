#include<bits/stdc++.h>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int s;
        cin >> s;
        string aud;
        cin >> aud;

        map<int, int> people;
        int num = 0, stand = 0;
        for(int i = 0; i < aud.size(); i++){
            int cnt = aud[i] - '0';
            people[i] += cnt;
            num += cnt;
        }

        int need = 0;
        while(stand < num){
            for (auto iter = people.begin(); iter != people.end(); ){
                if(iter->first <= stand){
                    stand += iter->second;
                    iter = people.erase(iter);
                }
                else{
                    int cur = iter->first - stand;
                    stand = iter->first;
                    num += cur;
                    need += cur;
                    break;
                }
            }
        }
        printf("Case #%d: %d\n", t, need);
    }
    return 0;
}


