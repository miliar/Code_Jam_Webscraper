#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<sstream>
#include<set>
#include<vector>
#include<map>
#include<cassert>
#include<queue>
using namespace std;

int main(){

   // freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    
    int tc;cin>>tc;
    for(int caso=1;caso<=tc;caso++){
        string s;
        cin>>s;
        cout<<"Case #"<<caso<<": ";
        
        int dev=1;
        for(int i=1;i<s.size();i++){
            if(s[i]!=s[i-1])
                dev++;
        }
        
        if(s[s.size()-1]=='+')
            dev--;
        
        cout<<dev<<endl;
    }

    return 0;
}





