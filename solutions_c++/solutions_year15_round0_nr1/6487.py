

#include <iostream>
using namespace std;

int main() {
  int cases,si_max,i,j,ppl_standing,ppl_needed;
  char si_list[1001];
  cin >> cases;
  for(i=0 ; i<cases;) {
    cin >> si_max;
    cin >> si_list;
    ppl_standing=0;
    ppl_needed=0;
    for(j=0;j<=si_max;j++) {
      if( ppl_standing < j ) {
	ppl_needed += 1;
	ppl_standing += 1;
      }
      ppl_standing += ( si_list[j]-'0' )? si_list[j]-'0':0;
    }
    cout << "Case #" << ++i << ": "<< ppl_needed <<endl;
  }
}
