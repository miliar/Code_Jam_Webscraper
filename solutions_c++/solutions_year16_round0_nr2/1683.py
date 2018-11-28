#include<bits/stdc++.h>

using namespace std;

int main() {

    freopen("C:\\Users\\Saurabh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh\\Desktop\\out.txt","w",stdout);

    int t,cas=1;
    cin>>t;
    while(t--) {
        int i;
        string s;
        cin>>s;
        vector <int> v;
        int c=1;
        for(i=1;i<s.size();i++) {
            if(s[i]==s[i-1])
                c++;
            else
                v.push_back(c),c=1;
        }
        v.push_back(c);
        cout<<"Case #"<<cas++<<": ";
        if(s[s.size()-1]=='-')
            cout<<v.size()<<endl;
        else
            cout<<v.size()-1<<endl;
    }

    return 0;
}
