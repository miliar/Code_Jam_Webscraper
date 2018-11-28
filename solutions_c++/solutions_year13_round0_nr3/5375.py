#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<fstream>
#include<math.h>
using namespace std;
string convert(int num, int base);
bool checkpal(string s);
int main(){
  ifstream in("fairsquare.in");
  ofstream out ("fairsquare.out");
  int numtests; 
  int a, b;
  int rangeA, rangeB;
  int count;
  vector<int> output;
  //vector <string> palsq1;
  //vector <string> palsq2;
  int base = 10;
  in >> numtests;
  for(int i = 0; i < numtests; i++){
    in >> a >> b;
    count = 0;
    rangeA = (int)ceil (sqrt(a)) ;
    rangeB = (int) sqrt(b);
    //if (rangeA * rangeA < a ) rangeA++;
    for(int k = rangeA; k <=rangeB; k++){
      int square = k *k;
      string str = convert(square, base);
      string str1 = convert(k,base);
      if (checkpal(str) && checkpal(str1)) count++; 
    }
    output.push_back(count);
  }
  vector<int> :: iterator it;
  int i = 1;
  for(it = output.begin(); it != output.end(); ++it)
    cout <<"Case #"<<i++<<": "<< *it << endl;
  return 0;
}

string convert (int num, int base){
  vector <char> numlist;
  string str;
  while (num > 0 ) {
    int r = num % base;
    num /= base;
    if (r >= 10 ) { 
      r = r + 'A' - 10;
    } 
    else{
      r = r + '0';
    } 
    numlist.push_back(r);
  }
  while ( ! numlist.empty()){
    str += numlist.back();
    numlist.pop_back();
  }
  return str;
}


bool checkpal(string s){
  for (int i =0 ; i <= s.length()/2; ++i)
    if (s[i] != s[s.length() - i-1])
	  return false;
  return true;
}
