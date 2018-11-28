#include<iostream>
#include<string>
#include<vector>
#include<utility>
using namespace std;

typedef pair<char,int> pt;

vector<pt> parse(string s){
    vector<pt> res;

    char last='@';
    int n=1;
    int i=0;
    s += '@';

    while(i<s.size()){
        if(last == s[i]){
            n++;
        }
        else if(last != '@'){
            res.push_back(pt(last,n));
            n=1;
        }
        last = s[i];
        i++;
    }
    return res;
}

string pt2string(const vector<pt>& v){
    string res;
    for(const auto& p : v){
        res += p.first;
    }
    return res;
}

int solve(string s1,string s2){
    int res=0;
    auto v1 = parse(s1);
    auto v2 = parse(s2);

    // auto ss1 = pt2string(v1);
    // auto ss2 = pt2string(v2);
    // cout << ss1 << ' ' << ss2 << endl;

    if(pt2string(v1) != pt2string(v2)){
        return -1;
    }

    for(int i=0;i<v1.size();i++){
        res += std::abs(v1[i].second - v2[i].second);
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N;
        cin >> N;
        string s1,s2;

        cin >> s1 >> s2;

        int res = solve(s1,s2);
        if(res >= 0){
            cout << "Case #" << t << ": " << res << endl;
        }
        else{
            cout << "Case #" << t << ": Fegla Won" << endl;
        }
    }

    return 0;
}
