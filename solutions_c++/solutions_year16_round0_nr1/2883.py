#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("my.in");
ofstream fout("my.out");

void foo(){
  int n;
  int f[10];
  int count = 0;

  fin >> n;
  
  if(n==0){
    fout << "INSOMNIA";
    return;
  }

  for(int i=0; i<10; i++)
    f[i] = 1;

  int m = 0, t;

  while(true){
    t = m = m + n;
    while(t>0){
      count += f[t%10];
      f[t%10] = 0;
      t = t/10;
    }
    if(count==10){
      fout << m;
      return;
    }
  }

}
int main(){
  int T;
  fin >> T;
  for(int i=1; i<=T; i++){
    fout << "Case #" << i << ": ";
    foo();
    fout << endl;
  }
}