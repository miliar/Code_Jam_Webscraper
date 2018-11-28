#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <assert.h>
#include <queue>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

bool officialprint=false;


typedef vector<vector<bool> > Omino;

ostream& operator<<(ostream& o, const Omino& oo) {
  for (int y=0; y<oo[0].size(); ++y) {
    for (int x=0; x<oo.size(); ++x) {
      o << oo[x][y] << " ";
    }
    o << endl;
  }

  return o;
}



void allRotations(set<Omino>& allRot, Omino o)
{
  //cout << "all rotations " << endl << o << endl;

  for (int rotation=0; rotation<3; ++rotation) {
    int X = o.size();
    assert(X!=0);
    int Y = o[0].size();

    Omino out(Y, vector<bool>(X, false));

    for (int xx=0; xx<X; ++xx)
      for (int yy=0; yy<Y; ++yy) {
        if (o[xx][yy]) { 
          out[Y-yy-1][X-xx-1] = true;
        }
      }

    //cout << "  yes: " << endl << out << endl;

    allRot.insert(out);
    o = out;
  }
}

Omino flip(const Omino& o, bool flipX)
{
  int x = o.size();
  assert(x!=0);
  int y = o[0].size();

  Omino out(x, vector<bool>(y, false));
  for (int xx=0; xx<x; ++xx)
    for (int yy=0; yy<y; ++yy) {
      int xxx = (flipX?x-xx-1:xx);
      int yyy = (flipX?yy:y-yy-1);

      if (o[xx][yy]) out[xxx][yyy]=true;
    }
  return out;
}

Omino board;


int X,R,C;

void rotateAndFlip(set<Omino>& allRotFlip, const Omino& o)
{
  vector<Omino> flips;

  allRotFlip.clear();
  allRotations(allRotFlip, o);
  
  for (const Omino& o: allRotFlip) {
    flips.push_back(flip(o, false));
    flips.push_back(flip(o, true));
  }

  allRotFlip.insert(flips.begin(), flips.end());
  // all.erase(std::unique(all.begin(), all.end()), all.end());
}

void getAllOmino(set<Omino>& all, int s)
{
  if (s==2) {
    Omino o1;
    vector<bool> age(2, true);
    o1.push_back(age);
    all.insert(o1);
  }
  
  if (s==3) {
    Omino o2;
    vector<bool> age(2, true);
    vector<bool> age2;
    age2.push_back(true);
    age2.push_back(false);
    o2.push_back(age);
    o2.push_back(age2);

    all.insert(o2);

    //    Omino o22;
    //    o22.push_back(age2);
    //    o22.push_back(age);
    //    all.insert(o22);

    Omino o3;
    vector<bool> age3(3, true);
    o3.push_back(age3);

    all.insert(o3);
  }

  if (s == 4) {
    Omino o4;
    vector<bool> age(2, true);
    o4.push_back(age);
    o4.push_back(age);
    all.insert(o4);

    Omino o5;
    vector<bool> age2(1, true);
    age2.push_back(false);
    o5.push_back(age);
    o5.push_back(age2);
    o5.push_back(age2);
    all.insert(o5);

    Omino o6;
    o6.push_back(age2);
    o6.push_back(age);
    o6.push_back(age2);
    all.insert(o6);

    Omino o7;
    o7.push_back(age2);
    o7.push_back(age);
    vector<bool> age3(1, false);
    age3.push_back(true);
    o7.push_back(age3);
    all.insert(o7);

    Omino o8;
    o8.resize(1, vector<bool>(4, true));
    all.insert(o8);
  }
}

bool fits(const Omino& o, const Omino& board, int x, int y)
{
  //cout << "x: " << x << " y: " << y << endl;

  for (int xx=0; xx<o.size(); ++xx)
    for (int yy=0; yy<o[0].size(); ++yy) {
      assert(xx < o.size());
      assert(yy < o[xx].size());
      assert(x+xx < board.size());
      assert(y+yy < board[0].size());
      //cout << "xx: " << xx << " yy: " << yy << endl;
      if (o[xx][yy] && board[x+xx][y+yy]) return false;
    }

  return true;
}

void print(const Omino& o, Omino& board, int x, int y)
{
  for (int xx=0; xx<o.size() && fits; ++xx)
    for (int yy=0; yy<o[0].size() && fits; ++yy) {
      board[x+xx][y+yy] = board[x+xx][y+yy] || o[xx][yy];
    }
}

bool finishSolve_(const set<Omino>& all, const Omino& board)
{
  //cout << "FINISH SOLVE " << endl;
  //cout << board << endl << endl;


  bool allDone=true;
  for (int x=0; x<R&&allDone; ++x)
    for (int y=0; y<C&&allDone; ++y)
      allDone &= board[x][y];

  if (allDone) return true;

  for (const Omino& o: all) {
    for (int x=0; x<R-int(o.size())+1; ++x)
      for (int y=0; y<C-int(o[0].size())+1; ++y) {
        bool fit=fits(o, board, x, y);
    
        if (fit) {
          Omino board2 = board;

          print(o, board2, x, y);

          if (finishSolve_(all, board2)) return true;
        }
      }
  }
  return false;
}


bool solve_(const Omino odun, const set<Omino>& all, const Omino& board)
{
  //cout << "--------------------------------" << endl;
  //cout << "SOLVE" << endl;
  //cout << " Board: " << endl << board << endl << endl;

  //  cout << "R: " << R << " o.size(); " << o.size() << " : " << R-o.size()+1 << endl;
  //  cout << "C: " << C << " o[0].size(); " << o[0].size() << " : " << C-o[0].size()+1 << endl;

  set<Omino> allRots;
  rotateAndFlip(allRots, odun);

  for (const Omino& o: allRots) {
    //cout << " Omino: " << endl << o << endl;

    for (int x=0; x<R-int(o.size())+1; ++x)
      for (int y=0; y<C-int(o[0].size())+1; ++y) {
        bool fit=fits(o, board, x, y);
        
        if (!fit) continue;
        
        //cout << "X: " << x << "/" << R-int(o.size())+1 << endl;
        //cout << "Y: " << y << "/" << C-int(o[0].size())+1 << endl;
        
        Omino board2=board;
        
        print(o, board2, x, y);
        if (finishSolve_(all, board2)) return true;
      }
    }

  return false;
}


bool solve()
{
  if (X == 1) return true;

  board.clear();
  board.resize(R, vector<bool>(C, false));

  //cout << "Initial board: " << endl << board << endl;

  set<Omino> allNonRotated;
  getAllOmino(allNonRotated, X);

  set<Omino> all, tmp;
  for (const Omino& o: allNonRotated) {
    all.insert(o);
    rotateAndFlip(tmp, o);
    all.insert(tmp.begin(), tmp.end());
  }

  //  if (!officialprint) cout << "All omino: "<< all.size() << endl;

  //  for (const Omino& o: all) {
  //    cout << o << endl;
  //  }

  for (const Omino& o: all) {
    if (!solve_(o, all, board)) return false;
  }


  return true;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;
  
  //  if (!officialprint)  cout << "Number of cases: " << numCases << endl;

  for (int c=0; c<numCases; ++c) {
    i >> X;
    i >> R;
    i >> C;

    //    cout << "X: " << X << " R: " << R << " C: " << C << endl;

    bool answer = solve();
    cout << "Case #" << c+1 << ": " << (answer?"GABRIEL":"RICHARD") << endl;
  }

  return true;
}


int main(int argv, char* argc[])
{
  if (argv < 2) {
    cout << "Usage " << argc[0] << " <inputFile>" << endl;
    exit(1);
  }

  ifstream filei(argc[1]);

  if (!readFile(filei)) {
    cout << "Couldn't parse file " << argc[1] << endl;
    exit(1);
  }

  //    for (long int d=0; d<100; ++d) {
  //      for (long int b=0; b<100; ++b) {
  //        cout << "d: " << d << " b: " << b << endl;
  //
  //        long int ff = f(d,b);
  //        long int hh = h(d,b);
  //        
  //        cout << "f: " << ff << " h: " << hh << endl;
  //
  //        assert(ff == hh);
  //
  //
  //        cout << setw(4) << h(d,b) << " ";
  //      }
  //      cout << endl;
  //    }

  //  cout << "********************" << endl;
  //
  //  cout << "h(5,2) = " << h(5,2) << endl;
  //
  //  cout << "********************" << endl;
  //
  //  cout << "h(5,3) = " << h(5,3) << endl;

  return 0;
}
