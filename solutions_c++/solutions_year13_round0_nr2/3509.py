#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;
int main()
{
  int T;
  cin >> T;
  for(int ca = 1; ca <= T; ca++){
    int h,w;
    cin >> h >> w;
    vector<vector<int> > map(h,vector<int>(w));
    for(int i=0; i<h; i++)
      for(int j=0; j<w; j++)
	cin >> map[i][j];
    bool bsuccess = true;
    for(int i=0; i<h; i++){
      for(int j=0; j<w; j++){
	bool bOK = true;
	for(int y = 0; y<h; y++)
	  if(map[y][j] > map[i][j]){
	    bOK = false;
	    break;
	  }
	if(bOK) continue;
	for(int x = 0; x<w; x++)
	  if(map[i][x] > map[i][j]){
	    bsuccess = false;
	    break;
	  }
      }
      if(!bsuccess) break;
    }
    printf("Case #%d: %s\n", ca, bsuccess ? "YES" : "NO");
  }
  return 0;
}
