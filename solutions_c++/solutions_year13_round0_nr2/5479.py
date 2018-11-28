#include <iostream>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

struct lawn {
  int *p;
  int width;
  int height;

  lawn(int width, int height) : width(width), height(height) {
    p = new int[width * height];
  }

  ~lawn(){
    delete p;
  }

  int& cell(int x, int y){
    return p[width * y + x];
  }

  bool has_hpath(int h, int y){
    for(int pos = 0; pos < width; ++pos)
      if(cell(pos, y) > h)
        return false;

    return true;
  }

  bool has_vpath(int h, int x){
    for(int pos = 0; pos < height; ++pos)
      if(cell(x, pos) > h)
        return false;

    return true;
  }

  bool has_path(int x, int y){
    int h = cell(x, y);
    return (has_hpath(h, y) || has_vpath(h, x));
  }
};

void run(int icase){
  int width, height;

  cin >> width >> height;
  
  lawn l(width, height);

  for(int x = 0; x < width; ++x)
    for(int y = 0; y < height; ++y){
      int h;
      cin >> h;
      l.cell(x, y) = h;
    }

//  for(int i = 0; i < width; ++i){
//    for(int j = 0; j < height; ++j){
//      cout << l.cell(i, j) << " ";
//    }  
//    cout << endl;
//  }

  for(int x = 0; x < width; ++x)
    for(int y = 0; y < height; ++y){
      if(!l.has_path(x, y)){
        cout << "Case #" << icase << ": NO\n";
        return;
      }
    }

  cout << "Case #" << icase << ": YES\n";

}

int main(){
  int ncases;
  cin >> ncases;
  for(int icase = 0; icase < ncases; ++icase)
    run(icase + 1);

  return 0;
}