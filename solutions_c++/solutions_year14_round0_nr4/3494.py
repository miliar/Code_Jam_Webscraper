#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
  cout.precision(3);
  cout<<fixed;
  int n;
  cin>>n;
  for(int i = 0; i < n; i++) {
    int a;
    cin>>a;
    vector <double> Naomi;
    vector <double> Ken;
    for(int j = 0; j < 2; j++) {
      for(int k = 0; k < a; k++) {
	double tmp;
	cin>>tmp;
	if(j)
	  Ken.push_back(tmp);
	else
	  Naomi.push_back(tmp);
      }
    }
    int wynik[2] = {0,0};
    vector <double> Kens = Ken;
    vector <double> Naomis = Naomi;
    for(int j = 0; j < Ken.size(); j++) {
      double mini[2] = {2,2};
      double maxi[2] = {0,0};
      int poz[4];
      for(int k = 0; k < Ken.size(); k++) {
	if(mini[0] > Ken[k] && Ken[k] != -1) {
	  poz[0] = k;
	  mini[0] = Ken[k];
	}
	if(mini[1] > Naomi[k] && Naomi[k] != -1) {
	  poz[1] = k;
	  mini[1] = Naomi[k];
	}
	if(maxi[0] < Ken[k] && Ken[k] != -1) {
	  poz[2] = k;
	  maxi[0] = Ken[k];
	}
	if(maxi[1] < Naomi[k] && Naomi[k] != -1) {
	  poz[3] = k;
	  maxi[1] = Naomi[k];
	}
      }
      
      if(mini[0] > mini[1]) {
	Naomi[poz[1]] = -1;
	Ken[poz[2]] = -1;
      } else {
	wynik[0]++;
	Naomi[poz[1]] = -1;
	Ken[poz[0]] = -1;
      }
      
    }
    for(int j = 0; j < Kens.size(); j++) {
      int poz[2];
      double minin = 2;
      for(int k = 0; k < Naomis.size(); k++) {
	if(minin > Naomis[k] && Naomis[k] != -1) {
	  poz[0] = k;
	  minin = Naomis[k];
	}
      }
      double maxin = 2;
      double mmm = 2;
      int pozz;
      for(int k = 0; k < Kens.size(); k++) {
	if(maxin > Kens[k] && Kens[k] > minin) {
	  poz[1] = k;
	  maxin = Kens[k];
	}
	if(mmm > Kens[k] && Naomis[k] != -1) {
	  pozz = k;
	  mmm = Kens[k];
	}
      }
      if(maxin == 2) {
	wynik[1]++;
	Kens[pozz] = -1;
	Naomis[poz[0]] = -1;
      } else {
	Kens[poz[1]] = -1;
	Naomis[poz[0]] = -1;
      }
      
    }
    
    
    cout<<"Case #"<<i+1<<": "<<wynik[0]<<" "<<wynik[1]<<endl;
  }
  
}