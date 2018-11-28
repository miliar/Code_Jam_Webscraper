#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

int main() {
  int T,N;
  in >> T;
  for (int curcase = 1; curcase <= T; curcase++) {
    in >> N;
    vector<double> naomi(N),ken(N);
    for (int i=0; i<N; i++) {
      in >> naomi[i];
    }
    for (int i=0; i<N; i++) {
      in >> ken[i];
    }
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    out << "Case #" << curcase << ": ";
    
    int numwin=0;
    for (int i=N-1,j=N-1; i>=0; i--,j--,numwin++) {
      while (j>=0 && ken[j] > naomi[i]) {
	j--;
      }
      if (j<0) {
	break;
      }      
    }

    out << numwin << " ";

    numwin=N;
    for (int i=0,j=0; i<N; i++,j++,numwin--) {
      while (j<N && ken[j] < naomi[i]) {
	j++;
      }
      if (j>=N) {
	break;
      }
    }

    out << numwin << endl;
  }
}
