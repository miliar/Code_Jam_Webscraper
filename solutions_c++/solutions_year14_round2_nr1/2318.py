#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <cmath>
using namespace std;
struct word{
    int M [110];
    char S [110];
    char E[110];
    int sz;
public:
    void add_M(int M[],int n){
        this->sz = n;
        for(int i = 0;i < n;i++)
            this->M[i] = M[i];
    }
};
struct Data{
    vector<word> S;
public:
    Data(){
        S.clear();
    }
    void add_word(word s){
        S.push_back(s);
    }
    void clear(){
        S.clear();
    }
};
Data Words = Data();
void extract(char s[],int index){
    vector<char> temp1;
    vector<int> temp2;
    char init = s[0];
    int ctr = 0;
    for(int i = 0;i < strlen(s);i++){
        if(init == s[i]){
            ctr++;
        }
        else{
            temp1.push_back(init);
            temp2.push_back(ctr);
            ctr = 1;
            init = s[i];
        }
    }
    temp1.push_back(init);
    temp2.push_back(ctr);
    int A[temp2.size()];char B[temp2.size() + 1];
    for(int i = 0;i < temp2.size();i++){
        A[i] = temp2.at(i);
        B[i] = temp1.at(i);
    }
    B[temp2.size()] = '\0';
    strcpy(Words.S.at(index).E,B);
    Words.S.at(index).add_M(A,temp2.size());
}

int f(){
    int s = 0,ctr;
    for(int i = 0;i < strlen(Words.S.at(0).E);i++){
        ctr = 0;
        for(int j = 0;j < Words.S.size();j++){
            ctr += Words.S.at(j).M[i];
        }
        ctr /= Words.S.size();
        int choice = Words.S.at(0).E[i];
        for(int j = 1;j < Words.S.size();j++){
            if(abs(choice - ctr) > abs(Words.S.at(j).M[i] - ctr))
                choice = Words.S.at(j).M[i];
        }
        for(int j = 0;j < Words.S.size();j++){
            s += abs(choice - Words.S.at(j).M[i]);
        }
    }
    return s;
}
bool g(){
    for(int i = 0;i < Words.S.size();i++){
        extract(Words.S.at(i).S,i);
    }
    char ref[strlen(Words.S.at(0).E)+1];
    strcpy(ref,Words.S.at(0).E);
    for(int i = 1;i < Words.S.size();i++){
        if(strlen(ref) != strlen(Words.S.at(i).E))
            return 0;
        for(int j = 0;j < strlen(ref);j++){
            if(ref[j] != Words.S.at(i).E[j])
                return 0;
        }
    }
    return 1;
}
int main(){
  ofstream fout ("output.out");
  ifstream fin ("A-small-attempt0.in");
  char S[110];
  int T,N;
  fin >> T;
  for(int i = 1;i <= T;i++){
      fin >> N;
      Words.clear();
      while(N-- > 0){
          fin >> S;
          word temp;
          strcpy(temp.S,S);
          Words.add_word(temp);
      }
      if(g() == 0)
          fout << "Case #" << i << ": Fegla Won\n";
      else{
          fout << "Case #" << i << ": " << f() << "\n";
      }
  }
  return 0;
}