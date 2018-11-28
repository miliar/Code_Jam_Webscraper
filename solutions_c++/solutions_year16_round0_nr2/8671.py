#include <iostream>
#include<queue>
#include<map>

using namespace std;

bool isHappy(string pan){
   bool happy=true;
   for(size_t i=0;i<pan.size();++i){
      if(pan[i]=='-')happy=false;
   }
   return happy;
}

int main(){
   long T;
   string pan;
   cin >> T;
   for(long t=1;t<=T;++t){
      cin >> pan;
      queue<pair<string,long long> > q;
      map<string,bool> h;
      h.insert(make_pair(pan,true));
      q.push(make_pair(pan,0));
      long long resp=-1;
      while(!q.empty()){
         string stk = q.front().first;
         long long count = q.front().second;
         if(isHappy(stk)){
            resp=count;
            break;
         }
         q.pop();
         for(size_t i=0;i<stk.size();++i){
            string n_stk(stk);
            for(size_t j=0;j<=i/2;++j){
               char v1 = n_stk[j];
               char v2 = n_stk[i-j];
               v1 = v1=='-'?'+':'-';
               v2 = v2=='-'?'+':'-';
               n_stk[j]=v2;
               n_stk[i-j]=v1;
            }
            if(h.find(n_stk)==h.end()){
               q.push(make_pair(n_stk,count+1));
               h.insert(make_pair(n_stk,true));
            }
         }
      }
      cout << "Case #"<<t<<": "<<resp<<endl;
   }
   return 0;
}
