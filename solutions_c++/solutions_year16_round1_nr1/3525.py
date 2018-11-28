#include<bits/stdc++.h>

using namespace std;
int T;
string line;
char mn;
int cc=1;


string solve(string str){
    string ans=""; ans+=mn;
    string aux="";
    for(int i=1;i<str.length();i++){
        if(line[i]<ans[0]) ans+=line[i];
        else{
            mn=line[i];
            aux=""; aux+=mn;
            aux+=ans;
            ans=aux;
        }
    }
    return ans;
}


int main(){

    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>line;
        mn=line[0];
        printf("Case #%d: %s\n",cc++,solve(line).c_str());
    }


    return 0;
}
