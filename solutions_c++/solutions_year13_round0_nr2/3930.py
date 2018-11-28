#include<iostream>
using namespace std;

void printCase(int cases, int choice){
  cout << "Case #" << cases << ": "; 
  if(choice == 1){cout << "YES";}
  else{cout<< "NO";}
  cout << endl;
}

bool pawnLeft(int ** pawn, int x, int y){
  for(int i = x; i >=0; --i){
    if(pawn[y][i] > pawn[y][x]){return true;}
  }
  return false;
}


bool pawnRight(int ** pawn, int x, int y, int w){
  for(int i = x; i < w; ++i){
    if(pawn[y][i] > pawn[y][x]){return true;}
  }
  return false;
}


bool pawnUp(int ** pawn, int x, int y){
  for(int i = y; i >=0; --i){
    if(pawn[i][x] > pawn[y][x]){return true;}
  }
  return false;
}

bool pawnDown(int ** pawn, int x, int y, int h){
  for(int i = y; i < h; ++i){
    if(pawn[i][x] > pawn[y][x]){return true;}
  }
  return false;
}

int eval(int ** pawn, int h, int w){
  int i = 0, j = 0, k = 0;
  for(i = 0; i < h; ++i){
    for(j = 0; j < w; ++j){
      if((pawnLeft(pawn,j,i) || pawnRight(pawn,j,i,w)) && (pawnUp(pawn,j,i) || pawnDown(pawn,j,i,h))){
	return 0;
      }
    }
  }
  return 1;
}

int main(){
  int cases = 0, count = 0, i = 0, j = 0;
  cin >> cases;
  count = cases;

  while(count > 0){
    int w = 0, h = 0;
    cin >> h >> w;
    int **pawn;
    pawn = new int*[h];
    for(i = 0; i < h; ++i){
      pawn[i] = new int[w];
    }
    for(i = 0; i < h; ++i){  // read pawn
      for(j = 0; j < w; ++j){
	cin >> pawn[i][j];
      }
    }
    if(h == 1 || w == 1){printCase(cases-count+1, 1);}
    else{
      printCase(cases-count+1, eval(pawn, h, w));
    }
    count--;
    for(i = 0; i < h; ++i){
      delete pawn[i];
    }
    delete pawn;
  }
  
  return 0;
}
