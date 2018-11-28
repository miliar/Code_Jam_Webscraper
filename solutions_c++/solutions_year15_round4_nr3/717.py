#include<bits/stdc++.h>
using namespace std;

void process(map<string,int>& S, string s){
   istringstream iss(s);
   string x;
   while(iss>>x) S[x] = 1;
}

vector<string> process(string s){
   istringstream iss(s);
   string x;
   vector<string> v;
   set<string> H;
   while(iss>>x) H.insert(x);
   return vector<string>(H.begin(),H.end());
}

vector<int> G[20];

vector<int> graycode(int n){
   if (G[n].size() != 0) return G[n];
   if (n == 1){
      vector<int> v; v.push_back(0);
      v.push_back(1);
      return G[n]=v;
   }
   vector<int> v = graycode(n-1);
   for(int i=v.size()-1; i>=0; i--){
      v.push_back(v[i]|(1<<(n-1)));
   }
   return G[n]=v;
}

ostream& operator<<(ostream& os, map<string,int>& H){
   for(map<string,int>::iterator it = H.begin(); it!= H.end(); it++){
      os<<"("<<(it->first)<<","<<(it->second)<<") ";
   }
   return os;
}
int eng[100000],fr[100000];

int f(){
   int ctr=0;
   for(int i=0; i<100000; i++){
      ctr += (eng[i] && fr[i]);
   }
   return ctr;
}

int main(){
   graycode(18);
   // puts("here");
   int T; scanf("%d",&T);
   for(int cs=0; cs<T; cs++){
      int n; scanf("%d",&n);
      string s; getline(cin,s);
      map<string,int> id;
      vector<vector<int> > v;
      for(int i=0; i<n; i++){
         getline(cin,s);
         istringstream iss(s);
         string x;
         set<int> w;
         while(iss>>x){
            int tmp = id.size();
            if (id.find(x) == id.end()) id[x]=tmp;
            w.insert(id[x]);
         }
         v.push_back(vector<int>(w.begin(),w.end()));
      }
      // puts("xx");
      fill(eng,eng+100000,0);
      fill(fr,fr+100000,0);
      // puts("here");
      for(int i=0; i<v[0].size(); i++) eng[v[0][i]]++;
      for(int i=0; i<v[1].size(); i++) fr[v[1][i]]++;
      
      n-=2;
      for(int i=0; i<n; i++){
         for(int j=0; j<v[2+i].size(); j++) eng[v[i+2][j]]++;
      }
      
      int minval = f();
      // printf("mv = %d\n",minval);
      int prev = minval;
      for(int i=1; i<G[n].size(); i++){
         int diff = (G[n][i]^G[n][i-1]);
         
         int x=0;
         while(diff%2 == 0){
            x++; diff>>=1;
         }
         // cout<<G[n][i-1]<<" "<<G[n][i]<<" "<<diff<<" "<<x<<endl;
         int curr = prev;
         if (G[n][i]&(1<<x)){  // from eng to fr
            for(int ii=0; ii<v[x+2].size(); ii++){
               // map<string,int>::iterator it1 = eng.find(v[x][ii]);
               // map<string,int>::iterator it2 = fr.find(v[x][ii]);
               bool common = (eng[v[x+2][ii]] && fr[v[x+2][ii]]);
               eng[v[x+2][ii]]--;
               fr[v[x+2][ii]]++;
               bool comm = (eng[v[x+2][ii]] && fr[v[x+2][ii]]);
               
               if (common && !comm) curr--;
               else if (!common && comm) curr++;
            }
         }
         else{
            for(int ii=0; ii<v[x+2].size(); ii++){
               // map<string,int>::iterator it1 = eng.find(v[x][ii]);
               // map<string,int>::iterator it2 = fr.find(v[x][ii]);
               bool common = (eng[v[x+2][ii]] && fr[v[x+2][ii]]);
               eng[v[x+2][ii]]++;
               fr[v[x+2][ii]]--;
               bool comm = (eng[v[x+2][ii]] && fr[v[x+2][ii]]);
               
               if (common && !comm) curr--;
               else if (!common && comm) curr++;
            }
         }
         // cout<<"Eng: "<<eng<<endl;
         // cout<<"Fr: "<<fr<<endl; 
         // puts("---");
         minval = min(minval,curr);
         prev = curr;
      }
      printf("Case #%d: %d\n",cs+1,minval);
   }
}