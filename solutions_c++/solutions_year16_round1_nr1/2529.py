#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

#define pb push_back
#define pf push_front
#define mp make_pair
#define sz(a) (int)a.size()
#define i128 __int128
#define INF 0x3f3f3f3f
// LLONG_MIN LLONG_MaX INT_MIN INT_MaX



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n;
    cin >> n;
    for(int TC=1; TC<=n; TC++){
        string s;
        cin >> s;
        string temp;
        for(int i=0; i<s.length(); i++){
            if(i){

                if(s[i] >= temp[0]){
                    temp = s.substr(i,1) + temp;
                }
                else{
                    temp = temp + s.substr(i,1);
                }
            }
            else{
                temp += s.substr(i,1);
            }
        }
        cout << "Case #" << TC << ": " << temp << endl;
    }
    return 0;
}