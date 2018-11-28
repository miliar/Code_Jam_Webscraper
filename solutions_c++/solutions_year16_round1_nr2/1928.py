#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){

 int T,N,i,j,temp,val;

 cin>>T;
 for(i=1;i<=T;++i){
   vector<int> vec;
   for(j=0;j<=2500;++j)
     vec.push_back(0);
   cin>>N;
   val = 2*N*N -N;
   for(j=0;j<val;++j){
     cin>>temp;
     vec[temp]++;
   }
   vector<int> indexes;
   for(j=1;j<=2500;++j){
     if(vec[j] != 0){
       if(vec[j]%2){
         indexes.push_back(j);
       }
     }
   }
   sort(indexes.begin(),indexes.end());
   cout<<"Case #"<<i<<":";
   vector<int>::iterator it;
   for(it=indexes.begin();it!=indexes.end();++it)
      cout<<" "<<*it;
   cout<<endl;
 }

 return 0;

}
