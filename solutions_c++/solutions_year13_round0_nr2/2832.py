#include "common.h"

int rows, cols;
int a[200][200];
std::set< int, std::greater<int> > hs;

void Readin() {  // process one case
  fin >> rows >> cols;
  hs.clear();
  forint (r, 0, rows - 1) {
    forint (c, 0, cols - 1) {
      fin >> a[r][c];
      hs.insert(a[r][c]);
    }
  }
}

void Work() {  // process one case
  vector<bool> flags_r(rows, true), flags_c(cols, true);
  foritr (itr, hs) {
    const int h = *itr;
    forint (r, 0, rows - 1) {
      forint (c, 0, cols - 1) {
        if (a[r][c] == h) {
          if (!flags_r[r] && !flags_c[c]) {
            fout << "NO" << endl;
            return;
          }
        }
      }
    }  // for (r, c)

    forint (r, 0, rows - 1) {
      forint (c, 0, cols - 1) {
        if (a[r][c] == h) flags_r[r] = flags_c[c] = false;
      }
    }
  }

  fout << "YES" << endl;
}  // Work()

int main(const int argc, const char** argv) {
  CHECK(argc == 1);
  const string main_filename = SetFile(/*@*/"   B-large        ");

  int num_test;  fin >> num_test;
  CHECK(Eoln(fin));  Readln(fin);
  
  showvar(num_test);
  forint (number, 1, num_test) { 
    fout << "Case #" << number << ": ";
    cerr << "Running on Case #" << number << endl;

    Readin();
    Work();
    //fout << ans << endl;
  }

  if (!SeekEof(fin)) ABORT("Wrong! Not at EOF!");
  fclose(stdin);
  fclose(stdout);

  cerr << "\n\n---------- OUTPUT of " + main_filename + ": ----------" << endl;
  system(("cat " + main_filename + ".out >&2").c_str());
  return 0;
}

