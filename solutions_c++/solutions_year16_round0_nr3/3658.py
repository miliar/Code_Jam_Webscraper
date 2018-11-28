#include<iostream>
#include<algorithm>
#include<set>
#include<string>
#include<cmath>
#include<map>
#include<vector>
#define PB push_back
#define REP(i,n) for(int i=0;i<n;++i)
#define LL long long
using namespace std;

vector<LL> getPrimes(){
           vector<LL> ret;
           ret.PB(2);
           LL f = (LL)(pow((double)10,8));
           vector<bool> tmp(f,true);
           
           for(int i=3;i*i<=tmp.size();i+=2)
           { 
              if(tmp[i]==false) continue;
             for(int j= i*i;j<tmp.size();j+=i)
              tmp[j] = false;
           }
           
           for(int i=3;i<tmp.size();i+=2) if(tmp[i]) ret.PB(i);
           
           return ret;
           }
           
LL isPrime(string d,int idx){
   
   LL x = 0;
   LL p = 1;
   for(int i=d.size()-1;i>=0;--i)
   {
     x+=(d[i]-'0')*p;
     p*=(LL)idx;
   } 
   
  // cout<<x<<endl;
              
  if(x==1||x%2==0) return -1;
  
  for(LL i=3;i*i<=x;i+=2) 
   if(x%i==0) return i;
  
  return -1;
}

string convertTo2(LL x)
{
       string ret="";
       LL pr = 1;
       while(pr<=x) pr*=2;
       if(pr>x) pr/=2;
       
       while(pr>0) 
       {
         if(pr<=x) {ret+="1"; x-=pr;}
         else ret+="0";
         pr/=2;
       }
       
       return ret;
}

void solve(int n,int j){
     
 //  vector<LL> p = getPrimes();
 
   LL a = (LL)pow(double(2),15)+(LL)1;
   LL b = (LL)pow(double(2),16);
   
   map<string,vector<int> > d;
   for(LL i=a;i<=b;i+=2) 
   { vector<int> tmp;
     d[convertTo2(i)] = tmp;}
     int upr = 10;
   for(int idx = 2;idx<=upr;++idx)
    for( map<string,vector<int> >::iterator it = d.begin(); it!=d.end(); it++)
    {
       string key = it->first;
       if(it->second.size()!= idx-2) continue;
       
       LL dv = isPrime(key,idx);
       if(dv!=-1) it->second.PB(dv);
    } 
    
    int printed = 0;
     for( map<string,vector<int> >::iterator it = d.begin(); it!=d.end(); it++)
    {
       string key = it->first;
       vector<int> value = it->second;
       if(value.size() !=upr-1) continue;
       cout<<key<<" ";REP(i,value.size()) cout<<value[i]<<" ";cout<<endl;
       ++printed;
       if(printed>=j) break;
    } 
    
  // REP(i,p.size())cout<<p[i]<<" ";cout<<endl;
}


int main(){
    //for(int i=2;i<=10;++i) cout<<isPrime("110111",i)<<endl;
    cout<<"Case #1:"<<endl;
    int t;cin>>t;
             int n,j; cin>>n>>j;
             solve(n,j);
             
    return 0;   
}
