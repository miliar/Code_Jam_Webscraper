#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>

using namespace std;

const int MAXN = 20;

string eil[MAXN];
int kur[MAXN];

int maxsofar = 0, comb = 0;

int kiek(vector<int> list){
	vector<string> tree;
	tree.clear();
	tree.push_back("TUSCIA_EILUTE");
	
	for(int i = 0; i < list.size(); i++){
		//~ cout << eil[list[i]] << endl;
		string s = "";
		for(int j = 0; j < eil[list[i]].size(); j++){
			s += eil[list[i]][j];
			//~ cout << s << endl;
			tree.push_back(s);
			}
		}
	
	sort(tree.begin(), tree.end());
	vector<string>::iterator it;
  it = unique (tree.begin(), tree.end());
  tree.resize( distance(tree.begin(),it) );
	
	//~ for(int i = 0; i < tree.size(); i++)
		//~ cout << tree[i] << endl;
	//~ 
	
  //~ cout << tree.size() << endl;
  
	return tree.size();
	}

void check(int n, int ser){
	int serveriai[MAXN];
	fill(serveriai, serveriai + ser, 0);
	for(int i = 0; i < n; i++)
		serveriai[kur[i]]++;
	
	for(int i = 0; i < ser; i++)
		if(serveriai[i] == 0)
			return;
	//~ cout << "ram8nas" << endl;
	int total = 0;
	for(int i = 0; i < ser; i++){
		vector<int> list;
		list.clear();
		
		for(int j = 0; j < n; j++)
			if(kur[j] == i)
				list.push_back(j);
				
		total += kiek(list);
		}
	
	//~ if(total == 11){
		//~ for(int j = 0; j < n; j++)
			//~ cout << kur[j] << " "; 
			//~ cout << endl;; 
		//~ 
		//~ }
	
	if(total == maxsofar)
		comb++;
	if(total > maxsofar)
		maxsofar = total, comb = 1;
	}

void gen(int x, int ser, int n){
	if(x >= n){
		check(n, ser);
		return;
		}
		
	for(int i = 0; i < ser; i++)
		kur[x] = i, gen(x+1, ser, n);
	}

void solve(int test){
	int n, ser;
	scanf("%d%d", &n, &ser);
	
	for(int j = 0; j < n; j++)
		cin >> eil[j];
	
	maxsofar = 0, comb = 0;
	gen(0, ser, n);
	
	
	printf("Case #%d: %d %d\n", test, maxsofar, comb);
	}

int main(){	
	int testcases;
	scanf("%d", &testcases);
	
	for(int test = 0; test < testcases; test++)
		solve(test+1);
	
	return 0;
}
