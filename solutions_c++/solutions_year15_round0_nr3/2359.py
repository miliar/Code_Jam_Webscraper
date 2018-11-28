#include<fstream>
#include<iostream>
#include<cstdio>
#include<map>
#include<string>

using namespace std;

#define FL(i, a, b) for(int i = a; i < b; i++)
#define MIN(a, b) ((a > b)? b : a)
#define MAX(a, b) ((a > b)? a : b)

string CODE[64] = {"1", "i", "j", "k", "-1", "-i", "-j", "-k",
                       "i", "-1", "k", "-j", "-i", "1", "-k", "j",
                       "j", "-k", "-1", "i", "-j", "k", "1", "-i",
                       "k", "j", "-i", "-1", "-k", "-j", "i", "1",
                       "-1", "-i", "-j", "-k", "1", "i", "j", "k",
                       "-i", "1", "-k", "j", "i", "-1", "k", "-j",
                       "-j", "k", "1", "-i", "j", "-k", "-1", "i",
                       "-k", "-j", "i", "1", "k", "j", "-i", "-1"};

int decode(string input) {
  if (input == "1")
    return 0;
  else if (input == "i")
    return 1;
  else if (input == "j")
    return 2;
  else if (input == "k")
    return 3;
  else if (input == "-1")
    return 4;
  else if (input == "-i")
    return 5;
  else if (input == "-j")
    return 6;
  else if (input == "-k")
    return 7;
  return -1;
}

string multiply(string a, string b) {
  int num_a = decode(a);
  int num_b = decode(b);
  return CODE[num_a * 8 + num_b];
}

int L;
long long X;
string S;

int len;
string final_S;

bool check(string target, int& l) {
  string str = "1";
  while (l < len) {
    string substr(1, final_S[l]);
    str = multiply(str, substr);

//cout<<l<<" "<<str<<" "<<len<<endl;

    l++;

    if (str == target)
      return true;
  }
  return false;
}

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("file input\n");
    return -1;
  }

  ifstream fin(argv[1]);

  int T;
  fin>>T;
  FL(t,0,T) {
    fin>>L>>X>>S;
    X = X%100;
    len = L*X;
    final_S.clear();
    FL(i,0,X) {
      final_S = final_S + S;
    }

    int l = 0;
    bool fail = false;

    fail = !check("i", l);
    if (!fail) {
      fail = !check("j", l);
    }
    if (!fail) {
      fail = !check("k", l);
    }

    if (!fail) {
      string final_check = "1";
      FL(i,l,len) {
        string substr(1, final_S[i]);
        final_check = multiply(final_check, substr);    
      }
      fail = final_check != "1";
    }

    printf("Case #%d: %s\n",t + 1, fail ? "NO" : "YES");

//cin.get();

  }
  return 0;
}




