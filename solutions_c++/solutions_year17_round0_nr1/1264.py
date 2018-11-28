/* Author : Jordhy Fernando */
#include<bits/stdc++.h>
#define ll long long
#define For(i,j,n) for(int i = j; i < n; i++)
#define EPS 1e-12

using namespace std;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

int main(){
	int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        int ans = 0;
        string s;
        int k;
        cin >> s >> k;
        for(int j = 0; j < s.length() - (k - 1); j++){
            if(s[j] == '-'){
                ans++;
                for(int l = 0; l < k; l++){
                    if(s[j + l] == '-'){
                        s[j + l] = '+';
                    }
                    else{
                        s[j + l] = '-';
                    }
                }
            }
        }
        int j = s.length() - 1;
        while(j >= 0 && s[j] == '+'){
            j--;
        }
        cout << "Case #" << i << ": ";
        if(j >= 0){
            cout << "IMPOSSIBLE" << endl;
        }
        else{
            cout << ans << endl;
        }
    }
	return 0;
}
