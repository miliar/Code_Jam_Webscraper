#include <stdio.h>
#include <vector>
#include <map>
#include <stdlib.h>
#include <string>
#include <set>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

ifstream in( "input.txt" );
ofstream out( "output.txt" );

struct Edge {
  int v1;
  int v2;
  int wMax;
  int wMin;
};

void solveTest()
{
  int N, M, P;
  in >> N >> M >> P;
  vector<Edge> e(M);
  for( int i = 0; i < M; i++ ) {
    in >> e[i].v1 >> e[i].v2 >> e[i].wMin >> e[i].wMax;
    e[i].v1--;
    e[i].v2--;
  }
  vector<int> path(P);
  for( int i = 0; i < path.size(); i++ ) {
    in >> path[i];
    path[i]--;
  }
  vector<int> ww(N, -1);
  ww[e[path[0]].v1] = 0;
  int finV = e[path[path.size() - 1]].v2;

  for( int i = 0; i < path.size(); i++ ) {
    int curV = e[path[i]].v2;
    if( ww[curV] >= 0 ) {
      out << path[i] + 1 << "\n";
      return;
    }
    ww[curV] = ww[e[path[i]].v1] + e[path[i]].wMin;
    vector<int> newW(ww.size());
    for( int j = 0; j < newW.size(); j++ ) {
      if( j != curV ) {
	newW[j] = 1000000000;
      } else {
	newW[j] = ww[j];
      }
    }
    for( int j = 0; j < N; j++ ) {
      for( int k = 0; k < M; k++ ) {
	int v1 = e[k].v1;
	int v2 = e[k].v2;
	if( newW[v2] > newW[v1] + e[k].wMin ) {
	  newW[v2] = newW[v1] + e[k].wMin;
	}
      }
    }
    vector<int> newW2 = ww;
    for( int j = 0; j < newW2.size(); j++ ) {
      if( newW2[j] < 0 ) {
	newW2[j] = 1000000000;
      }
    }
    for( int j = 0; j < N; j++ ) {
      for( int k = 0; k < M; k++ ) {
	int v1 = e[k].v1;
	int v2 = e[k].v2;
	if( newW2[v2] > newW2[v1] + e[k].wMax ) {
	  newW2[v2] = newW2[v1] + e[k].wMax;
	}
      }
    }
    vector<bool> forbidden(N, true);
    for( int j = 0; j < N; j++ ) {
      forbidden[j] = newW2[j] < newW[j];
    }
    vector<bool> vis(N, false);
    vis[curV] = true;
    for( int j = 0; j < N; j++ ) {
      for( int k = 0; k < M; k++ ) {
	int v1 = e[k].v1;
	int v2 = e[k].v2;
	if( vis[v1] && !forbidden[v1] && !forbidden[v2] ) {
	  vis[v2] = true;
	} 
      }
    }
    if( !(vis[finV] && !forbidden[finV]) ) {
      out << (path[i] + 1) << "\n";
      return;
    }
  }
  out << "Looks Good To Me\n";
}

void run()
{
  int tn;
  in >> tn;
  for( int i = 1; i <= tn; i++ ) {
    out << "Case #" << i << ": ";
    solveTest();
  }
}

int main()
{
  run();
  return 0;
}
