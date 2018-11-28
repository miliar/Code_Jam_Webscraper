#include <iostream>
#include<string>
#include <vector>
#include<map>
#include<algorithm>
using namespace std;

void init(vector <string > &v, map<char, string> &m)
{
    v.resize(10);
    v[0] ="ZERO";
    v[1] ="TWO";
    v[2] = "FOUR";
    v[3] = "SIX";
    v[4] = "EIGHT";
    v[5] = "ONE";
    v[6] ="THREE";
    v[7]="FIVE";
    v[8]="SEVEN";
    v[9]="NINE";

    m['Z'] = "0";
    m['W'] = "2";
    m['U'] = "4";
    m['X'] = "6";
    m['G'] = "8";
    m['O'] = "1";
    m['R'] = "3";
    m['F'] = "5";
    m['V'] = "7";
    m['I'] = "9";

}

void prob1(){
    int T;
    cin >> T;
    string s;

    map<char,int > freq;
    vector < string> v;
    map <char, string> letNums;
    string order = "ZWUXGORFVI";

    string res;
    init(v, letNums);
    for (int c=1; c<=T; c++){

        cin >> s;
        cout << "Case #" << c << ": ";

        res = "";
        // count char freq
        int sz = s.size();
        for (int i=0; i<sz; i++){
            freq[s[i]]++;
        }

        int curFreq; char numberLetter;
        for (int i=0; i<10; i++){
            numberLetter = order[i];
            curFreq = freq[numberLetter];

            if (curFreq != 0){
                for (int j=0; j< v[i].size(); j++){
                    freq[v[i][j]] -= curFreq;
                }

                for (int j=0; j<curFreq; j++)
                    res+= letNums[numberLetter];
            }
        }

        sort(res.begin(), res.end());
        cout << res << endl;


    }
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    prob1();
    return 0;
}