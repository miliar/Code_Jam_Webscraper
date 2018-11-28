#include<bits/stdc++.h>
using namespace std;
int ans;
map<vector<int>, int> m;
void func(vector<int> v,int cnt){
   if(v.size() == 0){
      ans = min(ans,cnt);
      return;
   }
   sort(v.begin(),v.end());
   if(m.find(v)!=m.end()){
      if(m[v] <= cnt) return;
   }
   m[v] = cnt;
   int maxId=v.size()-1;
   int maxV=v[maxId],maxhv;
   //
   vector<int> v1,v2;
   for(int i=0;i<v.size();i++) if(v[i]>1) v1.push_back(v[i]-1);
   func(v1,cnt+1);

   maxhv = maxV/2;
   v.push_back(0);
   int t = v.size()-1;
   for(int i=1;i<=maxhv;i++){
      v[maxId] = maxV-i;
      v[t] = i;
      func(v,cnt+1);
   }
}


int main(){
   int test,t=0;
   cin >> test;
   while(test--){
      m.clear();
      ans = INT_MAX;
      vector<int> v;
      int n,tmp;
      cin >> n;
      for(int i=0;i<n;i++){
         cin >> tmp;
         v.push_back(tmp);
      }
      func(v,0);
//      cout << "-------------------------------------------------------------\n";
      cout << "Case #" << ++t << ": " << ans << "\n";
   }
}

