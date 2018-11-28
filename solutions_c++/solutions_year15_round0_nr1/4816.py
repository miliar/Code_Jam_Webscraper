#include <bits/stdc++.h>

using namespace std;

int main(){
    //freopen("input.txt","r",stdin);
    //freopen("Standing Ovation small.txt","w",stdout);

    int tc, ct = 0;
    cin>>tc;
    while(tc--){
        cout<<"Case #"<<++ct<<": ";
        int n, standing = 0, add = 0;
        cin>>n;
        string s;
        cin>>s;
        int len = s.size();
        standing = int(s[0] - '0');
        for(int i=1;i<len;++i){
            if(standing + add < i)
                add++;
            standing = standing + int(s[i] - '0');
        }

        cout<<add<<endl;
    }
}
