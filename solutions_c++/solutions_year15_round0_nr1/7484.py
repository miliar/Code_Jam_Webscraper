#include <bits/stdc++.h>
using namespace std;
typedef long long int lli;

int main(){
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    lli t,smax,aud,frd;string s;
    cin>>t;
    //file>>t;
    for(lli j=1;j<=t;j++){
        cin>>smax>>s;
        //file>>smax;file>>s;
        aud=frd=0;
        aud+=(s[0]-'0');
        for(lli i=1;i<=smax;i++){
            //cout<<aud<<" "<<frd<<endl;
            if(aud>=i || (s[i]-'0')==0){
                aud+=(s[i]-'0');
                continue;
            }else{
                frd+=i-aud;
                aud+=((s[i]-'0')+i-aud);
            }
        }
        cout<<"Case #"<<j<<": "<<frd<<endl;
    }
    //file.close();
return 0;
}
