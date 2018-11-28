#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)

int main() {
    string str;
    int T;
    cin >> T;
    string s1 = "ZWUXG";
    string s2 = "OTFSN";
    
    for1(tc, T) {
        cout << "Case #" << tc << ": ";
           cin >> str;

            int a[26];
            vector<int> num;
            for(int i =0;i<26;i++)
                a[i]=0;
           for(int i = 0; i<str.length();i++){
                a[str[i]-'A']++;
            }
            while(1){
                string rem;
                if(a['Z'-'A'] >= 1){
                    rem = "ZERO";
                    num.push_back(0);
                }
                else if(a['W'-'A'] >= 1){
                    rem = "TWO";
                    num.push_back(2);
                }
                else if(a['U'-'A'] >= 1){
                    rem = "FOUR";
                    num.push_back(4);
                }
                else if(a['X'-'A'] >= 1){
                    rem = "SIX";
                    num.push_back(6);
                }
                else if(a['G'-'A'] >= 1){
                    rem = "EIGHT";
                    num.push_back(8);
                }
                else 
                    break;
                for(int j = 0; j<rem.length();j++)
                {
                    a[rem[j]-'A']--;
                }
            }
            while(1){
                string rem;
                if(a['O'-'A'] >= 1){
                    rem = "ONE";
                    num.push_back(1);
                }
                else if(a['T'-'A'] >= 1){
                    rem = "TWO";
                    num.push_back(3);
                }
                else if(a['F'-'A'] >= 1){
                    rem = "FIVE";
                    num.push_back(5);
                }
                else if(a['S'-'A'] >= 1){
                    rem = "SEVEN";
                    num.push_back(7);
                }
                else if(a['N'-'A'] >= 1){
                    rem = "NINE";
                    num.push_back(9);
                }
                else 
                    break;
                for(int j = 0; j<rem.length();j++)
                {
                    a[rem[j]-'A']--;
                }
            }

            sort(num.begin(),num.end());

            for(int j=0;j<num.size();j++){
                cout << num[j];
            }
            cout << endl;
    }
    }

