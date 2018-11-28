#include<iostream>
#include<istream>
#include<vector>
#include<string>
#include<bitset>
#include<algorithm>
#include<sstream>
#include<map>
#include<set>
#include<cmath>
#include<stack>
#include<queue>
#include<cstdio>
using namespace std;
vector<long long int>ser;
bool palin(long long int n){
     stringstream ss;
     ss<<n;
     string s=ss.str();
     string str=s;
     reverse(s.begin(),s.end());
     return str==s;
}
void calculate(){
     for(long long int i=1;i<=10000000;++i){
             if(palin(i)){
                          long long int x=i*i;
                          
                           if(palin(x))ser.push_back(x);
                           }
     }
}
int main()
{
    calculate();
    /*for(long int i=0;i<ser.size();++i)
            cout<<ser[i]<<endl;*/
   long long int t;
    cin>>t;
   
   for(long long int i=0;i<t;++i){
         long long int a,b,count=0;
         cin>>a>>b;
         for(long long int j=0;j<ser.size();++j){
                 long long int x=ser[j];
                 if(x>=a && x<=b)count++;
                 if(x>b)break;
                 //else break;
         }
          cout<<"Case #"<<i+1<<": "<<count<<endl;        
   }
   
       
       
}
