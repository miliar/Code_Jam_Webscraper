#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int calculate(int a, int b)
{
  int sig = 1;
  if (a < 0) {
    a = -a;
    sig *= -1;
  }
  if (b < 0) {
    b = -b;
    sig *= -1;
  }
  if (a == '1')
    return sig*b;
  if (b == '1')
    return sig*a;
  if (a == b)
    return sig*-1*'1';
  if (a == 'i' && b == 'j')
    return sig*'k';
  if (a == 'i' && b == 'k')
    return sig*-1*'j';
  if (a == 'j' && b == 'i')
    return sig*-1*'k';
  if (a == 'j' && b == 'k')
    return sig*'i';
  if (a == 'k' && b == 'i')
    return sig*'j';
  if (a == 'k' && b == 'j')
    return sig*-1*'i';
  return 0;
}


int main() {
  ifstream myfile("C-small-attempt1.in");
  ofstream of("output");
  int testcases;
  myfile >> testcases;
  int length;
  int repeat;
  int casenum = 1;
  while(myfile >> length >> repeat) {
    int len = length*repeat;
    string inputstr;
    myfile>>inputstr;
    if (len < 3) {
      of <<"Case #"<<casenum <<": NO"<<std::endl;
      casenum++;
      continue;
    }
    vector<bool>findi(len, false);
    vector<bool>findk(len, false);
    int init = inputstr[0];
    if (init == 'i')
      findi[0] = true;
    for (int i = 1; i < len-2; i++) {
      init = calculate(init, inputstr[i%length]);
      if (init == 'i')
	findi[i] = true;
    }
    init = inputstr[length-1];
    if (init == 'k')
      findk[len-1] = true;
    for (int j = len-2; j > 1; j--) {
      init = calculate(inputstr[j%length], init);
      if (init == 'k')
	findk[j] = true;
    }
    bool ret = false;
    for (int i = 0; i < len-2; i++) {
      if (findi[i]) {
	int calj = inputstr[(i+1)%length];
	if (calj == 'j' && findk[i+2]) {
	  ret = true;
	  break;
	}
	else {
	  for (int j = i+3; j < len; j++) {
	    calj = calculate(calj, inputstr[(j-1)%length]);
	    if (findk[j]) {
	      if (calj == 'j') {
		ret = true;
		j = len;
		i = len-2;
	      }	      
	    }
	  }
	}
      }
    }
    if (ret)
      of <<"Case #"<<casenum <<": YES"<<std::endl;
    else
      of <<"Case #"<<casenum <<": NO"<<std::endl;
    casenum++;
  }
  return 0;
}
