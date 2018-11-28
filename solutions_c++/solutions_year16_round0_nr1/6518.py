#include <iostream>
#include <iomanip>
#include <fstream>
#include <set>

using namespace std;

int main()
{
  long int name, eman;
  int i, t, c, digit, counter;
  const int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  set<int>::iterator it;
  ifstream fin;
  ofstream fout;
  
  fin.open("input.txt");
  fout.open("output.txt");
  fin >> t;
  long int n[t];
  for (c = 0; c < t; ++c) {
    fin >> n[c];
    if (n[c] == 0) {
      cout << "Case #" << c + 1 << ": INSOMNIA" << endl;
      fout << "Case #" << c + 1 << ": INSOMNIA" << endl;
    }
    else {
      set<int> box (arr, arr + 10);
      name = 0;
      counter = 10;
      while (counter > 0) {
	name += n[c];
	eman = name;
	while (eman > 0) {
	  digit = eman % 10;
	  it = box.end();
	  if (box.find(digit) != it) {
	    box.erase(box.find(digit));
	    counter--;
	  }
	  eman /= 10;
	}
	if (counter == 0) {
	  cout << "Case #" << c + 1 << ": " << name << endl;
	  fout << "Case #" << c + 1 << ": " << name << endl;
	}
      }
    }
  }
  fin.close();
  fout.close();
  return 0;
}
