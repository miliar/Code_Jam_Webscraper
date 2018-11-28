#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;

int main() {
	int n;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in>>n;
	string st[n];
	for(int i=0;i<n;i++)
	{
		in>>st[i];
	}
	for(int i=0;i<n;i++){
		int change=0;
		int last=-1;
		for (int j=0;j<st[i].length();j++){
			int current; 
			if (st[i][j]=='+') current=1;
			else current=0;
			if(last!=current){
				change++;
				last=current;
			} 
			
		}
		if (last==1) change--;
		out<<"Case #"<<i+1<<": "<<change<<endl;
	}
	
	
	return 0;
}
