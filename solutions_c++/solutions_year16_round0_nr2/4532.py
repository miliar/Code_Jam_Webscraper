#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
int analyze(string& s)
{
    int cnt=0;
    for(int i=0;i<s.size();i++){
        if(i==s.size()-1){
            if(s[i]=='-'){
                ++cnt;
            }
        }
        else{
            if(s[i]!=s[i+1]){
                for(int j=0;j<=i;j++){
                    if(s[i]=='-')
                        s[i]='+';
                    else
                        s[i]='-';
                }
                ++cnt;
            }
        }
    }
    return cnt;
}
int main()
{
    freopen("data.out","w",stdout);
    int T;
    string s;
    cin>>T;
    for(int kase=1;kase<=T;kase++){
        cin>>s;
        cout<<"Case #"<<kase<<": "<<analyze(s)<<endl;
    }

    return 0;
}
