#include <bits/stdc++.h>
#define mp make_pair
#define f first
#define s second

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int e=0;
    while(t--){
        e++;
        int ans=1;
        string s;
        cin>>s;
        char c=s[0];
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1]){
               c=s[i];
               ans++;
            }
        }
        if(c=='+'){ans--;}
        cout<<"Case #"<<e<<": "<<ans<<endl;
    }

    return 0;
}
