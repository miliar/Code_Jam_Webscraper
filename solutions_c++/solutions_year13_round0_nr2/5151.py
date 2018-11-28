#include <iostream>


int tab1[100][100];
int T,N,M;
bool X1[100];
bool Y1[100];
using namespace std;


bool czy_mniejsze_rowne_X(int x,int w) {
      for (int y=0;y<M;y++) {
        if (tab1[x][y] > w) { return false; }        
      }  
      return true;
  
}


bool czy_mniejsze_rowne_Y(int y,int w) {
      for (int x=0;x<N;x++) {
        if (tab1[x][y] > w) { return false; }        
      }  
      return true;  
}

int main(void) {
  cin >> T;
  for (int i=0;i<T;i++) {
    cin >> N;
    cin >> M;
     
    for (int x=0;x<N;x++) {
      for (int y=0;y<M;y++) {
        cin >> tab1[x][y];
      }
    }  
    
    bool ok=true;
    for (int x=0;x<N;x++) {
      for (int y=0;y<M;y++) {
        if (!czy_mniejsze_rowne_X(x,tab1[x][y]) && !czy_mniejsze_rowne_Y(y,tab1[x][y])) 
          ok=false;
      }
    }
    if (ok==true) {
      cout << "Case #" << (i+1) << ": YES" << endl; 
    } else {
      cout << "Case #" << (i+1) << ": NO" << endl; 
    }
    
  }
}