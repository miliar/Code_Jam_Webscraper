


#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <stdlib.h>

#include <math.h>
#include <string.h>
#include <utility>
#include <climits>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <iomanip>


using namespace std;

int main(){

  int T;
  scanf("%d",&T);
for(int _T = 1; _T <= T; _T++){
  int M[15][15], M2[15][15], r1, r2; 
  vector<int> a, b;
a.clear(); b.clear();

  cin >> r1;
for(int i =1; i<=4; i++)
  for(int j = 1; j<=4; j++){
     cin >> M[i][j];  
if(i == r1)
  a.push_back(M[i][j]);

}

  cin >> r2;
for(int i =1; i<=4; i++)
  for(int j = 1; j<=4; j++){
     cin >> M2[i][j];
      
if(i == r2)
  b.push_back(M2[i][j]);
}

	int resp = 0;
	int number = -1;
	for(int i = 0;i <a.size(); i++){
 	   for(int j = 0; j<b.size(); j++ ){
  		if(a[i] == b[j]){
  		  resp++;
		  number = a[i];
		}
		  
	   }
	 	
	}
     


  if(resp == 0)
   printf("Case #%d: Volunteer cheated!\n", _T);
  else if (resp == 1)
   printf("Case #%d: %d\n", _T, number);
 else
  printf("Case #%d: Bad magician!\n", _T);

}

return 0;
}
