#include <fstream>
#include <iostream>

using namespace std;

int main() {
  
  ifstream input ("A-large.in");
  if (input.is_open()) {
    int testcases = 0;
    int max_s = 0;
    string descr_s ;
    input >> testcases;
    //    cout << testcases << endl;
    int count = 0;
    while (count < testcases) {
      int tmp = 0, sum = 0;
      input >> max_s;
      input >> descr_s;
      //      cout <<  max_s << " " << descr_s << endl;
      count ++;
      for (int i =0; i < descr_s.size(); ++i) {
	int val = i -(sum + tmp);
	//	cout <<  "sum = " <<  sum  << " temp= " << tmp << " - " << val << endl;
	//	cout <<  descr_s[i] << " - " << i << " - " << val << endl;

	if (val>0) tmp +=val;
	char digit = descr_s[i];
	sum += atoi(&digit);
      }
      cout << "Case #"<<count<<": " << tmp << endl;
    }	
  }
  input.close();
  return 0;
}
