#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int preProcess(string& in,string& out){
    out.push_back(in[0]);
    for(int i = 1;i<in.size();i++){
        if(in[i] != in[i-1])
            out.push_back(in[i]);
    }
    return 0;
}

int solve(string ss){
    string s;
    preProcess(ss,s);
    const int sLen = s.size();
    int dp[sLen+1];
    dp[0] = 0;
    for(int i = 1;i<=sLen;i++){
        if(s[i-1] == '+')
            dp[i] = dp[i-1];
        else{
            if(i==1)
                dp[i] = dp[i-1] + 1;
            else
                dp[i] = dp[i-1] + 2;
        }
    }
    return dp[sLen];
}

int solve2(string s) {
    char a1 = '-';
    bool find = true;
    int cnt = 0;
    for(int i=0; i<s.size(); i++) {
        if(s[i]=='-'&&find) { cnt++; find = false;}
        else if(s[i]=='+') find = true;
    }
    if(cnt==0 ) {
        if(s[0] == '+') return 0;
        else return 1;
    } else {
        if(s[0] == '+') return 2*cnt;
        else return 2*cnt-1;
    }

}

int main()
{
    ifstream in("B-large.in");
    ofstream out("out_large.txt");
    if (! in.is_open()){
        cout << "Error opening file";
    }
    int t;
    string s;
    in>>t;
    //vector<int> result;
    int lineCount = 1;
    while(t--){
        in>>s;
        out<<"Case #"<<lineCount<<": "<<solve(s)<<endl;
        lineCount ++;
    }
    //for(auto ele:result)
    //    out<<ele<<endl;
    in.close();
    out.close();
    return 0;
}
