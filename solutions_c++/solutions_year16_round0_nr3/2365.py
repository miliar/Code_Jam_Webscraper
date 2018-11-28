#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<utility>
#include<iomanip>
#include<cmath>
#include<cstdlib>
#include<ctime>

using namespace std;

long long findPrime(string s, int b){
     long long num=0;
     for(int i=0;i<s.size();++i){
             if(s[i]=='1') num=num*b+1;
             else if(s[i]=='0') num=num*b;}
     long long bound=(long long)sqrt((double)num);
     for(long long k=2;k<=bound;++k){
             if(num%k==0) return k;}
     return -1;}
     
  
                          
     
map<string,vector<long long> > jamcoin(int N, int J){
      string sol(N,'0');
      sol[0]='1';
      sol[N-1]='1';
      map<string,vector<long long> > m;
      while(m.size()<J){
      for(int i=1;i<N-1;++i){
        bool t=rand()%2;
        if(t)sol[i]='1';
        else sol[i]='0';}
      vector<long long> tmp;
     for(int b=2;b<=10;++b){
             long long f=findPrime(sol,b);
             if(f==-1) break;
             else if(f>0) tmp.push_back(f);}     
      if(tmp.size()==9){m[sol]=tmp;}
      }     
      return m;}
      
              



int main(){
    ifstream infile("C-small-attempt2.txt");
    ofstream ofile("C-small-output.txt");
    srand(time(0));
    int cases;
    if(infile.is_open()&&ofile.is_open()){
       infile>>cases;
       int curcase=1;
       while(curcase<=cases){
          int N,J;
          infile>>N>>J;
          map<string,vector<long long> > m;
          m=jamcoin(N,J);
          ofile<<"Case #"<<curcase<<":"<<endl;
          for(map<string,vector<long long> >::iterator i=m.begin();i!=m.end();++i){
                ofile<<i->first<<" ";
                for(int j=0;j<(i->second).size();++j){
                        ofile<<(i->second)[j]<<" ";}
                ofile<<endl;}
          
          ++curcase;
                         }
           }
       infile.close();
       ofile.close();
       return 0;}


