#include <iostream>
#include <iomanip>   
#include <fstream>
#include <vector>
#include <string>

using namespace std;



int prod[16] = {0, 1, 2, 3, 
                1, 0, 3, 2,
                2, 3, 0, 1,
                3, 2, 1, 0};

int signTab[16] = {1,  1,  1,  1, 
                   1, -1,  1, -1,
                   1, -1, -1,  1,
                   1,  1, -1, -1};

inline
vector<int> char2int(string combi){
  vector<int> tab(combi.size());
  for(int i = 0; i < combi.size(); i++){
    if(combi[i] == 'i'){ tab[i] = 1;}
    if(combi[i] == 'j'){ tab[i] = 2;}
    if(combi[i] == 'k'){ tab[i] = 3;}
  }
  return tab;
}

inline
int mult(int i, int j, int &sign){
  int index = 4*abs(i)+abs(j);
  sign *= signTab[index];
  return prod[index];
}

inline
int value(const vector<int> &combi, int &sign){
  int prod = 0;
  for(int i = 0; i < combi.size(); i++){
    prod = mult(prod, combi[i], sign);
  }
  return prod;
}

inline
bool possible(int value, int X, int sign){
  if(value == 0 && sign == 1){
    return false;
  }

  if(value == 0 && sign == -1){
    return X%2 == 1;
  }

  return X%4 == 2;
}

inline
bool termPossible(const vector<int> &combi, int term, int combiVal, int &index, int &neededChain){
  int prod = 0;
  int sign = 0;
  neededChain = 0;
  for(int i = 0; i < combi.size(); i++){
    prod = mult(prod, combi[i], sign);
    if(prod == term){
      index = i+1;
      return true;
    }
  }

  int prevProd = prod;
  while(prod != combiVal){
    prod = mult(prod, combiVal, sign);
    neededChain ++;
    if(prod == term){
      index = 0;
      return true;
    }
    if(prod == prevProd){
      break;
    }
  }
  return false;
}

inline
vector<int> concat(const vector<int> &c1, const vector<int> &c2){
  vector<int> res = c1;
  res.resize(c1.size()+c2.size());
  for(int i = 0; i < c2.size(); i++){
    res[c1.size()+i] = c2[i];
  }
  return res;
}

int main(int argc, char *argv[]) {
  string inPath = argv[1];
  string outPath = argv[2];

  // open two files
  ifstream input(inPath, std::ifstream::in);
  ofstream output(outPath, std::ios::out | std::ios::trunc);

  // read input file
  int nInput;
  input >> nInput;

  for(unsigned int k = 0; k < nInput; k++){
    cout << k << endl;
    // read input
    int L, X;
    string ijk;
    input >> L >> X >> ijk;
    if(k == 31){
      cout << L << "/" << X << "/" << ijk << endl;
    }
    // compute ijk value
    vector<int> combi = char2int(ijk);
    int sign = 1;
    int val = value(combi, sign);

    string answer = "NO";
    if(possible(val, X, sign)){
      answer = "YES";
      vector<int> tempCombi;
      
      if(X > 1){
        tempCombi = concat(combi, combi);
        X -= 2;
      }
      else{
        tempCombi = combi;
        X --;
      }

      for(int i = 1; i < 4; i++){
        int index, neededChain;
        // negative issue
        bool possible = termPossible(tempCombi, i, val, index, neededChain);
        X -= neededChain;
        if(!possible || X < 0){
          answer = "NO";
          break;
        }
        // else
        if(i == 3){
          answer = "YES";
          break;
        }
        if(index == 0 || index == tempCombi.size()){
          if(X < 0){
            answer = "NO";
            break;
          }
          tempCombi = combi;
          X --;
        }
        else{
          int n = tempCombi.size()-index;
          vector<int> newCombi(n);
          for(int j = 0; j < n; j++){
            newCombi[j] = tempCombi[index + j];
          }
          if(X > 0){
            newCombi = concat(newCombi, combi);
            X--;
          }
          if(X > 0){
            newCombi = concat(newCombi, combi);
            X--;
          }
          tempCombi = newCombi;
        }
      }
    }

    // write output file
    output << "Case #" << std::setprecision(7) << fixed << k+1 << ": " << answer << endl;
  }
  return 0;
}