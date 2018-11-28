
#include <iostream>
#include <cstdlib>



using namespace std;

int main() {
  int mag[17];
  int nb_case;
  int cas;
  int i,j,k,row;
  int temp;
  int faute;

  cin >> nb_case;

  for(cas=1;cas<=nb_case;cas++) {
    for(i=0;i<17;i++) {
      mag[i]=0;
    }
    for(k=0;k<2;k++) {
      cin >> row;
      for(j=1;j<5;j++) {
	cin >> temp;
	if(row==j)
	  mag[temp]++;
	cin >> temp;
	if(row==j)
	  mag[temp]++;
	cin >> temp;
	if(row==j)
	  mag[temp]++;
	cin >> temp;
	if(row==j)
	  mag[temp]++;
      }
    }
    temp=-1;
    faute=0;
    for(i=1;i<17;i++) {
      if(temp==-1 && mag[i]==2)
	temp=i;
      else if(mag[i]==2)
	faute=1;
    }
    if(faute==1)
      cout << "Case #" << cas << ": Bad magician!" << endl;
    else if(temp==-1)
      cout << "Case #" << cas << ": Volunteer cheated!" << endl;
    else
      cout << "Case #" << cas << ": " << temp << endl;
  }

}
