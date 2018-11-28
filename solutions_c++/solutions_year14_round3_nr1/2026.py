#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<sstream>

using namespace std;

#define diff 0.00000000000001

int N;
string current;
int first;
int last;

float c;

ofstream myfile;

void input() {
  cin >> current;
  string str = current.substr(0, current.find("/"));
  string str1 = current.substr(current.find("/") + 1);

  istringstream ( str  ) >>  first;
  istringstream ( str1  ) >>  last;
}

bool is_power(int n) {
  bool is = false;

  while(true) {
    if(n == 1) return true;
    if(n % 2 == 1) return false;
    n /= 2;
  }
}

void process(int n) {
  bool found = true;
  bool first_found = false;
  int answer = 0;


  while(true) {
    if(first_found == false)
      answer += 1;

    last /= 2;
    if(first == last) break;
    if(first > last) {
      first -= last;
      first_found = true;
    }
    if(last % 2 != 0) {
      found = false;
      break;
    }
  }

  if(found) {
    cout << "Case #" << n << ": " << answer << endl;
    myfile << "Case #" << n << ": " << answer << endl;
  } else {
    cout << "Case #" << n << ": impossible" << endl;
    myfile << "Case #" << n << ": impossible" << endl;
  }
}

int main() {
  cin >> N;
  myfile.open("a.output");
  for(int i = 0; i < N; i++) {
    input();
    process(i + 1);
  }
  myfile.close();
}
