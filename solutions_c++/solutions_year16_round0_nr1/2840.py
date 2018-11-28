#include <iostream>
#include <fstream>
#include <ctime>
#include <string>
#include <cstdlib>
#include <cstring>
#include <map>

using namespace std;

map<int,bool> _map;

void solve(void);
int _solve(int nr);

int main(int argc, char* argv[]){
  solve();
  return 0;
}

#define LINESIZE 2000
ofstream of;

void solve(){

  ifstream fl;
  fl.open("f2.in");
  of.open("f2.out");

  int n, i, nr, res;
  fl >> n;

  //char tmp[LINESIZE];
  //memset(tmp,0,LINESIZE);
  //fl.getline(tmp,LINESIZE);

  for (i = 0; i < n; i++){
    _map.clear();
    fl >> nr;
    res = _solve(nr);
    if (res < 0)
      of << "Case #" << (i+1) << ": INSOMNIA" << endl;
    else
      of << "Case #" << (i+1) << ": " << res << endl;
    //of << "Case #" << (i+1) << ": ";
  }

  fl.close();
  of.close();
}


void print_map(void){
  int i;
  map<int,bool>::iterator it;
  for (i = 0; i < 10; i++){
    it = _map.find(i);
    if (it != _map.end()){
      cout << i << ' ';
    }
    cout << endl;
  }
}

int _solve(int nr){

  if (nr == 0){
    //cout << "INSOMNIA" << endl;
    return -1;
  }

  bool stop;
  map<int,bool>::iterator it;
  int dig, nr_cpy1, nr_cpy2 = nr, m = 2, i, cnt = 0;
  while (true){

    //cnt = cnt + 1;
    //if (cnt > 10)
      //  break;

    stop = true;
    nr_cpy1 = nr_cpy2;
    while (nr_cpy1 > 0){
      dig = nr_cpy1 % 10;
      _map[dig] = true;
      nr_cpy1 = nr_cpy1 / 10;
    }

    //print_map();

    //break;
    //cout << _map << endl;
    //break;

    // check for completion
    for (i = 0; i < 10; i++){
      it = _map.find(i);
      if (it == _map.end()){
	stop = false;
	break;
      }
    }

    if (stop == true)
      return nr_cpy2;
    nr_cpy2 = m * nr;
    m = m + 1;
  }
  return -1;
}
