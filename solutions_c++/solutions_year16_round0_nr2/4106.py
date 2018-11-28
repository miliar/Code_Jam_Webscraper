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

bool debug=false;

#define DEBUG if (debug) cout

//ostream& operator<<(ostream& o, const Omino& oo) {
//  for (int y=0; y<oo[0].size(); ++y) {
//    for (int x=0; x<oo.size(); ++x) {
//      o << oo[x][y] << " ";
//    }
//    o << endl;
//  }
//
//  return o;
//}

vector<bool> pc;

string int2string(long int i) 
{
  stringstream s;
  s << i;

  return s.str();
}

long int string2int(const string& s)
{
  assert(s.find("@") == string::npos);

  long int i;
  stringstream ss(s);
  ss >> i;

  assert(int2string(i) == s);

  return i;
}

class Node {
public:
  vector<bool> p;
  int n;

  Node(const vector<bool>& bla, int nn): p(bla), n(nn) { trim(); }

  bool isDone() const { return find(p.begin(), p.end(), false) == p.end(); }

  void trim();

  void flip(int i);
};


ostream& operator<<(ostream& o, const Node& n) {
  for (bool b: n.p) {
    o << (b?"+":"-");
  }
  o << " (n: " << n.n << ")";
  return o;
}

void Node::trim() {
  int t = p.size()-1;
  for (; t>=0 && p[t]; --t);
  if (t>=0)
    p.erase(p.begin() + t + 1, p.end());
  else
    p.clear();
}

void Node::flip(int i)
{
  assert(i<=p.size() && i > 0);
   
  vector<bool> cp = p;
  for (int j=0; j<i; ++j) {
    p[j] = !(cp[i-j-1]);
  }
    
  trim();
}


map<vector<bool>, long int> solved;


long int solve()
{
  set<vector<bool>> visited;

  Node start(pc,0);

  if (debug) cout << "Starting at " << start << endl;

  queue<Node> nodes;
  nodes.push(start);

  while (!nodes.empty()) {
    Node n = nodes.front();
    nodes.pop();

    if (n.isDone()) { 
      solved[pc] = n.n;
      return n.n;
    }

    if (visited.find(n.p) != visited.end()) continue;

    if (debug) cout << "Expanding " << n << endl;

    //    auto it = solved.find(n.p);
    //    if (it != solved.end()) {
    //      if (debug) cout << "Got answer from cache!" << endl;
    //      return n.n + it->second;
    //    }

    visited.insert(n.p);

    for (size_t i=1; i<=n.p.size(); ++i) {
      Node n2 = n;
      n2.n++;
      n2.flip(i);

      if (debug) cout << "  Openning " << n2 << endl;


      nodes.push(n2);
    }
  }

  assert(false);

  return 0;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    string NSTR;
    i >> NSTR;
    pc.clear();
    for (int c=0; c<NSTR.size(); ++c) {
      assert(NSTR[c] == '-' || NSTR[c] == '+');
      pc.push_back(NSTR[c]=='-'?false:true);
    }

    long int a = solve();
    cout << "Case #" << c+1 << ": " << a << endl;
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

  readFile(filei);

  return 0;
}
