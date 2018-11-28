#include <bits/stdc++.h>

using namespace std;

string to_string(int a){

    stringstream ss;
    ss << a;
    return ss.str();

}

int main() {

    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);

    int t, a;
    string num;
    cin >> t;

    map<char, bool> digit;
    for(int ti = 1; ti <= t; ti++){
        digit.clear();
        cin >> a;
        int valid = 0;

        if(a == 0){
            valid = -1;
        }

        for(int i = 1; valid == 0 ; i++){

            num = to_string(a*i);

            for(int j = 0; j < num.size(); j++){
                digit[num[j]] = 1;
            }

            if(digit.size() == 10){
                valid = 1;
                break;
            }

        }



        cout <<"Case #"<< ti <<": ";

        if(valid == -1) cout << "INSOMNIA\n";
        else cout << num<<"\n";
    }

    return 0;
}

