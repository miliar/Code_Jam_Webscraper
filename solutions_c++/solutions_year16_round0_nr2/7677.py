#include <bits/stdc++.h>
using namespace std ;
main ()
{
  freopen("out1.txt","w",stdout);
    freopen("in1.txt","r",stdin);
long long t;
cin>>t;
for(int i=0 ; i <  t ; i++){
        long ans=0;
string s;
cin>>s;
char c='-';
for(int j =s.length()-1 ; j>=0 ; j--){
if( s[j] == c){
    ans++;
if(c=='-')c='+';
else{     c='-';}
}
}
cout<<"Case #"<<i+1<<": "<<ans<<endl;
}

 }
