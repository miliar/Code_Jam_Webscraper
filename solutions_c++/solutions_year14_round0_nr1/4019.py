#include <iostream>
using namespace std;

bool contain(int r[4],int grid[4][4],int row) {
  bool res = false;
  int needle;
  for(int i=0;i<4;i++) {
    needle = r[i];
    bool flag = false;
    for(int j=0;j<4;j++) {
     if(grid[row][j] == needle) {
      flag = true;
      break;
     }
    }
    res = res || flag;
  }
  return res;
}

int find(int r[4],int grid[4][4],int row) {
  int res[4];
  for(int i=0;i<4;i++) {
   for(int j=0;j<4;j++) {
    for(int k=0;k<4;k++) {
     if(grid[i][j] == r[k]) {
      res[k]= i;
     }
    }
   }
  }
  
  int cnt=0;
  for(int i=0;i<4;i++) {
   if(res[i] == row)
    cnt++;
  }
  
  if(cnt > 1)
  return -1;
  
  for(int i=0;i<4;i++)
   if(res[i] == row)
    return r[i];
}

int main() {
	// your code goes here
	int t;
	int c1,c2;
	int g = 4;
	int grid[4][4];
	int init[4];
	cin>>t;
	for(int i=0;i<t;i++) {
	  cin>>c1;
	  c1--;
	  for(int k=0;k<g;k++) {
	   for(int l=0;l<g;l++) {
	     cin>>grid[k][l];
	     if(k == c1) {
	       init[l]=grid[k][l];
	     }
	   }
	  }
	  
	  cin>> c2;
	  c2--;
      for(int k=0;k<g;k++) {
	   for(int l=0;l<g;l++) {
	     cin>>grid[k][l];
	   }
	  }	  
	  
	  if (!contain(init,grid,c2)) {
	    cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
	  } else {
	    int res = find (init,grid,c2);
	    if(res == -1)
	    cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
	    else
	    cout<<"Case #"<<i+1<<": "<<res<<endl;
	  }
	}
	return 0;
}