#include <iostream>
#include <queue>  
#include <vector>   
#include <set>
#include <utility>
#include <math.h>       /* atan */
#include <limits>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <string.h>
#include <stdlib.h>
#include <stack>

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
#define foreach(i, n) for (int i = 0; i < (int)(n); i++)
#define PI 3.14159265358979323846 
long double diff = 1e-10;

string number[10]= {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool DFS(vector<int> &number, \
		unordered_map<int, unordered_map<char, int>> &D2C, \
		unordered_map<char, unordered_set<int>> &C2D, \
		unordered_map<char, int> &freq, \
		int remainL){
	if(remainL == 0)
		return true;
	vector<char> remainChar;
	for(auto it = freq.begin(); it!=freq.end(); it++){
		if(it->second>0)
			remainChar.push_back(it->first);
	}
	for(auto item: remainChar){
		for(auto it = C2D[item].begin(); it!= C2D[item].end(); it++){
			//now suppose translate it to *it. 
			int no = *it;
			bool OK = true;
			for(auto it1 = D2C[no].begin(); it1 != D2C[no].end(); it1++){
				if(freq.find(it1->first) == freq.end() || freq[it1->first] < it1->second ){
					OK = false;
					break;
				}
			}
			if(OK){
				number.push_back(no);
				int len=0;
				for(auto it1 = D2C[no].begin(); it1 != D2C[no].end(); it1++){
					freq[it1->first] -= it1->second;
					len += it1->second;
				}
				remainL-=len;
				bool retV =  DFS(number, D2C, C2D, freq, remainL);
				if (retV)
					return true;
				remainL+=len;
				for(auto it1 = D2C[no].begin(); it1 != D2C[no].end(); it1++){
					freq[it1->first] += it1->second;
				}
				number.pop_back();
			}
			//else, continue search
		}
	}			
	return false;
}
int main(int argc, char** argv) {
	int T;
	cin>>T;
	cin.ignore();
	unordered_map<int, unordered_map<char, int>> D2C;
	unordered_map<char, unordered_set<int>> C2D;
	for(int i=0; i<10; i++){
		for(int j=0; j<number[i].length(); j++){
			D2C[i][number[i][j]]++;
			C2D[number[i][j]].insert(i);
		}
	}
	
	foreach(itest, T){
		string input;
		getline(cin, input);
		vector<int> number;
		unordered_map<char, int> freq;
		
		for(int i=0; i<input.length(); i++)
			freq[input[i]]++;
		
		DFS(number, D2C, C2D, freq, input.length());
		sort(number.begin(), number.end());
		cout<<"Case #"<<itest+1<<": ";
		for(auto item: number)
			cout<<item;
		cout<<endl;	
	}
	return 0;
}
