#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<cmath>
using namespace std;

int main(){
  long long t=0, n=0, i=0, j=0, k=0, pocetnaomi=0, pocetken=0;
  cin >> t;
  for(i=0; i<t; i++){
    pocetnaomi=0;
    pocetken=0;
    j=0;
    k=0;
    cin >> n;
    vector<double> naomi (n);
    vector<double> ken (n);
    for(j=0; j<n; j++){
      cin >> naomi[j];
    }
    for(j=0; j<n; j++){
      cin >> ken[j];
    }
    j=0; k=0;
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    while(j<n && k<n){
//       cout << j << " " << k << endl;
      if(naomi[j]>ken[k]){
	j++;
	k++;
	pocetnaomi++;
      }
      if(naomi[j]<ken[k]){
	j++;
      }
    }
//     cout << pocetnaomi << endl;
    j=0; k=0;
    while(j<n && k<n){
      if(ken[j]>naomi[k]){
	j++;
	k++;
	pocetken++;
      }
      if(ken[j]<naomi[k]){
	j++;
      }
    }
//     cout << pocetken << endl;
    cout << "Case #" << i+1 << ": " << pocetnaomi << " " << n-pocetken << endl;
  }
  return 0;
}