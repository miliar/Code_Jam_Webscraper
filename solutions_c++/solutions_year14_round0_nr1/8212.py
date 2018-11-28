using namespace std;


#include <iostream> 
#include <algorithm> 
#include <iterator> 
#include <sstream> 
#include <fstream> 
#include <cassert> 
#include <climits> 
#include <cstdlib> 
#include <cstring> 
#include <string> 
#include <cstdio> 
#include <vector> 
#include <cmath> 
#include <queue> 
#include <stack> 
#include <deque> 
#include <stack> 
#include <list> 
#include <map> 
#include <set> 

#define D(x) cout << #x " = " << (x) << endl

int arr1 [4][4];
int arr2 [4][4];
int row, row2;

int main(){
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    int z = 1;   
    while(n--){
       cin >> row;
       row--;
       for(int i = 0; i < 4; ++i){
          for(int j = 0; j < 4; j++) cin >> arr1[i][j];
       }
       cin >> row2;
       row2--;
       for(int i = 0; i < 4; ++i){
          for(int j = 0; j < 4; j++) cin >> arr2[i][j];
       }
       int acum = 0;
       int m;
       for(int i = 0; i < 4; i++){
          if(arr2[row2][i] == arr1[row][0] || arr2[row2][i] == arr1[row][1] || arr2[row2][i] == arr1[row][2] || arr2[row2][i] == arr1[row][3]){
             acum++;
             m = arr2[row2][i];
          }
             if(acum == 2) break;    
       }
       
       cout << "Case #" << z << ": ";
       
       if(acum == 1) cout << m;
       else if(acum == 0) cout << "Volunteer cheated!";
       else cout << "Bad magician!";
       cout << endl;
       
       z++;
       
    }
    
    
    return 0;    
}
