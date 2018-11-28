#include <bits/stdc++.h>

using namespace std;

map<string, int> m;

string reverse(string s){
    int len = s.size();
    for(int i = 0; i < len/2; ++i){
        swap(s[i], s[len - 1 - i]);
    }
    string sss = "";
    for(int i = 0; i < len; ++i)
        if(s[i] == '-')
            sss += "+";
        else
            sss += "-";
    return sss;
}

int rec(string sss){
    if(m.find(sss) != m.end())
        return m[sss];
    //cout<<sss<<endl;
    string s, recon;

    int len = sss.size();

    for(int i = 0; i < len; ++i){
        s = reverse(sss.substr(0, i + 1)) + sss.substr(i + 1, len - (i + 1));

        if(s[0] == '-')
            recon = "-";
        else
            recon = "+";
        len = s.size();
        for(int i = 1; i < len; ++i){
            if(s[i] != s[i - 1]){
                if(s[i] == '-')
                    recon += "-";
                else
                    recon += "+";
            }
        }
        if(m.find(sss) != m.end())
            m[sss] = min(m[sss], 1 + rec(recon));
        else
            m[sss] = 1 + rec(recon);
    }
    return m[sss];
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    m["+"] = 0;
    int t, len;
    cin>>t;
    string s, recon;
    for(int i = 1; i <= t; ++i){
        cin>>s;
        if(s[0] == '-')
            recon = "-";
        else
            recon = "+";
        len = s.size();
        for(int i = 1; i < len; ++i){
            if(s[i] != s[i - 1]){
                if(s[i] == '-')
                    recon += "-";
                else
                    recon += "+";
            }
        }

        cout<<"Case #"<<i<<": "<<rec(recon)<<endl;
    }


    return 0;
}
