//
// Created by Harshit on 4/8/2017.
//

#include<bits/stdc++.h>
using namespace std;
string s;
int k;
void flip(int i){
    for(int j=i;j<i+k;j++){
        if(s[j]=='+') s[j]='-';
        else if(s[j]=='-') s[j]='+';
    }

}
int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif // ONLINE_JUDGE
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){

        cin>>s>>k;
        int coun=0;
        bool ok=false;
        for(int i=0;i<=s.size()-k;i++)
        {if(s[i]=='-')
            {   coun++;
                flip(i);}
        }
        cout<<"Case #"<<i<<": ";
        for(int i=s.size()-k+1;i<s.size();i++)
        {if(s[i]=='-') {cout<<"IMPOSSIBLE"<<endl;
                ok=true;
                break;
            }}
        if(ok) continue;
        cout<<coun<<endl;

    }

}
