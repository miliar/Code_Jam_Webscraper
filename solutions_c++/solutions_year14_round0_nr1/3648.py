#include <iostream>
using namespace std;


int main() {
  int n;
  cin>>n;
  for(int i = 0; i < n; i++) {
    int P[4][2];
    int a[2];
    for(int l = 0; l < 2; l++) {
      cin>>a[l];
      for(int j = 0; j < 4; j++) {
	for(int k = 0; k < 4; k++) {
	  int tmp;
	  cin>>tmp;
	  if(j == a[l]-1) {
	    P[k][l] = tmp;
	  }
	}
      }
    }
    int il = 0;
    int li;
    for(int j = 0; j < 4; j++) {
      for(int k = 0; k < 4; k++) {
	
	if(P[j][0] == P[k][1]) {
	  il++;
	  li = P[j][0];
	}
      }
    }
    
    if(il == 1) cout<<"Case #"<<i+1<<": "<<li<<endl;
    if(il == 0) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    if(il > 1) cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
    
  }
}