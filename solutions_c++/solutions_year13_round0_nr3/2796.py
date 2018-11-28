#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;
typedef long long ll;
int isPal(ll num){
    char buf[101];
    sprintf(buf,"%d",num);
    for(int i=0, j=strlen(buf);i<strlen(buf)/2;i++)
    {
    if(buf[i] != buf[j-i-1])
    {
                         return false;
    }
}
return true;
}
int main(){
    int t=0,cas=1;
    cin>>t;
    while(t--){
        int cnt=0;
        ll st,ed;
        cin>>st>>ed;
        st=(ll)ceil(sqrt(st*1.0));
        ed=(ll)(sqrt(ed));
        for(ll i=st;i<=ed;i++ ){
            if(isPal(i) && isPal(i*i))
            {
                //cout<<i*i<<endl;
                cnt++;
            }
        }
        cout<<"Case #"<<cas++<<": "<<cnt<<endl;
    }
    return 0;
}
