#include<bits/stdc++.h>
#define mp(x,y) make_pair(x,y)
#define pii pair<int,int>
#define pb push_back


using namespace std;

typedef long long ll;

int letter[30], tmp;

void remove(char l){
    int idx = l - 'A';
    letter[idx] --;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    freopen("digits.in", "r",stdin);
    freopen("digits.out", "w",stdout);

    int t;
    cin >> t;

    string s;

    for(int tc = 1; tc <= t; tc ++){
        memset(letter, 0, sizeof(letter));
        vector<int> ans;
        cin >> s;
        int n = s.size();

        for(int i = 0; i < n; i ++){
            letter[s[i] - 'A'] ++;
        }
        //zero
        tmp = letter['Z' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(0);
            remove('Z');
            remove('E');
            remove('R');
            remove('O');
        }

        //two
        tmp = letter['W' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(2);
            remove('T');
            remove('W');
            remove('O');
        }

        //four
        tmp = letter['U' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(4);
            remove('F');
            remove('O');
            remove('U');
            remove('R');
        }

        //SIX
        tmp = letter['X' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(6);
            remove('S');
            remove('I');
            remove('X');
        }

        //EIGHT
        tmp = letter['G' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(8);
            remove('E');
            remove('I');
            remove('G');
            remove('H');
            remove('T');
        }

        //FIVE
        tmp = letter['F' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(5);
            remove('F');
            remove('I');
            remove('V');
            remove('E');
        }

        //SEVEN
        tmp = letter['V' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(7);
            remove('S');
            remove('E');
            remove('V');
            remove('E');
            remove('N');
        }

        //ONE
        tmp = letter['O' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(1);
            remove('O');
            remove('N');
            remove('E');
        }

        //THREE
        tmp = letter['T' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(3);
            remove('T');
            remove('H');
            remove('R');
            remove('E');
            remove('E');
        }

        //NINE
        tmp = letter['E' - 'A'];
        for(int i = 0; i < tmp; i ++){
            ans.pb(9);
            remove('N');
            remove('I');
            remove('N');
            remove('E');
        }

        sort(ans.begin(), ans.end());

        cout << "Case #" << tc << ": ";

        for(int i = 0; i < ans.size(); i ++)
            cout << ans[i];
        cout << "\n";
    }
    return 0;
}
