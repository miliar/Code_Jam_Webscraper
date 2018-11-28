#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;

int main()
{
  ifstream fin("A-small-attempt1.in");
  ofstream fout("MagicTrick.out");
  int N, temp, temp1, count=0, ans;
  fin >> N;
  for(int q=0; q<N; q++){
  count=0;
  bool possible[17]={false};
  fin >> temp;
  for(int i=0; i<16; i++){
    fin >> temp1;
    if(4*(temp-1)<=i && i<4*temp){
      possible[temp1]=true;
    }
  }
  fin >> temp;
  for(int i=0; i<16; i++){
    fin >> temp1;
    if(4*(temp-1)<=i && i<4*temp){
      if(possible[temp1]){
        ans=temp1;
        count++;
        //cout << count;
      }
    }
  }
  fout << "Case #" << q+1 << ": ";
  if(count==0){fout << "Volunteer cheated!";}
  else if(count>1){fout << "Bad Magician!";}
  else{fout << ans;}
  fout << endl;
  }
}
