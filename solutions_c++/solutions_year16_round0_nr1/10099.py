
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>

using namespace std;  

int main() {
  int t, n;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n;    
    set<int> rcount;
    bool found=false;
    int tn=n;
    int j=1;
    rcount.insert(tn);
    set<int> track;
    int result=tn;
    while(!found){
      while(tn!=0){
	int r=tn%10;
	tn=tn/10;
	track.insert(r);
      }
      if(track.size()==10){
	found=true;
	cout << "Case #" << i << ": " << result << "\n";
	break;
      }
      j++;
      tn=j*n;
      result=tn;
      if(rcount.find(tn)!=rcount.end()){
	cout << "Case #" << i << ": INSOMNIA\n";
	break;
      } else {
	rcount.insert(tn);
      }
    }
  }
  return 0;
}
