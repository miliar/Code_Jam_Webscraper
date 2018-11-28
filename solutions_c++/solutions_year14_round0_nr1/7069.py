#include <iostream>

using namespace std;

int main(){
  int n,a,b;
  int prvy [4][4];
  int druhy [4][4];
  cin >>n;
  for(int i=0; i<n; i++){
    cin >> a;
    for (int j=0; j<4; j++){
      for (int k=0; k<4; k++){
	cin >> prvy[j][k];
      }
    }
    cin >> b;
    for (int j=0; j<4; j++){
      for (int k=0; k<4; k++){
	cin >> druhy[j][k];
      }
    }
    //nacitane
    bool bolo=false;
    int kde=0;
    for (int j=0; j<4; j++){
      for (int k=0; k<4; k++){
	if (prvy[a-1][j]==druhy[b-1][k]){ 
	  if (bolo==true) kde=1000;
	  if (bolo==false) { bolo=true; kde=j;}
	}
      }
    }
    if (kde==1000) cout<<"Case #"<<i+1<<": Bad magician!\n";
    else if (bolo==false) cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
    else cout <<"Case #"<<i+1<<": "<<prvy[a-1][kde]<<endl;
  }
}
    
    
    