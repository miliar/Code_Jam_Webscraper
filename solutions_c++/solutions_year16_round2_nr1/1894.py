#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007;
const int INF = 1<<29;
const double EPS = 1e-8;
typedef vector<int> vec;
typedef pair<int,int> P;
typedef long long ll;

int change(map<char, int>& count, string str, char p){
    int n = count[p];
    for(int i=0;i<str.size();i++){
        count[str[i]] -= n;
    }
    return n;
}

int main(){
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        string S;
        cin >> S;
        map<char, int> count;
        for(int i=0;i<S.size();i++){
            count[S[i]]++;
        }
        vec ans(10, 0);
        ans[0] = change(count, "ZERO", 'Z');
        ans[2] = change(count, "TWO", 'W');
        ans[6] = change(count, "SIX", 'X');
        ans[8] = change(count, "EIGHT", 'G');

        ans[3] = change(count, "THREE", 'T');
        ans[4] = change(count, "FOUR", 'U');
        ans[5] = change(count, "FIVE", 'F');
        ans[7] = change(count, "SEVEN", 'V');
        ans[9] = change(count, "NINE", 'I');
        ans[1] = change(count, "ONE", 'O');

        printf("Case #%d: ", t+1);
        for(int i=0;i<10;i++){
            for(int j=0;j<ans[i];j++){
                printf("%d", i);
            }
        }
        printf("\n");
    }
    return 0;
}