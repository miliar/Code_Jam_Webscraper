#include <iostream>
#include <istream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cmath>
#include <iomanip>
using namespace std;

int currentCase = 0;
double mintime = 0.0;
vector<double> inputarr;


vector<string> split(const string &s, const char* delim) {
  vector<string> itemarr;
  stringstream ss(s);
  string item;
  while (getline(ss, item, *delim)) {
    itemarr.push_back(item);
  }
  return itemarr;
}

vector<double> stringArrToDoubleArr(vector<string> stringarr) {
  vector<double> itemarr;
  vector<string>::iterator it = stringarr.begin();
  while (it != stringarr.end()) {
    itemarr.push_back(atof((*it).c_str()));
    it++;
  }
  return itemarr;
}

double solveProblemHelper(double fprice, double frate, double winprice, double crate, double ctime) {
  double nofpurchase = winprice / crate + ctime;
  // double fpurchase_once = fprice / crate + winprice / (crate + frate);
  //if (nofpurchase < fpurchase_once) return nofpurchase;
  //cout << "current rate: " << crate << " current time: " << ctime ;
  //cout << " nofpurchase: " << nofpurchase << " pre-minimum: " << mintime << endl;
  if (nofpurchase > mintime) return mintime;
  if ((nofpurchase < mintime) && (mintime - nofpurchase < 0.0000001)) return mintime = nofpurchase;
  if (nofpurchase < mintime) mintime = nofpurchase;
  double fpurchase = solveProblemHelper(fprice, frate, winprice, crate + frate, fprice / crate + ctime);
 // cout << "fpurchase: " << fpurchase << " mid-minimum: " << mintime << endl;
  double minimum = fpurchase;
  if (nofpurchase < fpurchase) minimum = nofpurchase;
  if (mintime < minimum) return mintime;
  else return mintime = minimum;
  }

void solveProblem(ofstream & resultfile) {
  mintime = inputarr[2] / 2.0;
  double resultMin = solveProblemHelper(inputarr[0], inputarr[1], inputarr[2], 2.0, 0.0); 
  //cout << setprecision(15) << resultMin << endl;
  resultfile << "Case #" << currentCase << ": ";
  resultfile << setprecision(15) << resultMin; //round(resultMin * 10000000) / 10000000;
  resultfile << endl;
}

int main () {
  ofstream resultfile;
  ifstream inputfile;
  inputfile.open ("input.in");
  resultfile.open ("result.txt");
  
  string line;
  getline (inputfile, line);
  while (getline (inputfile, line)) {
    inputarr = stringArrToDoubleArr(split(line, " "));
    currentCase++; 
    solveProblem(resultfile);
    continue;
  }

  inputfile.close();
  resultfile.close();
  return 0;
}
