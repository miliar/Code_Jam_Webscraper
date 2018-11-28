#include <bits/stdc++.h>

using namespace std;

int countPeople(int x, string y) {
   int levPeople = 0;
   int nedPeople = 0;
   /*for(int i = 0; i < y.size(); i++) {
      int v = y[i] - '0';
      levPeople += v + nedPeople;
      if(i > levPeople) {
         nedPeople += i-levPeople;
      }
   }*/
   for(int i = 0; i < y.size(); i++) {
      if(i > levPeople) {
         nedPeople += i-levPeople;
         levPeople = i;
      }
      int v = y[i] - '0';
      levPeople += v;
   }
   return nedPeople;
}

int main() {
   freopen("A-large.in","r",stdin);
   freopen("A-large.out", "w", stdout);
   int n;
   double x;
   string y;
   int b = 0, aux;
   
   cin >> n;
   
   while(cin >> x >> y) {
      b++;
      int res = countPeople(x, y);
      cout << "Case " << "#" << b << ": " << res << endl;
   }
}