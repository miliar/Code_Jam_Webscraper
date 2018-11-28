#include <iostream>  
#include <string>
using namespace std;

char nth_letter(int n)
{
    //assert(n >= 1 && n <= 26)
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[n-1];
}

bool tryOne(int ind, int totalNum, int size, int parl[]){
  totalNum = totalNum - 1;
  for(int i = 0; i < size; ++i){
    if(ind == i){
      continue;
    }
    if(2*parl[i]>totalNum){
      return false;
    }
  }
  return true;
}

bool tryTwo(int ind1, int ind2, int totalNum, int size, int parl[]){
  totalNum = totalNum - 2;
  for(int i = 0; i < size; ++i){
    if(ind1 == i || ind2 == i){
      continue;
    }
    if(2*parl[i]>totalNum){
      return false;
    }
  }
  return true;
}

string evacPlan(int p){
  int inP;
  int pMembers [p] = {0};
  int totalNum = 0;
  bool ok = false;
  string outString = "";
  // Read the party info
  for(int i = 1; i<= p; ++i){
    cin >> inP;
    pMembers[i-1] = inP;
    totalNum = totalNum + inP;
  }
  while(totalNum > 0){
    int i = 1;
    for(i = 1; i <= p; ++i){
      if(pMembers[i-1] == 0){
        continue;
      }
      ok = tryOne(i-1, totalNum, p, pMembers);
      if(ok == true){
        outString += ' ';
        outString += nth_letter(i);
        totalNum = totalNum - 1;
        pMembers[i-1] = pMembers[i-1] - 1;
      }
    }
    if(i == p+1 && ok == false){
      for(int j = 1; j <= p; ++j){
        if(pMembers[j-1] == 0){
          continue;
        }
        for(int k = 1; k <= p; ++k){
          if(pMembers[k-1] == 0){
            continue;
          }
          bool ok2 = tryTwo(j-1,k-1,totalNum, p,pMembers);
          if(ok2 == true){
            outString += ' ';
            outString += nth_letter(j);
            outString += nth_letter(k);
            totalNum = totalNum - 2;
            pMembers[j-1] = pMembers[j-1] - 1;
            pMembers[k-1] = pMembers[k-1] - 1;
          }
        }
      }
    }
  }
  return outString;
}

int main() {
  int t;
  int p; // Number of parties
  cin >> t;  // Number of cases
  for (int i = 1; i <= t; ++i) {
    cin >> p;  // read n and then m.
    
    cout << "Case #" << i << ": " << evacPlan(p) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
