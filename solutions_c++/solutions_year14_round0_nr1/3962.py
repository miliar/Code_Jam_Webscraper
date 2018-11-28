#include <iostream>
#include <set>

using namespace std;

int main()
{
   int t;
   cin >> t;
   for (int cas = 1; cas<=t; cas++) {
       cout << "Case #" << cas << ": ";
       int first,second;
       set<int> s1,s2;
       cin >> first;
       int aux;
       for (int i=1; i<=4; i++) {
           for (int j=1;j<=4; j++) {
               cin >> aux;
               if (i == first) s1.insert(aux);
           }
       }
       cin >> second;
       for (int i=1; i<=4; i++) {
           for (int j=1;j<=4; j++) {
               cin >> aux;
               if (i == second and s1.count(aux)>0) s2.insert(aux);
           }
       }
       if (s2.size() == 0) cout << "Volunteer cheated!" << endl;
       else if (s2.size() > 1) cout << "Bad magician!" << endl;
       else {
           set<int>::iterator it = s2.begin();
           cout << (*it) << endl;
       }
   }
}

