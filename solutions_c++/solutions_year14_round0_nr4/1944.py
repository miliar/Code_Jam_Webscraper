#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  vector <double> naomi;
  vector <double> ken;
  int ken_max,ken_min;
  int i,j,k;
  int nb_cas,cas;
  int nb_blocks,points,points_deceived;
  cin >> nb_cas;
  for(cas=1;cas<=nb_cas;cas++) {
    cin >> nb_blocks;
    naomi.resize(nb_blocks);
    ken.resize(nb_blocks);
    for(i=0;i<nb_blocks;i++)
      cin >> naomi[i];
    for(i=0;i<nb_blocks;i++)
      cin >> ken[i];
    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());
    ken_max=nb_blocks-1;
    ken_min=0;
    points=0;
    points_deceived=0;
    for(i=0;i<nb_blocks;i++) {
      if(naomi[i]>ken[ken_min]) {
	points_deceived++;
	ken_min++;
      }
      else {
	ken_max--;
      }
    }
    ken_min=0;
    ken_max=nb_blocks-1;
    for(i=0;i<nb_blocks;i++) {
      for(j=0;j<nb_blocks;j++){
	if(ken[j]>naomi[i]) {
	  ken[j]=0;
	  points++;
	  break;
	}
      }
    }
    points=nb_blocks-points;
    cout << "Case #" << cas << ": " << points_deceived << " " << points << endl;
    //    cout << points << endl;
  }
}
