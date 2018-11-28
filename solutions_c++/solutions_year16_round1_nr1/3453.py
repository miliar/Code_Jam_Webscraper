#include<bits/stdc++.h>
using namespace std;
string s;

int main(){
  ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 freopen("A-large.in","r",stdin);

 freopen("A-salida.out","w",stdout);
int tc;
cin>>tc;
for(int ttt=1;ttt<=tc;ttt++){

    list<char> chars;
    cin>>s;
    list<char>::iterator it = chars.begin();
    for(int i=0;i<s.size();++i){
        it=chars.begin();
        if(i==0)chars.insert(it,s[i]);
        else{
            if(s[i] < *it)
            {
                it=chars.end();
            }
            chars.insert(it,s[i]);
        }
    }
    cout<<"Case #"<<ttt<<": ";
    for(it=chars.begin();it!=chars.end();it++){
        cout<<*it;
    }
    cout<<endl;
}

return 0;
}
