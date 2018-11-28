#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<cstdio>
using namespace std;

int main(){
    int tc;
    cin>>tc;

    for(int caso=1;caso<=tc;caso++){
        int x;
        cin>>x;
        string s;
        cin>>s;
        for(int i=0;i<2000;i++){
            int val=i+(s[0]-'0');
            bool ok=1;
            for(int j=1;j<s.size();j++){
                if(val<j)ok=0;
                val+=(s[j]-'0');
            }
            if(ok){
                cout<<"Case #"<<caso<<": "<<i<<endl;
                break;
            }
        }
    }
    
    return 0;
}
