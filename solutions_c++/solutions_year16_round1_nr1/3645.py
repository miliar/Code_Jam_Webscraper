#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <map>
#include <tuple>
#include <string>
#include <iostream>

using namespace std;

vector<string> possiveis;

void generate(const string &letras, int pos, string *resp) {
  //printf("%s\n", (*resp).c_str());
  
  if(pos == letras.size()) {
    possiveis.push_back(*resp);
    return;
  }
  (*resp).push_back(letras[pos]);
  generate(letras, pos + 1, resp);
  (*resp).pop_back();
  (*resp).insert(0, 1, letras[pos]);
  generate(letras, pos + 1, resp);
  (*resp).erase((*resp).begin());
}

int main() {
  int n;
  scanf(" %d ", &n);
  for (int i = 0; i < n; i++) {
    char tmp[2000];
    scanf(" %s ", tmp);
    string letras = tmp;
    string resp = "";
    resp.push_back(letras[0]);
    for (size_t i = 1; i < letras.size(); i++) {
      char letra = letras[i];
      if(letra >= resp.front()) {
        resp.insert(0, 1, letra);
      } else {
        resp.push_back(letra);
      }
    }
    printf("Case #%d: %s\n", i+1, resp.c_str());
  }
}
