#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        string s;
        cin>>s;
        int n=s.size();
        list<char> lis;
        lis.push_back(s[0]);
        for(int i=1;i<n;i++){
            char c=lis.front();
            if(s[i]<c){
                lis.push_back(s[i]);
            }
            else{
                lis.push_front(s[i]);
            }
        }
        for(list<char>::iterator i=lis.begin();i!=lis.end();i++){
            cout<<(*i);
        }
        cout<<endl;
    }
}
