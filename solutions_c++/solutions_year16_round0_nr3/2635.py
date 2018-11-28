#include <iostream>
#include <bits/stdc++.h>
#include <bitset>
using namespace std;
vector<string> v;
typedef unsigned long long ull;
ull _sieve_size;

bitset<10000010> bs;
vector<ull> primes;
map<string,vector<ull> > ma;
void sieve(ull upTo) {
_sieve_size = upTo + 1llu;
bs.set();
bs[0] = bs[1] = 0llu;
for (ull i = 2llu; i <= ((int)sqrt( _sieve_size )) + 1llu; i++)
if (bs[i]) {
for (ull j = i * i; j <= _sieve_size; j += i)
bs[j] = 0;
primes.push_back(i);
}
}
bool isPrime(ull N) {
if (N <= _sieve_size) return bs[N];
for (auto p : primes)
if (N % p == 0) return false;
return true;
}


ull convert(string n,ull b){
ull f=0;
ull a=1;
for(int i=n.size()-1;i>=0;i--){
if(n[i]=='1') {
f+=a;
}
a*=b;
}
return f;

}


bool verif(string s){
int n=s.size();
if(s[0]=='1' && s[n-1]=='1') return true;
else return false;
}

bool check(string s){
bool besa=true;
for(int i=2;i<11;i++){
ull a=convert(s,i);
if(isPrime(a)) {besa=false;
break;
}
}

return besa;



}
void genera(string s){

    if(s.length() <=16)  {
   if(verif(s) && check(s) && s.size()==16) v.push_back(s);
    genera(s + "0") ;
    genera(s+ "1");
    }
}
ull deviseur(ull a){
for(ull i=2;i<=a/2;i++){
if(a%i==0) return i;
}
return a;

}
void findu(string s){
ull a;
for(int i=2;i<11;i++){
 a=convert(s,i);
//ma[s].push_back(a);
ma[s].push_back(deviseur(a));
}
}


int main()
{
   ofstream cout ("br0");
    string s="";
    sieve(10000000);
    genera(s);
    //cout<<v.size()<<endl;

   for(int i=0;i<50;i++){
   // cout<<v[i]<<" ";
      findu(v[i]);
   // cout<<endl;
    }
    cout<<"Case #1:"<<endl;
    for(map<string,vector<ull> >::iterator it=ma.begin();it!=ma.end();it++){
    cout<<it->first<<" "<<it->second[0]<<" "<<it->second[1]<<" "<<it->second[2]<<" "<<it->second[3]<<" "<<it->second[4]<<" "<<it->second[5]<<" "<<it->second[6]<<" "<<it->second[7]<<" "<<it->second[8]<<endl;
    }
    return 0;
}
