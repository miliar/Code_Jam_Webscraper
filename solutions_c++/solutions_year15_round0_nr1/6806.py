#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long int int64;
typedef unsigned long long int64u;

int main(){
    std::ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for(int j = 1; j <= T; j++){
        int a;
        string s;
        cin >> a >> s;
        int count = 0;
        int running_sum = 0;
        for(int i = 0; i < a+1; i++){
            if(i>running_sum){
                count++;
                running_sum++;
            }
            running_sum+=(s[i]-'0');
            //cout << running_sum << endl;
        }
        cout << "Case #"<< j << ": " << count << endl;
    }
    return 0;
}