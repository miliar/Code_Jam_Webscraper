#include <iostream>
#include <string>
using namespace std;

int main(){

 int T,i,j;

 cin>>T;

 for(i=1;i<=T;++i){
   string str,last;
   string::iterator it;

   cin>>str;
   last.push_back(str[0]);
   for(j=1;j<str.size();++j){
     if(str[j] >= last[0]){
       last.insert(last.begin(),str[j]);
     } else
       last.insert(last.end(),str[j]);
   }
   cout<<"Case #"<<i<<": "<<last<<endl;
 }

 return 0;
}

