#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
#define rep(a,b) for(int a = 0; a < (int)b; a++)
int letters['z' - 'a' + 5];
int ans[10];
void solve(int indexToSolve, char importantLetter, string otherLetters){
    ans[indexToSolve] = letters[importantLetter - 'A'];
    rep(i, otherLetters.size()){
        letters[otherLetters[i] - 'A'] -= ans[indexToSolve];
    }
}
int main(){
//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);
    int T;
    string s;
    cin>>T;
    rep(t, T){
        rep(i, 'z' - 'a' + 5){
            letters[i] = 0;
        }
        rep(i, 10){
            ans[i] = 0;
        }
        cout<<"Case #"<<t+1<<": ";
        cin>>s;
        rep(i, s.size()){
//            cout<<i<<" "<<s[i] - 'A';
            letters[s[i] - 'A']++;
        }
//        cout<<endl;
        rep(i, 'z' - 'a' + 1){
//            cout<<letters[i]<<" ";
        }
//        cout<<endl;
        solve(0, 'Z', "ZERO");
        solve(2, 'W', "TWO");
        solve(6, 'X', "SIX");
        solve(8, 'G', "EIGHT");
        solve(3, 'H', "THREE");
        solve(7, 'S', "SEVEN");
        solve(4, 'R', "FOUR");
        solve(5, 'V', "FIVE");
        ans[1] = letters['O' - 'A'];
        ans[9] = letters['I' - 'A'];

        rep(i, 10){
            rep(j, ans[i]){
                cout<<i;
            }
        }
        cout<<endl;
    }
}
