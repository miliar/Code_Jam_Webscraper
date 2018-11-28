#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

struct str{
	int size;
	int left;
};

const int SZ = 10010;
int a[SZ];

str b[SZ];

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int n, x;
		cin>>n>>x;
		for(int i=0; i<n; i++) cin>>a[i];
		sort(&a[0],&a[n]);
		for(int i=0; i<SZ; i++){ b[i].size = x; b[i].left=2; }
		for(int i=n-1; i>=0; i--){
			for(int j=0; j<n; j++){
				if(b[j].left>0 && b[j].size>=a[i]){
					b[j].size-=a[i];
					b[j].left--;
					break;
				}
			}
		}
		int rez = 0;
		for(int i=0; i<SZ; i++){
			if(b[i].left<2) rez++;
		}
		cout<<"Case #"<<testnum+1<<": "<<rez<<endl;
	}
	return 0;
}
