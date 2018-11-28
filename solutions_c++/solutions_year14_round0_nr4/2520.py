#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool Isgr (float i, float j) { return i > j; }

int fairplay(std::vector<float> &p1,std::vector<float> p2){
   int p(0), s(p1.size());
   std::vector<float>::iterator it;
   for(int i = 0;i<s;i++) {
      it = std::upper_bound (p2.begin(), p2.end(), p1[i]);
      if(it != p2.end()) {
        p2.erase(it);
      } else {
         p++;
         p2.erase(p2.begin());
      }
   }
   return p;
}


int cheatplay(std::vector<float> &p1,std::vector<float> &p2,std::vector<float> &v){
   int p(0), pp(0), s(p1.size());

   while((p2.back()) > (p1.back())) {
      p1.erase(p1.begin());
      p2.pop_back();
   }

   std::vector<float>::iterator it = upper_bound (p1.begin(), p1.end(), p2[0]);
   int i = 0;
   while(it!= p1.end()) {
     pp++;
     p1.erase(it);
     p2.erase(p2.begin());
     it = upper_bound (p1.begin(), p1.end(), p2[0]);
     
   }
   return  pp;
}
int main() {
   int t,n(1),d;
   vector <float> p1, p2;
   vector <float> v;
   cin >> t;
   std::vector<float>::iterator it;
   int f(0),c(0);
   while(t--) {
      cin >> d;
      v.reserve(d<<1);
      p1.resize(d);
      p2.resize(d);
      for(int i=0;i<d;i++) cin >> p1[i];
      for(int i=0;i<d;i++) cin >> p2[i];
      sort(p1.begin(), p1.end());
      sort(p2.begin(), p2.end());
      it = set_union(p1.begin(),p1.end(),p2.begin(),p2.end(),v.begin());
      f = fairplay(p1,p2);
      c = cheatplay(p1,p2,v);
      cout << "Case #" << n++ <<": " << c << " " << f << endl;
      p1.clear();
      p2.clear();
      v.clear();
      f = 0;
      c = 0;
   }
   return 0;
}
