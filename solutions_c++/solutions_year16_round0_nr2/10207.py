#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int twoPow(int x) {
  if(x==0) return 1;
  else return 2*twoPow(x-1);
}

int twoLog(int x) {
  if(x==0) return 0;
  else return 1+twoLog(x/2);
}

int flip(int x,int bits) {
  int up=x%twoPow(bits);
  int down=x-up;
  int ans=down;
  for(int i=1;i<=bits;i++) {
    ans+=(1-up%2)*twoPow(bits-i);
    up/=2;
  }
  return ans;
}

int main() {
  int T;
  ifstream input;
  ofstream output;
  input.open("input.in");
  output.open("output.out");
  input>>T;
  string gamw;
  getline(input,gamw);
  for(int i=0;i<T;i++) {
    string word;
    getline(input,word);
    int S=word.length();
    int powS=twoPow(S);
    int prob=0;
    int A[powS];
    for(int k=0;k<powS;k++) A[k]=0;
    bool B[powS];
    for(int k=0;k<powS;k++) B[k]=false;
    for(int j=0;j<S;j++) {
      if(word[j]=='-') prob+=twoPow(j);
    }
    int tempprob=prob;
    while(tempprob>0) {
      B[tempprob]=true;
      int bitused=twoLog(tempprob);
      for(int k=1;k<=bitused;k++) {
        int flipped=flip(tempprob,k);
        if(A[flipped]==0||A[flipped]>A[tempprob]+1) A[flipped]=A[tempprob]+1;
      }
      int min=0;
      for(int l=1;l<powS;l++) {
        if(A[l]>0&&(!B[l])&&(A[l]<A[min]||A[min]==0)) min=l;
      }
      tempprob=min;
    }
    output<<"Case #"<<i+1<<": "<<A[0]<<endl;
  }

  input.close();
  output.close();

  return 0;
}
