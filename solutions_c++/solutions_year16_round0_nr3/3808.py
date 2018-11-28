#include<bits/stdc++.h>
using namespace std;
vector <long long> v;
void sieve(){
    v.push_back(2);
for(int i=3;i<70000;++i){
        bool pr=true;
        long long sq=sqrt(i)+1;
    for(int j=0;j<v.size()&&v[j]<=sq;++j){
        if(i%v[j]==0){
            pr=false;
            break;
        }
    }
    if(pr){
        v.push_back(i);
    }
}
}
bool isPrime(vector<int> &k,long long b){
long long sq=sqrt(b)+1;
for(int i=0;i<v.size()&&v[i]<=sq;++i){
    if(b%v[i]==0){
        k.push_back(v[i]);
        return false;
    }
}
return true;
}

long long toBase(string s,int c){
long long num=0;
for(int i=0;i<s.length();++i){
    num=num*c+int(s[i]-48);
}
return num;
}
bool isjamcoin(vector<int> &k,string s){
    bool jc=true;
   for(int i=2;i<=10;++i){
    long long x=toBase(s,i);
    if(isPrime(k,x)){
        jc=false;
        break;
    }
   }
   return jc;
}
string numtobin(long long x){
string s="";
while(x>0){
    s=char((x%2)+48)+s;
    x=x/2;
}
return s;
}
string nextS(string s){
int top=s.length()-2;
while(s[top]=='1'){
    s[top]='0';
    --top;
}
s[top]='1';
return s;
}
void do_it(){
int n,j;
cin>>n>>j;
long long start=pow(2,n-1)+1;
string x=numtobin(start);
while(j>0){
        vector <int> k;
    if(isjamcoin(k,x)){
        cout<<x<<" ";
       for(int i=0;i<k.size();++i){
        cout<<k[i]<<" ";
       }
         cout<<endl;
        x=nextS(x);
    }else{
    x=nextS(x);
    continue;
    }
    --j;
}
}
int main(){
    sieve();
    int t;
    cin>>t;
    int m=1;
    while(t>0){
    cout<<"Case #"<<m<<":"<<endl;
    do_it();
    --t;
    ++m;
    }
return 0;
}
