#include <iostream>
#include <fstream>
using namespace std;

void getRowData(ifstream& fin, int* p) {
  int d;

  int row;
  fin >> row;

  for (int i=1; i<=4; ++i) {
    if (i == row)
      fin >> p[3] >> p[2] >> p[1] >> p[0];
    else
      fin >> d >> d >> d >> d;
  }
}

void checkAndSave(ofstream& fout, int* p, int* q) {

  int counter = 0, cardNo = -1;
  for (int i=0; i<4; ++i) {
    for (int j=0; j<4; ++j) {
      if (p[i] == q[j]) {
	cardNo = p[i];
	++counter;
	break;
      }
    }
  }

  if (counter == 0)
    fout << "Volunteer cheated!" << endl;
  else if (counter == 1)
    fout << cardNo << endl;
  else 
    fout << "Bad magician!" << endl;
}

int main(int argc, char* argv[]) {

  if (argc < 3) {
    cout << "Usage: ./magic input output" << endl;
    return -1;
  }

  ifstream fin(argv[1]);
  ofstream fout(argv[2]);

  string dummy;

  int N;
  fin >> N;

  for (int i=0; i<N; ++i) {
    int p[4];
    int q[4];

    getRowData(fin, p);
    getRowData(fin, q);

    fout << "Case #" << i+1 << ": ";
    checkAndSave(fout, p, q);
  }

  fout.close();
  fin.close();

  return 0;
}
