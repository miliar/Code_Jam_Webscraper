#include <iostream>
#include <fstream>
#include <limits>
#include <cmath>
#include <vector>

using namespace std;

bool isPali(int);
void output(const char*,int*,int);

int main(int argc, char const *argv[])
{
  ifstream file("fsample.txt");
  if(!file.is_open()) return 0;
  int length;
  file>>length;
  int start,end;
  int* res = new int[length];
  for(int i=0;i<length;i++){
    file>>start;
    file>>end;
    int x = ceil(sqrt(start));
    int count =0;
    while(x*x<=end){
      if(isPali(x)){
        if(isPali(x*x)){
          cout<<"x:"<<x<<" x²:"<<x*x<<endl;
          count++;
        }
      }
      x++;
    }
    res[i]=count;
  }
  output("fout.txt",res,length);
}

void output(const char* filename,int* res,int n){
  ofstream file;
  file.open(filename,ios::out);
  for(int i=0;i<n;i++){
    file<<"Case #"<<(i+1)<<": ";
    file<<res[i]<<endl;
  }
  file.close();
}

  

bool isPali(int s){
  int tmp = s;
  int r = 0;
  while(tmp>0){
    int d=tmp%10;
    r=r*10+d;
    tmp=tmp/10;
  }
  return r==s;
}



