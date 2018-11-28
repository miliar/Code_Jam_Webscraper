#include<iostream>
using namespace std;

int main (){
  int t;
  cin>>t;
  bool poss [17];
  for (int it = 1;it<=t;++it){
    int r, x;
    cin>>r;
    for (int i=0;i<4;++i){
      for (int j=0;j<4;++j){
	cin>>x;
	if (i==(r-1))poss[x] = 1;
	else poss[x] = 0;
      }
    }

    int tot = 0;
    
    cin>>r;
    for (int i=0;i<4;++i){
      for (int j=0;j<4;++j){
	cin>>x;
	if (i==(r-1) && poss[x] == 1) tot ++;
	else poss[x] = 0;
      }
    }

    cout<<"Case #"<<it<<": ";
    if (tot == 1){
      for (int i=1;i<=16;++i)if (poss[i])cout<<i<<"\n";
    }
    else if (tot > 1)
      cout<<"Bad magician!\n";
    else 
      cout<<"Volunteer cheated!\n";

  }
  return 0;
}
