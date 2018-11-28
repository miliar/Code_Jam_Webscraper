#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    //freopen("d:\\A-large.in","r",stdin);
    //freopen("d:\\output.txt","w",stdout);
    int T,Smax;
    string s;
    cin>>T;
    for(int I=1;I<=T;I++){
        cin>>Smax>>s;
        int cur=0,cnt=0,len=s.size();
        for(int i=1;i<len;i++){
            cur+=s[i-1]-'0';
            if(cur<i){
                cnt+=i-cur;
                cur=i;
            }
        }
        cout<<"Case #"<<I<<": "<<cnt<<endl;
    }
}
