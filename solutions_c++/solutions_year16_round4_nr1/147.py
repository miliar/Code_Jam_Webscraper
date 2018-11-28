#include <stdio.h>
#include <map>
#include <string>

struct Data{
   int p, r, s;
   Data(int _p = 0, int _r = 0, int _s = 0){
      p = _p;
      r = _r;
      s = _s;
   }
   bool operator < (const Data& d) const {
      if(p != d.p) return p < d.p;
      if(r != d.r) return r < d.r;
      return s < d.s;
   }
};

std::map<Data, std::string> mp;

std::string next(std::string str){
   std::string ret;
   if(str.size() == 1){
      if(str[0] == 'P')
         return "PR";
      if(str[0] == 'R')
         return "RS";
      if(str[0] == 'S')
         return "PS";
   }
   int n = str.size() / 2;
   std::string ret1, ret2;
   ret1 = next(str.substr(0, n));
   ret2 = next(str.substr(n));
   if(ret1 < ret2)
      return ret1 + ret2;
   else
      return ret2 + ret1;
}

Data getData(std::string str){
   Data data;
   for(int i=0; i<str.size(); ++i){
      if(str[i] == 'P')
         data.p += 1;
      if(str[i] == 'R')
         data.r += 1;
      if(str[i] == 'S')
         data.s += 1;
   }
   return data;
}

void run(std::string str){
   for(int i=0; i<=13; ++i){
      Data data = getData(str);
      mp[data] = str;
      str = next(str);
   }
}

int main(){
   mp.clear();
   run("P");
   run("R");
   run("S");
   int T, n, r, p, s;
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      printf("Case #%d: ", t);
      scanf("%d%d%d%d", &n, &r, &p, &s);
      Data data(p, r, s);
      if(mp.find(data) == mp.end())
         printf("IMPOSSIBLE\n");
      else
         printf("%s\n", mp[data].c_str());
   }
   return 0;
}
