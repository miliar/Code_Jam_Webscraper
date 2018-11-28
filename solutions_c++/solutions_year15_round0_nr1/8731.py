#include<fstream>
#include<string>

using namespace std;

ifstream cin("A-large.in");
ofstream cout("A-large.out");

string s;

int main(){
    int i,j,k,t,n,d;

    cin>>t;
    for(j=1; j<=t; ++j){
        cin>>n>>s;

        k=0; d=0;
        for(i=0; i<=n; ++i){
            if(d<i){
                k+=i-d;
                d+=i-d;
            }

            d+=int(s[i]-'0');
        }

        cout<<"Case #"<<j<<": "<<k<<'\n';
    }


return 0;
}
