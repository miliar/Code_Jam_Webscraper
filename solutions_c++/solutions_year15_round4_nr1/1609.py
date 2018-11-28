#include <iostream>
#include <random>
#include <time.h>
#include <limits>
#include <vector>
#include <sstream>
using namespace std;


class Instance{
public:
  void read();
  void write();

  void compute();
private:
 long long _n;
 vector<long long> out;

 vector<int> R;
 vector<int> C;

 vector< vector<int > > grid;
};


int pos(int c, int r, int nR) {
  return (c*nR +r);
}


void Instance::read()
{
  cin >> _n;

  for (long long i = 0; i < _n; ++i) {
    long long in;
    cin >> in;
    R.push_back(in);
    cin >> in;
    C.push_back(in);

    vector<int > ngrid;


    grid.push_back(ngrid);



    for (int j=0; j < R[i]*C[i]; ++j) {
      grid[i].push_back(0);
    }


    for (int rows = 0; rows < R[i]; ++ rows) {
      string s;
      cin >> s;

      for (int p = 0; p < C[i]; ++p) {



        if (s[p] == '.') {
          grid[i][pos(p,rows,R[i])] =0;
        }
        if (s[p] == '^') {
          grid[i][pos(p,rows,R[i])] =1;
        }
        if (s[p] == '>') {
          grid[i][pos(p,rows,R[i])] =2;
        }
        if (s[p] == 'v') {
          grid[i][pos(p,rows,R[i])] =3;
        }
        if (s[p] == '<') {
          grid[i][pos(p,rows,R[i])] =4;
        }
      }

    }

  }

}


void Instance::write()
{
   for (long long i = 0; i < out.size(); ++i) {
     if (out[i] == -1) {
       cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
     } else {
       cout << "Case #" << i+1 << ": " << out[i]  << endl;
     }
   }

}





void Instance::compute()
{
  for (int i = 0; i < _n; ++i){
    int nR = R[i];
    int nC = C[i];

    vector<int> runter;
    vector<int> hoch;
    vector<int> rechts;
    vector<int> links;
    for (int j = 0; j < nR*nC; ++j) {
      runter.push_back(0);
      hoch.push_back(0);
      rechts.push_back(0);
      links.push_back(0);
    }

    for (int r = 0; r < nR; ++r){
      for (int c = 0; c < nC; ++c) {
        int a = 0;


        if (grid[i][pos(c,r,nR)] != 0) {
          a = 1;
        }

        if (r>0) {
          hoch[pos(c,r,nR)] = hoch[pos(c,r-1,nR)] +a;
        } else {
          hoch[pos(c,r,nR)] = a;
        }
        if (c>0) {
          links[pos(c,r,nR)] = links[pos(c-1,r,nR)] +a;
        } else {
          links[pos(c,r,nR)] = a;
        }

      }
    }


    for (int r = nR-1; r >= 0; --r){
      for (int c = nC-1; c >= 0; --c) {
        int a = 0;


        if (grid[i][pos(c,r,nR)] != 0) {
          a = 1;
        }

        if (r<nR-1) {
          runter[pos(c,r,nR)] = runter[pos(c,r+1,nR)] +a;
        } else {
          runter[pos(c,r,nR)] = a;

        }
        if (c<nC-1) {
          rechts[pos(c,r,nR)] = rechts[pos(c+1,r,nR)] +a;
        } else {
          rechts[pos(c,r,nR)] = a;
        }
      }
    }

  int counter = 0;
  bool possible = true;


    for (int r = 0; r < nR; ++r){
      for (int c = 0; c < nC; ++c) {
         if (grid[i][pos(c,r,nR)] == 0) {
           continue;
         }


         if ( (grid[i][pos(c,r,nR)] == 1) && (hoch[pos(c,r,nR)] > 1)) {
           continue;
         }
         if ( (grid[i][pos(c,r,nR)] == 2) && (rechts[pos(c,r,nR)] > 1)) {
           continue;
         }
         if ( (grid[i][pos(c,r,nR)] == 3) && (runter[pos(c,r,nR)] > 1)) {
           continue;
         }
         if ( (grid[i][pos(c,r,nR)] == 4) && (links[pos(c,r,nR)] > 1)) {
           continue;
         }

         int all = hoch[pos(c,r,nR)] + runter[pos(c,r,nR)] + rechts[pos(c,r,nR)] + links[pos(c,r,nR)];
         if (all == 4) {
           possible = false;
         } else {
           counter ++;
         }
      }
    }

     if (!possible) {
       counter = -1;
     }
    out.push_back(counter);
  }
}


int main(int argc, char** argv){
  Instance I;
  I.read();

 I.compute();
  I.write();
}
