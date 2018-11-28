#include<iostream>
#include<string>
using namespace std;

int main(){
freopen("jam2in.txt","r",stdin);
freopen("jam2out.txt","w",stdout);
    int t;
    cin>>t;
    for(int z=0;z<t;z++){
        string s;
        cin>>s;
        string s1=" ";
        s1[0]=s[0];
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1]){
                s1+=s[i];
            }
        }

        int ans=s1.size();
        if(s1[s1.size()-1]=='+'){
            ans--;
        }
        cout<<"Case #"<<z+1<<": "<<ans<<endl;
    }
}
