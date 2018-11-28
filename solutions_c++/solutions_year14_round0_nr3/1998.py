#include <fstream>
#include <iostream>
#include <math.h>
using namespace std;

#define BLANK 0
#define MINE 1
#define TOUCH 2
#define PATH 3

int** draw(int x, int y, int size_x, int size_y, int** map, int count, int target){
  int** new_map = new int*[size_x];
  int new_count = count;
  for(int i = 0 ; i < size_x ; i ++){
    new_map[i] = new int[size_y];
    for(int j = 0 ; j < size_y ; j ++){
      new_map[i][j] = map[i][j];
    }
  }

  if(new_map[x][y] != PATH){
    if(new_map[x][y] == MINE) new_count ++;
    new_map[x][y] = PATH;
  }

  if(new_count == target){
    return new_map;
  }
  if(new_count > target){
    for(int i = 0 ; i < size_x ; i ++){
      delete new_map[i];
    }
    delete new_map;
    return NULL;
  }


  if(x - 1 >= 0 && new_map[x - 1][y] == MINE){ new_map[x - 1][y] = BLANK; new_count ++; }
  if(y - 1 >= 0 && new_map[x][y - 1] == MINE){ new_map[x][y - 1] = BLANK; new_count ++; }

  if(x + 1 < size_x && new_map[x + 1][y] == MINE){ new_map[x + 1][y] = BLANK; new_count ++; }
  if(y + 1 < size_y && new_map[x][y + 1] == MINE){ new_map[x][y + 1] = BLANK; new_count ++; }

  if(x + 1 < size_x && y - 1 >= 0 && new_map[x + 1][y - 1] == MINE){ new_map[x + 1][y - 1] = BLANK; new_count ++; }
  if(x - 1 >= 0 && y - 1 >= 0 && new_map[x - 1][y - 1] == MINE){ new_map[x - 1][y - 1] = BLANK; new_count ++; }

  if(y + 1 < size_y && x - 1 >= 0 && new_map[x - 1][y + 1] == MINE){ new_map[x - 1][y + 1] = BLANK; new_count ++; }
  if(y + 1 < size_y && x + 1 < size_x && new_map[x + 1][y + 1] == MINE){ new_map[x + 1][y + 1] = BLANK; new_count ++; }


  if(new_count == target){
    return new_map;
  }

  int** up = NULL;
  int** right = NULL;
  int** down = NULL;
  int** left = NULL;
  int** up_right = NULL;
  int** up_left = NULL;
  int** down_right = NULL;
  int** down_left = NULL;

  if(x + 1 < size_x && new_map[x + 1][y] != PATH)
    right = draw(x + 1, y, size_x, size_y, new_map, new_count, target);
  if(right != NULL)
    return right;

  if(y + 1 < size_y && new_map[x][y + 1] != PATH)
    up = draw(x, y + 1, size_x, size_y, new_map, new_count, target);
  if(up != NULL)
    return up;
  if(x - 1 >= 0 && new_map[x - 1][y] != PATH)
    left = draw(x - 1, y, size_x, size_y, new_map, new_count, target);
  if(left != NULL)
    return left;
  if(y - 1 >= 0 && new_map[x][y - 1] != PATH)
    down = draw(x, y - 1, size_x, size_y, new_map, new_count, target);
  if(down != NULL)
    return down;

  if(x + 1 < size_x && y - 1 >= 0 && new_map[x + 1][y - 1] != PATH)
    down_right = draw(x + 1, y - 1, size_x, size_y, new_map, new_count, target);
  if(down_right != NULL)
    return down_right;
  if(x + 1 < size_x && y + 1 < size_y && new_map[x + 1][y + 1] != PATH)
    up_right = draw(x + 1, y + 1, size_x, size_y, new_map, new_count, target);
  if(up_right != NULL)
    return up_right;
  if(x - 1 >= 0 && y - 1 >= 0 && new_map[x - 1][y - 1] != PATH)
    down_left = draw(x - 1, y - 1, size_x, size_y, new_map, new_count, target);
  if(up_right != NULL)
    return down_left;
  if(x - 1 >= 0 && y + 1 < size_y && new_map[x - 1][y + 1] != PATH)
    up_left = draw(x - 1, y + 1, size_x, size_y, new_map, new_count, target);
  if(up_left != NULL)
    return up_left;

  for(int i = 0 ; i < size_x ; i ++){
    delete new_map[i];
  }
  delete new_map;

  return NULL;
}


int main(){
  fstream file;
  ofstream out;

  int num_cases;
  int x, y, mines;
  int open;
  int** map;

  file.open("input.dat");
  out.open("output.txt");

  file >> num_cases;

  for(int i = 0 ; i < num_cases ; i ++){

    file >> x;
    file >> y;
    file >> mines;

    out << "Case #" << i + 1 << ":" << endl;

    map = new int*[x];
    for(int k = 0 ; k < x ; k ++){
      map[k] = new int[y];
      for(int j = 0 ; j < y ; j ++){
          map[k][j] = MINE;
      }
    }

    map = draw(0, 0, x, y, map, 0, (x * y) - mines);

    if(map != NULL){
      map[0][0] = TOUCH;
      for(int j = 0 ; j < x ; j ++){
        for(int k = 0 ; k < y ; k ++){
          switch(map[j][k]){
            case BLANK:
            case PATH:
              out << "."; break;
            case MINE: out << "*"; break;
            case TOUCH: out << "c"; break;
          }
        }
        out << endl;
      }
    }else{
      out << "Impossible" << endl;
    }

  }

  out.close();

  return 0;
}

