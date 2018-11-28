#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;

vector<string> num;
vector<int> num2;
void ini(){
    num.push_back("ZERO");
    num.push_back("ONE");
    num.push_back("TWO");
    num.push_back("THREE");
    num.push_back("FOUR");
    num.push_back("FIVE");
    num.push_back("SIX");
    num.push_back("SEVEN");
    num.push_back("EIGHT");
    num.push_back("NINE");
    num2.push_back(0);
    num2.push_back(2);
    num2.push_back(4);
    num2.push_back(6);
    num2.push_back(7);
    num2.push_back(1);
    num2.push_back(9);
    num2.push_back(5);
    num2.push_back(3);
    num2.push_back(8);

}

int main(){
    freopen("A-large.in","r", stdin);
    freopen("a.out", "w", stdout);

    ini();
    ios_base::sync_with_stdio(false);
    int tt;
    string s;
    vector<int> res;
    string l = "ZWUXSONVRH";
    cin >> tt;
    int let[27];
    for(int cc = 0; cc < tt; cc++){
        cout<<"Case #" << cc + 1 << ": ";
        res.clear();
        memset(let, 0, sizeof let);
        cin >> s;
        for(int i = 0; i < s.size(); i++)
            let[s[i] - 'A']+= 1;
        for(int j = 0; j < l.size(); j++){
            while(let[l[j]- 'A'] > 0){
                for(int i = 0; i < num[num2[j]].size(); i++){
                    let[num[num2[j]][i] - 'A']--;
                }
                res.push_back(num2[j]);
            }
        }
        sort(res.begin(), res.end());
        for(int i = 0; i < res.size(); i++){
            cout << res[i];
        }
        cout << endl;
    }

    return 0;
}
