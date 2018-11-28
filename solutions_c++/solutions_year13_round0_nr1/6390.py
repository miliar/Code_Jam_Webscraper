#include <iostream>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

bool solve(vector<char> v_c)
{
  char l_w = 'T';
  char sign = 'T';
  int ctr = 0;
  vector<char>::iterator itr = v_c.begin();
  while(itr != v_c.end()) {
    if((l_w == 'T' && *itr != '.' && (sign == 'T' || sign == *itr)) || (l_w == *itr && l_w != '.') || *itr == 'T') {
      l_w = *itr;
      if(l_w == 'X' || l_w == 'O') {
	sign = l_w;
      }
    } else {
      return false;
    }
    ctr++;
    itr++;
  }

  return true;
}

int main(void)
{
  int d_size;
  int t_size;
  bool flag;
  bool has_dot;
  string t_str;
  vector<string> v_str;
  vector<string> v_tmp;
  vector<char> v_char;

  cin >> d_size;

  while(cin >> t_str) {
    v_str.push_back(t_str);
  }

  t_size = v_str.size() / d_size;

  // -----

  for(int i = 0; i < d_size; i++) {
    v_tmp.clear();
    flag = true;

    cout << "Case #" << i + 1 << ": ";

    for(int j = 0; j < t_size; j++) {
      v_tmp.push_back(v_str[i * t_size + j]);
    }
    
    /* solve */
    // search 1
    v_char.clear();
    for(int j = 0; j < t_size; j++) {
      v_char.push_back(v_tmp[j][j]);
    }
    if(solve(v_char)) {
      flag = false;
    }

    if(flag) {
      // search 2
      v_char.clear();
      for(int j = 0; j < t_size; j++) {
	v_char.push_back(v_tmp[j][t_size - 1 - j]);
      }
      if(solve(v_char)) {
	flag = false;
      }
    }

    if(flag) {
      // search 3
      for(int j = 0; j < t_size; j++) {
	v_char.clear();
	for(int k = 0; k < t_size; k++) {
	  v_char.push_back(v_tmp[j][k]);
	}
	if(solve(v_char)) {
	  flag = false;
	  break;
	}
      }
    }

    if(flag) {
      // search 4
      for(int j = 0; j < t_size; j++) {
	v_char.clear();
	for(int k = 0; k < t_size; k++) {
	  v_char.push_back(v_tmp[k][j]);
	}
	if(solve(v_char)) {
	  flag = false;
	  break;
	}
      }
    }

    if(flag) {
      // check dots
      has_dot = false;
      for(int j = 0; j < t_size; j++) {
	for(int k = 0; k < t_size; k++) {
	  if(v_tmp[j][k] == '.') {
	    has_dot = true;
	    break;
	  }
	  if(has_dot) {
	    break;
	  }
	}
      }
      cout << (has_dot ? "Game has not completed" : "Draw") << endl;
    } else {
      for(int i = 0; i < v_char.size(); i++) {
	if(v_char[i] == 'X' || v_char[i] == 'O') {
	  cout << v_char[i] << " won" << endl;
	  break;
	}
      }
    }
  }

  return 0;
}
