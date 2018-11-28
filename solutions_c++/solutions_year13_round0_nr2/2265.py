#include<stdlib.h>
#include<stdio.h>
#include<set>
#include<algorithm>
#include<vector>

using namespace std;

typedef struct{
  int height;
  int width;
  int grass;
}square;

const int MAX = 100;
int lawn[MAX][MAX];
int number;
bool result, ok;
int test_case;
int width;
int height;
square mysquare;
int grass;
int height_number, width_number;
set<int> rows[MAX];
set<int> columns[MAX];
set<int>::iterator iter;

struct comparator{
  bool operator() (const square& lhs, const square& rhs){
    if(lhs.grass == rhs.grass){
      if(lhs.height == rhs.height){
	return lhs.width<rhs.width;
      }
      else {
	return lhs.height<rhs.height;
      }
    }
    else {
      return lhs.grass<rhs.grass;
    }
  }
};

set<square, comparator> myset;
set<square, comparator>::iterator it;

int load(){
  scanf("%d", &height_number);
  scanf("%d", &width_number);
  for(int i=0; i<height_number; ++i){
    for(int j=0; j<width_number; ++j){
      scanf("%d", &lawn[i][j]);
      rows[i].insert(j);
      columns[j].insert(i);
      mysquare.grass = lawn[i][j];
      mysquare.height = i;
      mysquare.width = j;
      myset.insert(mysquare);
    }
  }
  return 0;
}

int clear_all(){
  myset.clear();
  for(int i=0; i<height_number; ++i){
    rows[i].clear();
  }
  for(int j=0; j<width_number; ++j){
    columns[j].clear();
  }
  return 0;
}

int delete_elements(bool ok){
  if(ok){
    for(iter=rows[height].begin(); iter!=rows[height].end(); ++iter){
      columns[*iter].erase(height);
      mysquare.grass = grass;
      mysquare.height = height;
      mysquare.width = *iter;
      myset.erase(mysquare);
    }
    rows[height].clear();
  }
  else{
    for(iter=columns[width].begin(); iter!=columns[width].end(); ++iter){
      rows[*iter].erase(width);
      mysquare.grass = grass;
      mysquare.height = *iter;
      mysquare.width = width;
      myset.erase(mysquare);
    }
    columns[width].clear();
  }
  return 0;
}

int main(){
  scanf("%d\n", &number);
  for(int i=0; i<number; ++i){
    test_case = i+1;
    load();
    result = true;
    while(!myset.empty()){
      it = myset.begin();
      grass = (*it).grass;
      height = (*it).height;
      width = (*it).width;
      ok = true;
      for(iter=rows[height].begin(); iter!=rows[height].end(); ++iter){
	int j = *iter;
	if(lawn[height][j] != grass){
	  ok = false;
	  break;
	}
      }
      if(!ok){
	for(iter=columns[width].begin(); iter!=columns[width].end(); ++iter){
	  int i = *iter;
	  if(lawn[i][width] != grass){
	    result = false;
	    break;
	  }
	}
      }
      if(!result){
	break;
      }
      delete_elements(ok);
    }
    clear_all();
    printf("Case #%d: ", test_case);
    printf("%s\n", (result)?"YES":"NO");
  }
  return 0;
}
