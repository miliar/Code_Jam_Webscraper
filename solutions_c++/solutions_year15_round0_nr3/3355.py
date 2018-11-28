//
// 0 = 1
// 1 = i
// 2 = j
// 3 = k
// 
// Easy way to represent quaternions?
// 
// Observation #1:
// if a*b =c, and a and c are known, then b is known.
//  --- Look at each column for the quarterion table to tell you what 
//      b must.
//
// Observation 
// pair <sign, val>
#include <iostream>
#include <string>
#include <cassert>
#include <vector>
using namespace std;

int lookup(char c) {
  switch (c) {
   case  '1' : return 0;
   case 'i' : return 1;
   case 'j' : return 2;
   case 'k' : return 3;
  default: cout << "ERROR" << endl;
  }
}

pair<int,int> calc(int i, int j, vector<vector< pair<int,int> > > &quart, string &LS) 
{
    pair<int,int> t1;
    t1 = make_pair(1,lookup(LS[i]));
    for (int k=i+1;k<=j;k++) {
      pair<int,int> t2;
      t2 = quart[t1.second][lookup(LS[k])];
      t1=make_pair(t1.first*t2.first,t2.second);
    }
    return t1;
}

void build_table(vector<pair<int,int> > & partials, vector<vector<pair<int,int> > > &quart, string& L) {
  
  partials.push_back(make_pair(1,lookup(L[0])));
  for (int i=1;i<L.length();i++) {
    pair<int,int> temp =partials[i-1];
    int z = lookup(L[i]);
    pair<int,int> t1 = quart[temp.second][z];
    partials.push_back(make_pair(temp.first*t1.first,t1.second));
  }
}

void build_rev_table(vector<pair<int,int> > & rev_partials, vector<vector<pair<int,int> > > &quart, string& L) {
  rev_partials.resize(L.length());
  rev_partials[L.length()-1] = make_pair(1,lookup(L[L.length()-1]));
  for (int i=L.length()-2;i>=0;i--) {
    pair<int,int> temp =rev_partials[i+1];
    int z = lookup(L[i]);
    pair<int,int> t1 = quart[z][temp.second];
    rev_partials[i]=make_pair(temp.first*t1.first,t1.second);
  }
}

// Calculates the product from L[i..j] using the partials array.
// note that L[0..j] =c is known.
// Similarly, L[0..i-1] =a is known.
// Hence, 
pair<int,int> quart_calc(int i, int j, vector<vector< pair<int,int> > > &quart, vector<pair<int,int> > &partials) {
  if (i==0) return partials[j];

  

  pair<int,int> t1 = partials[i-1];
  pair<int,int> t2 = partials[j];
 
  int second=-1;
  for (int i=0;i<4;i++) {
    if (quart[t1.second][i].second == t2.second) {
      second = i;
      break;
    }
  }
  assert(second!=-1);

  pair<int,int> t3 = quart[t1.second][second];
  if (t1.first*t3.first !=t2.first) {
    return make_pair(-1,second);
  } else {
    return make_pair(1,second);
  }
}


  
  
		    

// Does there exist a way to break up abc = L^X so that  
bool ijk_possible(vector<vector< pair<int,int> > > &quart, string &L, int X) {

  // Observation:
  // if there exists a way to break up L^X into abc, where a gives us i
  // b gives us j, and c gives us k, then 
  // a must be L^u followed by the m characters of L.
  // Notice that L^u is always either 1 or -1.

  // Then, b is either 
  // i.) the next L-m characters of L, followed by z copies of L (1 or -1), followed by 
  //     the first y characters (could be 0)
  // ii.) The next q characters of L.
  //
  // iii.) c is the final r characters of L followed by L^

  string LS;
  for (int i=0;i<X;i++) {
    LS = LS+L;
  }
  assert(LS.length() == X*L.length());
  vector<pair<int,int> > partials; 
  vector<pair<int,int> > rev_partials; 
  build_table(partials,quart,LS);
  build_rev_table(rev_partials,quart,LS);
  
  for (int i=0;i<LS.length();i++) {
    pair<int,int> t1;
    t1 = partials[i]; // The string from 0..i
    if ((t1.first==1)&&(t1.second == 1)) { // +i
      for (int j=i+1;j<LS.length();j++) {
	pair<int,int> t2;
	t2= quart_calc(i+1,j,quart,partials);
	/*
	pair<int,int> t3;
	t3 = calc(i+1,j,quart,LS);
	if (!((t2.first==t3.first) && (t2.second == t3.second))) {
	  cout << i << "*** " << j << endl;
	  cout << t2.first << " " << t2.second << endl;
	  cout << t3.first << " " << t3.second << endl;
	}
	*/
	if ((t2.first==1)&&(t2.second==2)) { // j
	  if (j+1<LS.length()) {
	    pair<int,int> t3;
	    t3 = rev_partials[j+1];
	    if ((t3.first==1)&&(t3.second==3)) { // k
	      return true;
	    }
	  }
	}
      }
    }
  }
  return false;
}

/*
	  if (rev_partia
  // Try all possible 
  if (X%2 == 0) { // X is even
    for (int i=0;i<L.length();i++) {
      pair<int,int> t1;
      t1 = partials[i];
      if (t1.first == 1) && (t1.second == 1) { // Found an i
	  if 
    
using namespace std;
*/
int main() {

  vector<vector<pair<int,int> > > table;
  table.resize(4);
  for (int i=0;i<4;i++) {
    table[i].resize(4);
  }
  table[0][0] = make_pair(1,0);
  table[0][1] = make_pair(1,1);
  table[0][2] = make_pair(1,2);
  table[0][3] = make_pair(1,3);
  table[1][0] = make_pair(1,1);
  table[1][1] = make_pair(-1,0);
  table[1][2] = make_pair(1,3);
  table[1][3] = make_pair(-1,2);
  table[2][0] = make_pair(1,2);
  table[2][1] = make_pair(-1,3);
  table[2][2] = make_pair(-1,0);
  table[2][3] = make_pair(1,1);
  table[3][0] = make_pair(1,3);
  table[3][1] = make_pair(1,2);
  table[3][2] = make_pair(-1,1);
  table[3][3] = make_pair(-1,0);



  string line;
  int T;
  cin >> T;
  for (int I=0;I<T;I++) {

    int L,X;
    cin >> L;
    cin >> X;
    getline(cin,line);
    getline(cin,line);
    assert(line.length()==L);
    if (ijk_possible(table,line,X)) {
      cout << "Case #"<<I+1<<": "<< "YES" << endl;
    } else {
      cout << "Case #"<<I+1<<": "<< "NO" << endl;
    }
  }
}
