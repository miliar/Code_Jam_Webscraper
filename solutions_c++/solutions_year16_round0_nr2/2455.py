#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<cstdio>


using namespace std;

int T;

long long n;
string s;

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    cin>>T;
    for(int C=0;C<T;C++) {
        cin>>s;
        int ans=0;
        for(int i=0;i<s.length()-1;i++) {
            if(s[i]!=s[i+1]) ans++;
        }
        if(s[s.length()-1]=='-') ans++;
        cout<<"Case #"<<C+1<<": "<<ans<<endl;
    }
}
