#include<bits/stdc++.h>
using namespace std;

string s;

int main()
{
    ifstream in ("B-large.in");
    ofstream out ("largepancake.txt");

    int t;
    in>>t;
    getline(in, s);

    for(int ts=1;ts<=t;ts++){
        getline(in, s);
        int n = s.length();

        while(n>0 && s[n-1]=='+')
            n--;

        if(n==0){
            out<<"Case #"<<ts<<": "<<0<<endl;
            continue;
        }

        int ans = 1;
        for(int i=0;i<n-1;i++){
            if(s[i]!=s[i+1])
                ans++;
        }

        out<<"Case #"<<ts<<": "<<ans<<endl;
    }

    return 0;
}
