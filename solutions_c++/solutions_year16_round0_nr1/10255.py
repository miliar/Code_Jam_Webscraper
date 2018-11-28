#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
string k;
long long int a,n,c=1,r,h;
set<char> dig;
cin>>a;
for(int i=0; i<a; i++){
cin>>n;
if(n==0){cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        continue;}
while(dig.size()!=10){
r=n*c;
k = to_string(r);
for(int q=0;q<k.size();q++) if(dig.find(k[q])==dig.end()) dig.insert(k[q]);
c++;
}
dig.clear();
cout<<"Case #"<<i+1<<": "<<r<<endl;
c=1;
}
return 0; }
