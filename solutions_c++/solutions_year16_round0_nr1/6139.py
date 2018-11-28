#include<bits/stdc++.h>
using namespace std;
long long n,aux;

string tostring( long long a){
stringstream aa;
aa<<a;
return aa.str();
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-asdf.out","w",stdout);
int t;
cin>>t;
for(int cc=1;cc<=t;++cc){
    vector<bool> digito(10,0);
    cin>>n;
    int s=1;
    if(n==0){cout<<"Case #"<<cc<<": "<<"INSOMNIA"<<endl;continue;}
    while(count(digito.begin(),digito.end(),true)!=10){
        aux=n*s;
        //cout<<aux<<endl;
        s++;
        string p=tostring(aux);
        for(char c:p){
         //   cout<<c;
        digito[c-'0']=1;
        }
        //cout<<endl;
        //system("pause");
    }
    cout<<"Case #"<<cc<<": "<<aux<<endl;
}

return 0;
}
