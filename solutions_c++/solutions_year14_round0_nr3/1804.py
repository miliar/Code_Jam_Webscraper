#include <algorithm>

#include <iostream>
#include <cassert>
#include <vector>
using namespace std;

void print(vector<char> boards, int R, int C, int i, int j) {
  //cout << "Board = " << endl;
      for (int r=0;r<R;r++) {
	for (int c=0;c<C;c++) {
	  if ((r==i)&&(c==j)) cout << "c";
	  else cout << boards[r*C+c];
	}
	cout << endl;
      } 
}

bool valid(int i, int j, int R, int C) {
  if (i<0) return false;
  if (j<0) return false;
  if (i>=R) return false;
  if (j>=C) return false;
  return true;
}

int count_mines(int i, int j,vector<char> &visited, int R, int C) {
  int c = 0;
  for (int l1=-1;l1<2;l1++) {
    for (int l2=-1;l2<2;l2++) {
      if ((l1!=0)||(l2!=0)) {
	if (valid(i+l1,j+l2,R,C)) {
	  if (visited[(i+l1)*C+j+l2]=='*') c++;
	}
      }
    }
  }
  return c;
}

bool dfs(int i,int j, vector<char> &visited, int R, int C) {
  if (visited[i*C+j]=='.') {
    int k = count_mines(i,j,visited,R,C);
    visited[i*C+j]=(char)('0'+k);
    if (k > 0) {
      visited[i*C+j]=(char)('0'+k);
    } else {
      
      for (int l1=-1;l1<2;l1++) {
	for (int l2=-1;l2<2;l2++) {
	  if (valid(i+l1,j+l2,R,C)) {
	    dfs(i+l1,j+l2,visited,R,C);
	  }
	}
      }
    }
  }
}
 
// No dots
bool found(vector<char> &visited) {
  for (int i=0;i<visited.size();i++) {
    if (visited[i]=='.') return false;
  }
  return true;
}


int main() {
  
  int n;
  cin >> n;
  for (int i=1;i<=n;i++) {
    cout << "Case #"<<i<<":" << endl;
    int R, C, M;
    cin >> R;
    cin >> C;
    cin >> M;
    assert(M<R*C);

    vector<char> boards;
    boards.resize(R*C,'.');
    for (int j=0;j<M;j++) {
      boards[j] = '*';
    }
    //int count = 0;
    bool found_it = false;
    do {
      //print(boards,R,C,0,0);
      for (int l1=0;l1<R;l1++) {
	if (found_it) break;
	for (int l2=0;l2<C;l2++) {
	  vector<char> visited;
	  visited=boards;
	  dfs(l1,l2,visited,R,C);
	  if (found(visited)) {
	    print(boards,R,C,l1,l2);
	    found_it=true;
	    break;
	  }
	}
      }
      if (found_it) break;
      
      //count++;
    } while (next_permutation(boards.begin(),boards.end()) && (!found_it));
    if (!found_it) {
      cout << "Impossible" << endl;
    }
    //cout << count << endl;
  }
  
}

    

