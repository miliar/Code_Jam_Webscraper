#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

void printField(int**,int,int);
int** fieldCopy(int**,int,int);
bool mow(int**,int**,int,int);
bool isValid(int**,int**,int,int);
void output(const char*,int*,int);
void delfield(int**,int);

int counter=0;

int main(int argc, char const *argv[])
{
  ifstream file("sample.txt");
  if(!file.is_open()) return 0;
  int length;
  file>>length;
  int* res = new int[length];
  for(int i=0;i<length;i++){
    int n,m;
    file>>n>>m;
    int **field = new int*[n];
    int **start = new int*[n];
    for(int j=0;j<n;j++){
      field[j] = new int[m];
      start[j] = new int[m];
      for(int k=0;k<m;k++){
        file>>field[j][k];
        start[j][k]=100;
      }
    }
    res[i]=(int)mow(start,field,n,m);
  }
  output("out.txt",res,length);


  return 0;
}

void printField(int** field,int n,int m){
  cout<<"#";
  for(int i=0;i<m;i++){
    cout<<"#####";
  }
  cout<<"#"<<endl;
  for(int i=0;i<n;i++){
    cout<<"#"<<setw(1+m*5)<<"#"<<endl<<"#";
    for(int j=0;j<m;j++){
      cout<<" "<<setw(3)<<field[i][j]<<" ";
    }
    cout<<"#"<<endl;
  }
  cout<<"#"<<setw(1+m*5)<<"#"<<endl;
  cout<<"#";
  for(int i=0;i<m;i++){
    cout<<"#####";
  }
  cout<<"#"<<endl;
}

int** fieldCopy(int** field,int n,int m){
  int** copy = new int*[n];
  for(int i=0;i<n;i++){
    copy[i]=new int[m];
    for(int j=0;j<m;j++){
      copy[i][j]=field[i][j];
    }
  }
  return copy;
}

bool mow(int** field,int** result,int n,int m){
  if(!isValid(field,result,n,m)){
    delfield(field,n);
    return false;
  }
  int maxv=0;
  int imax,jmax;
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(field[i][j]==result[i][j]) continue;
      if(result[i][j]>maxv){
        maxv=result[i][j];
        imax = i;
        jmax = j;
      }
    }
  }
  if(maxv==0) return true;
  int** field2 = fieldCopy(field,n,m);
  for(int i=0;i<n;i++){
    field[i][jmax] =maxv;
  }
  for(int j=0;j<m;j++){
    field2[imax][j]=maxv;
  }
  return mow(field,result,n,m) || mow(field2,result,n,m);

}

bool isValid(int** field,int** result,int n,int m){
  for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
      if(field[i][j]<result[i][j]) return false;
    }
  }
  return true;
}

void delfield(int** field,int n){
  for(int i=0;i<n;i++){
    delete [] field[i];
  }
  delete field;
}

void output(const char* filename,int* res,int n){
  ofstream file;
  file.open(filename,ios::out);
  for(int i=0;i<n;i++){
    file<<"Case #"<<(i+1)<<": ";
    switch(res[i]){
      case 0:
        file<<"NO"<<endl;
        break;
      case 1:
        file<<"YES"<<endl;
        break;
    }
  }
  file.close();
}