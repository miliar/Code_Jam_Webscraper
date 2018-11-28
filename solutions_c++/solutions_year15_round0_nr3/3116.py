#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, map<char, string> > table;
map<string, string> multitab;
map<string,string>::iterator it;

string multiply1(char str1, string str2) {
  char index1 = str1;
  char index2 = str2[0];
  int sign = 1;
  if (str2.length() > 1) {
    sign = -1;
    index2 = str2[1];
  }
  string result = table[index1][index2];
  if (result.length() > 1) {
    if (sign == -1) {
      result = result[1];
      return result;
    }
    return result;
  }
  if (sign == -1) {
    result = "-"+result;
    return result;
  }
  return result;
}

string multiply(string str) {
  it = multitab.find(str);
  if (it != multitab.end()) {
    return it->second;
  }
  string output = "1";
  for (int c=0; c<str.length(); c++) {
    bool flag = false;
    char index1;
    char index2 = str[c];
    if (output[0] == '-') {
      flag = true;
      index1 = output[1];
    }
    else {
      index1 = output[0];
    }
    string tmp = table[index1][index2];
    if (tmp.length() == 1) {
      if (flag) {
        output = "-"+tmp;
      }
      else {
        output = tmp;
      }
    }
    else {
      if (flag) {
        output = tmp[1];
      }
      else {
        output = tmp;
      }
    }
  }
  multitab[str] = output;
  return output;
}

int isValid(string patt, int L, int X) {

  if (L*X < 3) {
    return 0;
  }
  else {
    string inp = "";
    for (int i=0; i<X; i++) {
      inp += patt;
    }
    int n = L*X;
    int k_start, j_start;
    string prev = "1";
    for (k_start=n-1; k_start>=2; k_start--) {
      string m1 = multiply1(inp[k_start], prev);
      if (m1 == "k") {
        break;
      }
      prev = m1;
    }
    if (k_start < 2)
      return 0;
    prev = "1";
    for (j_start = k_start-1; j_start >= 1; j_start--) {
      string m2 = multiply1(inp[j_start], prev);
      if (m2 == "j") {
        break;
      }
      prev = m2;
    }
    if (j_start < 1)
      return 0;
    string m3 = multiply(inp.substr(0, j_start));
    if (m3 == "i")
      return 1;
    return 0;
  }
  return 0;
}




int main(int argc, char *argv[]) {
  table['1']['1'] = "1";
  table['1']['i'] = "i";
  table['1']['j'] = "j";
  table['1']['k'] = "k";
  table['i']['1'] = "i";
  table['i']['i'] = "-1";
  table['i']['j'] = "k";
  table['i']['k'] = "-j";
  table['j']['1'] = "j";
  table['j']['i'] = "-k";
  table['j']['j'] = "-1";
  table['j']['k'] = "i";
  table['k']['1'] = "k";
  table['k']['i'] = "j";
  table['k']['j'] = "-i";
  table['k']['k'] = "-1";

  int tests;
  cin>>tests;
  int index = 1;
  while (index <= tests) {
    int L,X;
    cin>>L>>X;
    string patt;
    cin>>patt;
    if (isValid(patt, L, X)) {
      cout<<"Case #"<<index<<": YES"<<endl;
    }
    else {
      cout<<"Case #"<<index<<": NO"<<endl;
    }
    index++;
  }
  return 0;
}
