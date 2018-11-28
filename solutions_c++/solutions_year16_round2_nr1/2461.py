#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }
int even(int n) { return !(n%2); }
int odd(int n) { return n%2; }

int main(){
    int t,i,j,k,l;
    int T,N;
    vector<string> spelled({"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"});

    cin >> T;
    F1(t,T){
        string S;
        cin >> S;
        vi ans,letterCount(26,0);

        F0(i,SZ(S)){
            char c = S[i];
            letterCount[(int)c-65]++;
        }

        while (letterCount['Z'-65]){
            F0(i,SZ(spelled[0])){
                letterCount[spelled[0][i]-65]--;
            }
            ans.push_back(0);
        }

        while (letterCount['X'-65]){
            F0(i,SZ(spelled[6])){
                letterCount[spelled[6][i]-65]--;
            }
            ans.push_back(6);
        }

        while (letterCount['W'-65]){
            F0(i,SZ(spelled[2])){
                letterCount[spelled[2][i]-65]--;
            }
            ans.push_back(2);
        }

        while (letterCount['U'-65]){
            F0(i,SZ(spelled[4])){
                letterCount[spelled[4][i]-65]--;
            }
            ans.push_back(4);
        }

        while (letterCount['G'-65]){
            F0(i,SZ(spelled[8])){
                letterCount[spelled[8][i]-65]--;
            }
            ans.push_back(8);
        }

        while (letterCount['H'-65]){
            F0(i,SZ(spelled[3])){
                letterCount[spelled[3][i]-65]--;
            }
            ans.push_back(3);
        }

        while (letterCount['S'-65]){
            F0(i,SZ(spelled[7])){
                letterCount[spelled[7][i]-65]--;
            }
            ans.push_back(7);
        }

        while (letterCount['V'-65]){
            F0(i,SZ(spelled[5])){
                letterCount[spelled[5][i]-65]--;
            }
            ans.push_back(5);
        }

        while (letterCount['O'-65]){
            F0(i,SZ(spelled[1])){
                letterCount[spelled[1][i]-65]--;
            }
            ans.push_back(1);
        }

        while (letterCount['E'-65]){
            F0(i,SZ(spelled[9])){
                letterCount[spelled[9][i]-65]--;
            }
            ans.push_back(9);
        }

        sort(begin(ans),end(ans));



        cout << "Case #" << t << ": ";
        F0(i,SZ(ans)){
            cout << ans[i];
        }
        cout << endl;

    }
    return 0;
}
