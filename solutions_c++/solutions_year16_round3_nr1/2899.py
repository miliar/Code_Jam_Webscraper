#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <algorithm> 
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int sumv(vector<int> v);

int main() {
  char A[26] = "ABCDEFGHIJKLMNOPQRSTUWXYZ";
  int T;
  cin >> T;
  int size ; 
  int e;
  int Tot; 
  int max,maxs;
  vector<int> P; 
  for (int i = 0; i < T; ++i) {
    max=0;
    maxs=0; 
    cout << "Case #" << i+1 << ": ";
    cin >> size;
    
    for ( int j = 0 ; j< size ; ++j ) {
        cin >> e; 
        P.push_back(e); 
    }
    Tot = sumv(P);
    
    while ( Tot != 0 ){
        for( int l = 0 ; l< P.size(); ++ l){
            if( P[l] >= P[max]){
                maxs=max;
                max = l; 
            }
        }
        if( Tot % 2 == 0 ){ 
            P[max]--; 
            P[maxs]--; 
            cout<< A[max]<<A[maxs]<<" "; 
            Tot -= 2;
        }else{
            P[max]--; 
            cout<< A[max]<<" "; 
            Tot -= 1;
        }
        
    }    
    
    
    cout << endl;
    P.clear();
  }
  
  
  return 0;
}

int sumv ( vector<int> v){
   int s (0);
   for( int i = 0; i < v.size(); ++i){
       s+= v[i]; 
   }
   return s; 
}