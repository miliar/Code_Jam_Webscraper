#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

static int a_table[4][4] = {
  {1,  2,  3,  4},
  {2, -1,  4, -3},
  {3, -4, -1,  2},
  {4,  3, -2, -1}
};

static int transform(int n_value) {
  switch(n_value > 0 ? n_value : -n_value) {
  case '1': return 1;
  case 'i': return 2;
  case 'j': return 3;
  case 'k': return 4;
  }
}

static int multiply(int n_v1,
		    int n_v2) {
  int n_sign(1);

  if(n_v1 < 0) {
    n_sign = -1;
    n_v1   = -n_v1;
  }

  if(n_v2 < 0) {
    n_sign *= -1;
    n_v2   = -n_v2;
  }

  return a_table[n_v1 - 1][n_v2 - 1] * n_sign;
}

static string::iterator get_next(string::iterator i_i) {
  return ++i_i;
}

static bool find_k(string& sz_total) {
  int n_result(1);

  for(string::iterator i_i(sz_total.begin()); i_i != sz_total.end(); ++i_i) {
    int n_value(transform(*i_i));

    n_result = multiply(n_result, n_value);

    if(4 == n_result) {
      if(get_next(i_i) == sz_total.end())
	return true;
    }
  }
  
  return false;
}

static bool find_j(string& sz_total) {
  int n_result(1);

  for(string::iterator i_i(sz_total.begin()); i_i != sz_total.end(); ++i_i) {
    int n_value(transform(*i_i));

    n_result = multiply(n_result, n_value);

    if(3 == n_result) {
      string sz_partial(get_next(i_i), sz_total.end());
      
      if(find_k(sz_partial))
	return true;
    }
  }
  
  return false;
}

int main(void) {
  unsigned int n_t(0);

  cin >> n_t;
  
  for(unsigned int n_i(1); n_i <= n_t; ++n_i) {
    unsigned int n_l(0);
    unsigned int n_x(0);
    string       sz_line;
    string       sz_total;
    string       sz_result("NO");
    int          n_result(1);

    cin.ignore();

    cin >> n_l;
    cin >> n_x;

    cin.ignore();

    cin >> sz_line;

    sz_line = sz_line.substr(0, n_l);

    for(unsigned int n_j(0); n_j < n_x; ++n_j)
      sz_total += sz_line;

    for(string::iterator i_i(sz_total.begin()); i_i != sz_total.end(); ++i_i) {
      int n_value(transform(*i_i));

      n_result = multiply(n_result, n_value);
      
      if(2 == n_result) {
	string sz_partial(get_next(i_i), sz_total.end());
	
	if(find_j(sz_partial)) {
	  sz_result = "YES";
	  break;
	}
      }
    }

    fprintf(stdout, "Case #%u: %s\n", n_i, sz_result.c_str());
  }
  
  return 0;
}
