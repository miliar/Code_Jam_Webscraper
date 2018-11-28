#include <iostream>
#include <string>

using namespace std;

int main(void) {
  unsigned int n_t(0);

  cin >> n_t;

  for(unsigned int n_i(1); n_i <= n_t; ++n_i) {
    unsigned int n_x(0);
    unsigned int n_r(0);
    unsigned int n_c(0);
    string       sz_name;

    cin.ignore();

    cin >> n_x;
    cin >> n_r;
    cin >> n_c;

    if(1 == n_x)
      sz_name = "GABRIEL";
    else if(n_x > 6)
      sz_name = "RICHARD";
    else {
      unsigned int n_cells(n_r * n_c);

      sz_name = "RICHARD";

      if(!(n_cells % n_x) && (n_cells >= n_x)) {
        switch(n_x) {
        case 2: sz_name = "GABRIEL"; break;

        case 3: {
          if((n_r > 1) && (n_c > 1))
            sz_name = "GABRIEL";
        } break;

        case 4: {
          if((n_r > 2) && (n_c > 2))
            sz_name = "GABRIEL";
        } break;

        case 5:
        case 6: {
          if((n_r > 3) && (n_c > 3))
            sz_name = "GABRIEL";
        } break;
        }
      }
    }

    fprintf(stdout, "Case #%u: %s\n", n_i, sz_name.c_str());
  }
  
  return 0;
}
