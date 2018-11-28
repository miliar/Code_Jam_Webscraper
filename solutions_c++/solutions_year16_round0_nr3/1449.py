// Anve$hi $hukla
#include <bits/stdc++.h>
using namespace std;
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(NULL);}}$;

typedef long long LL;
const int Maxn = 200005;
#define TRACE
#ifdef TRACE
#define trace1(x)       cerr<< #x <<": "<<x<<endl;
#define trace2(x, y)    cerr<< #x <<": "<<x<<" | "<< #y <<": "<<y<< endl;
#define trace3(x, y, z) cerr<< #x <<": "<<x<<" | "<< #y <<": "<<y<<" | "<< #z <<": "<<z<< endl;
#else
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#endif

int main(){

   int t, n, J;
   cin >> t;
   for(int x=1;x<=t;x++){
      vector <int> odd, even;
      cin >> n >> J;
      for(int i=1;i<n-1;i++){
         if(i%2 == 1)
            odd.push_back(i);
         else
            even.push_back(i);
      }

      vector < pair< pair<int,int>, pair<int,int> > > arr;

      for(int i=0;i<odd.size();i++){
         for(int j=i+1;j<odd.size();j++){
            for(int k=0;k<even.size();k++){
               for(int l=k+1;l<even.size();l++){
                  arr.push_back({{odd[i], odd[j]}, {even[k], even[l]}});
               }
            }
         }
      }

      /*for(int i=0;i<500;i++){
         trace3(i, arr[i].first.first, arr[i].first.second);
         trace3(i, arr[i].second.first, arr[i].second.second);
      }
      for(int i=0;i<500;i++){
         for(int j=i+1;j<500;j++){
            if(arr[i].first.first == arr[j].first.first &&
               arr[i].first.second == arr[j].first.second &&
               arr[i].second.first == arr[j].second.first &&
               arr[i].second.second == arr[j].second.second)
               trace2(i, j);
         }
      }*/

      cout << "Case #" << x << ":" << endl;
      assert(J == 500);
      for(int i=0;i<J;i++){
         bool z[n];

         for(int j=0;j<n;j++){
            z[j] = 0;
         }

         z[0] = 1;
         z[n-1] = 1;
         z[arr[i].first.first] = 1;
         z[arr[i].first.second] = 1;
         z[arr[i].second.first] = 1;
         z[arr[i].second.second] = 1;

         for(int j=0;j<n;j++){
            cout << z[j];
         }

         for(int j=2;j<11;j++){
            cout << " " << j+1;
         }
         cout << endl;
      }
   }      
   return 0;
}