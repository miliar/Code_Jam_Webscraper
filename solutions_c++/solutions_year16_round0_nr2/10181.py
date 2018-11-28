#include<iostream>

using namespace std;

char negate_char(char c) {
   if(c=='+') return '-';
   return '+';
}

long long int flips(string s,char c) {
   for(int i=s.size()-1;i>=0;i--) {
       if(s[i]!=c) {
         long long int x=1;
         x+=(i>0?flips(s.substr(0,i),negate_char(c)):0);
         return x;
       }
   }
   return 0;
}

int main() {
  int t;
  string s;
  cin>>t;
  for(int i=1;i<=t;i++){
     cin>>s;
     cout<<"Case #"<<i<<": "<<flips(s,'+')<<"\n";
  }
}
