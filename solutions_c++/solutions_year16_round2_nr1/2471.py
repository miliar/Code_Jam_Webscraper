#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int main() {
  int T;
  string s;
  cin >> T;
  for(int i=0; i<T; i++) {
    cin >> s;
    
    map<int, int> digits;
    for(int j=0; j<10; j++) digits[j] = 0;

    map<char, int> chars;
    for(int j=0; j<s.size(); j++) {
      if(chars.find(s[j]) == chars.end()) {
        chars[s[j]] = 0;
      }
      chars[s[j]]++;
    }

    auto zts = chars.find('Z');
    if(zts != chars.end()) {
      digits[0] += zts->second;
      chars['E']-=zts->second;
      chars['R']-=zts->second;
      chars['O']-=zts->second;
    }

    auto ws = chars.find('W');
    if(ws != chars.end()) {
      digits[2] += ws->second;
      chars['T']-=ws->second;
      chars['O']-=ws->second;
    }

    auto us = chars.find('U');
    if(us != chars.end()) {
      digits[4] += us->second;
      chars['F']-=us->second;
      chars['O']-=us->second;
      chars['R']-=us->second;
    }

    auto xs = chars.find('X');
    if(xs != chars.end()) {
        digits[6] += xs->second;
        chars['S']-=xs->second;
        chars['I']-=xs->second;
    }

    auto gs = chars.find('G');
    if(gs != chars.end()) {
      digits[8] += gs->second;
      chars['E']-=gs->second;
      chars['I']-=gs->second;
      chars['H']-=gs->second;
      chars['T']-=gs->second;
    }

    auto os = chars.find('O');
    if(os != chars.end()) {
      digits[1] += os->second;
      chars['N']-=os->second;
      chars['E']-=os->second;
    }

    auto ts = chars.find('T');
    if(ts != chars.end()) {
      digits[3]+=ts->second;
      chars['H']-=ts->second;
      chars['R']-=ts->second;
      chars['E']-=2*ts->second;
    }

    auto fs = chars.find('F');
    if(fs != chars.end()) {
      digits[5]+=fs->second;
      chars['I']-=fs->second;
      chars['V']-=fs->second;
      chars['E']-=fs->second;
    }

    auto ss = chars.find('S');
    if(ss != chars.end()) {
      digits[7] +=ss->second;
      chars['E']-=ss->second;
      chars['V']-=ss->second;
      chars['E']-=ss->second;
      chars['N']-=ss->second;
    }

    auto ns = chars.find('N');
    if(ns != chars.end()) {
      digits[9] += (ns->second)/2;
    }

    cout << "Case #" << (i+1) << ": "; 
    for(int j=0; j<10; j++) {
      for(int k=0; k<digits[j]; k++) {
        cout << j;
      }
    }
    cout << endl;
  }
  return 0;
}