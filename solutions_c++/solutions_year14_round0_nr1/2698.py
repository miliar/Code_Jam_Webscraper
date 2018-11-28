#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
   int t,n(1),g1,g2;
   string bad("Bad magician!"), vc("Volunteer cheated!");
   cin >> t;
   vector < vector<int> > v1(4, vector<int>(4));
   vector < vector<int> > v2(4, vector<int>(4));
   vector <int> v(8);
   std::vector<int>::iterator it;
//   v.reserve(4);
   while(t--) {
      cin >> g1;
      g1--;
    //  cout << "g1 " << g1 << endl;
      for (int i=0;i<4;i++)
         for (int j=0;j<4;j++)
            cin >> v1[i][j];
      cin >> g2;
      g2--;
  //    cout << "g2 " << g2 << endl;
      for (int i=0;i<4;i++)
         for (int j=0;j<4;j++)
            cin >> v2[i][j];
      sort(v1[g1].begin(),v1[g1].end()); 
      sort(v2[g2].begin(),v2[g2].end());
//      for (int i=0;i<4;i++)
//         cout << v1[g1][i] << " ";
//      cout << endl;
//      for (int i=0;i<4;i++)
//         cout << v2[g2][i] << " ";
//      cout << endl;
      it = set_intersection(v1[g1].begin(),v1[g1].end(),v2[g2].begin(),v2[g2].end(),v.begin());
      cout << "Case #" << n++ <<": ";
      v.resize(it-v.begin());
      if(v.size() == 0) cout << vc << endl;
      else if(v.size() > 1) cout << bad << endl;
      else cout << v[0] << endl;
//      cout << v.size() << endl;
      v.clear();
      v.resize(8);
   }
   return 0;
}
