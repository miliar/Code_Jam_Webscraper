#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace::std;

ofstream fout("wunnnn2.txt");
string s;
vector <long long int> divis;
long long int heron(string s, int base){
long long int w=0;
if(s[0]=='1') w=1;

    for(int i = 1; i<s.size(); i++){
        if(s[i]=='1'){
            w=w*base+1;
        }else{
            w=w*base;
        }
    }
return w;
}

string convert(int num){
    string ret,ret2;
    while(num>0){
        int t=num%2;
        ret+=char(t+'0');
        num/=2;
    }
    for(int i=ret.size()-1; i>=0; i--){
        ret2+=ret[i];
    }
return ret2;
}

bool isPrime(long long int liczba){
    for(long long  int i=2; i<=sqrt(liczba); i++){
        if(liczba%i==0) { divis.push_back(i);  return false; }
    }
return true;
}


int main(){
int t1,t2,t3;
cin>>t1>>t2>>t3;
int licznik=0;
cout<<"Case #1:"<<endl;
for(int i=32769; i<=65535; i++){
    divis.clear();
    string x=convert(i);
    if(x[15]=='0') continue;
    for(int b=2; b<=10; b++){
       long long int inn=heron(x,b);
        if(isPrime(inn)==true) break;
        if(b==10)   {cout<<x; for(int i=0; i<divis.size(); i++) cout<<" "<<divis[i]; cout<<endl; licznik++;}
    }
if(licznik==t3) break;
}


return 0;
}
//32769
//65535
