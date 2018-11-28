#include <iostream>
#include <istream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

int currentCase = 0;
vector<int> arrange1;
vector<int> arrange2;
int answer1;
int answer2;

void printIntVect(vector<int> & vect) {
  vector<int>::iterator it = vect.begin();
  while (it != vect.end()) {
    cout << " " << *it ;
    it++;
  }
  cout << endl;
}

vector<string> split(const string &s, const char* delim) {
  vector<string> itemarr;
  stringstream ss(s);
  string item;
  while (getline(ss, item, *delim)) {
    itemarr.push_back(item);
  }
  return itemarr;
}

vector<int> stringArrToIntArr(vector<string> stringarr) {
  vector<int> itemarr;
  vector<string>::iterator it = stringarr.begin();
  while (it != stringarr.end()) {
    itemarr.push_back(atoi((*it).c_str()));
    it++;
  }
  return itemarr;
}

// void sortIncreasing(vector<int> & itemarr) {
//   sort(itemarr.begin(), itemarr.end());
// }

// // void filterBigger(vector<int> & itemarr) {
// //   vector<int>::iterator it = itemarr.end();
// //   cout << "Total Creds: " << totalcreds << endl;
// //   while (it != itemarr.begin()) {
// //     cout << "Item: " << *it << endl;
// //     if ((*it) > totalcreds) itemarr.pop_back();
// //     it--;
// //   }
// // }

// void initializeCheck(vector<int> &check) {
//   int length = itemarr.size();
//   while (length > 0) {
//     check.push_back(-1);
//     length--;
//   }
// }

// // void copyIntVect(vector<int> & from, vector<int> & to) {
// //   vector<int>::iterator it = from.begin();
// //   while (it != from.end()) {
// //     to.push_back((*it));
// //     it++;
// //   }
// // }

// bool solveProblemHelper(vector<int> & arr, vector<int> & result, vector<int> check, int front, int total) {
//   // cout << "check:";
//   // printIntVect(check);
//   // cout << "front: " << front << " total: " << total << endl;

//   if (front >= arr.size()) return false;
//   int item = arr[front]; 
//   if (item + total == totalcreds) {
//     check[front] = 1;
//     result = check;
//     // cout << "Solution found for check:";
//     // printIntVect(check);
//     return true;
//   }
//   if (item + total > totalcreds) {
//     check[front] = 0;
//     //cout << "Total " << item + total << " exceeds allowed total " << totalcreds << endl;
//     if (solveProblemHelper(arr, result, check, front + 1, total)) return true;
//     if (solveProblemHelper(arr, result, check, front + 1, total)) return true;
//     return false;
//   }
//   else  {
//     check[front] = 1;
//     if (solveProblemHelper(arr, result, check, front + 1, total + item)) return true;
//     check[front] = 0;
//     if (solveProblemHelper(arr, result, check, front + 1, total)) return true;
//     else {
//       check[front] = -1;
//       // cerr << "cannot find solution for check:";
//       // printIntVect(check);
//       return false;
//     }
//   }
// }

void solveProblem(ofstream & resultfile) {
  int caseresult = 0;
  int answercard = 0;

  int i = 0;
  while (i < arrange1.size()) {
    int j = 0;
    while (j < arrange2.size()) {
      if (arrange1[i] == arrange2[j]) {
        if (caseresult == 1 || caseresult == -1) {
          caseresult = -1;
          break;
        }
        else {
          caseresult = 1;
          answercard = arrange2[j];
        }
      }
    j++;
  }
  i++;
}
  
  resultfile << "Case #" << currentCase << ": ";
  if (caseresult == -1) resultfile << "Bad magician!";
  if (caseresult == 0) resultfile << "Volunteer cheated!";
  if (caseresult == 1) resultfile << answercard;
  resultfile << endl;
} 

int main () {
  ofstream resultfile;
  ifstream inputfile;
  inputfile.open ("input.in");
  resultfile.open ("result.txt");
  
  string line;
  int linenum = 0; // Line number starting from 1
  int parseline1 = -10;
  int parseline2 = -10;
  while ( getline (inputfile, line)) {
    linenum++;
    if (linenum == 1) {
      continue;
    }
    if (linenum == 2) {
      answer1 = atoi(line.c_str());
      parseline1 = answer1 + linenum;
      continue;
    }
    if (linenum == parseline1) {
      arrange1 = stringArrToIntArr(split(line, " "));
      parseline1 = -10;
      continue;
    }
    if (linenum == 7) {
      answer2 = atoi(line.c_str());
      parseline2 = answer2 + linenum;
      continue;
    }
    if (linenum == parseline2) {
      arrange2 = stringArrToIntArr(split(line, " "));
      parseline2 = -10;
      linenum = 1 - (4 - answer2);

      currentCase++; 
      solveProblem(resultfile);
      continue;
    }
  }

  inputfile.close();
  resultfile.close();
  return 0;
}
