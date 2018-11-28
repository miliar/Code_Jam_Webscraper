#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<ctime>
#include<vector>
#include<string>
#include<set>

using namespace std;


int fun(string s){

    int c=0;
    for(int i=1;i<s.length();i++){
        if(s[i-1]!=s[i])
            c++;
    }
    if (s[s.length()-1]=='-')
        c++;
    return c;

}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);


    string s;
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>s;
        int r=fun(s);

        cout<<"Case #"<<i<<": "<<r<<endl;
    }
    return 0;
}