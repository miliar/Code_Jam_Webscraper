#include <iostream>
#include <map>
using namespace std;

int main(){
   int T;
   cin >> T;
   for(int t=1; t<=T; t++){
      int number;
      int grid[4][4];
      cin >> number;
      number--;
      
      for(int i=0; i<4; i++)
	 for(int j=0; j<4; j++) cin >> grid[i][j];

      map<int,int>m;
      
      for(int i=0; i<4; i++) m[grid[number][i]]++;
      
      cin >> number;
      number--;
      for(int i=0; i<4; i++)
	 for(int j=0; j<4; j++) cin >> grid[i][j];

      for(int i=0; i<4; i++) m[grid[number][i]]++;

      int cnt = 0;
      int ans = 0;
      for(map<int,int>::iterator it = m.begin(); it != m.end(); it++){
	 if(it->second == 2){
	    ans = it->first;
	    cnt++;
	 }
      }

      cout << "Case #" << t << ": ";
      if(cnt == 1) cout << ans << endl;
      else if(cnt == 0) cout << "Volunteer cheated!" << endl;
      else cout << "Bad magician!" << endl;


      
   }
   return 0;
}
