#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int ans=0;

void trim(string &s)
{
    int i=s.size()-1;
    while(i>=0 && s[i]=='+') i--;
    s = s.substr(0, i+1);
}

void top(string &s)
{
    int i=0;
    while(i<s.size() && s[i]=='+') {
        s[i]='-';
        i++;
    }
    ans += (i!=0)?1:0;
}

void rotate(string &s)
{
    reverse(s.begin(), s.end());
    for(auto &c:s) {
        if(c=='-') c='+';
        else c='-';
    }
    ans++;
}


int main()
{
    int t;
    string in;
    cin>>t;
    for(int T=1;T<=t;T++) {
        cin>>in;
        ans = 0;
        trim(in);
        //cout<<in<<"\n";
        while(!in.empty()) {
            top(in);
            //cout<<"Loop: \n"<<ans<<" "<<in<<"\n";
            rotate(in);
            //cout<<ans<<" "<<in<<"\n";
            trim(in);
            //cout<<ans<<" "<<in<<"\n";
        }
        cout<<"Case #"<<T<<": "<<ans<<"\n";
    }
    return 0;
}
