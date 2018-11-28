#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

bool xcut(int, int, int);
bool ycut(int, int, int);
bool isPossible(int, int);

int map[100][100];
int imap[100][100];
set<int> list;

bool isPossible(int, int);

int main(){
	int t, max;
	
	cin >> t;
	for(int i = 0; i < t; i++){
		int n, m;
		max = 0;
		
		cin >> n >> m;
		for(int j = 0; j < n; j++){
			for(int k = 0; k < m; k++){
				cin >> imap[j][k];
				list.insert(imap[j][k]);
				if(imap[j][k] > max){
					max = imap[j][k];
				}
			}
		}
		
		for(int j = 0; j < n; j++){
			for(int k = 0; k < m; k++){
				map[j][k] = max;
			}
		}
		
		
		if(isPossible(n, m)) 
			cout << "Case #" << i+1 << ": YES" << endl;
		else
			cout << "Case #" << i+1 << ": NO" << endl;
	}
	
	return 0;
}

bool isPossible(int n, int m){
	set<int>::reverse_iterator h = list.rbegin();
	while( h != list.rend()){
		for(int i = 0; i < n; i++){
			if(xcut(i, m, *h)){
				for(int j = 0; j < m; j++){
					map[i][j] = *h;
				}
			}
		}
		
		for(int i = 0; i < m; i++){
			if(ycut(i, n, *h)){
				for(int j = 0; j < n; j++){
					map[j][i] = *h;
				}
			}
		}
		h++;
	}
	
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(imap[i][j] != map[i][j])
				return false;
		}
	}
	return true;
}
	
bool xcut(int i, int m, int h){
	//cout << "t = " << imap[i][0] << " h = " << h << endl;
	
	for(int j = 0; j < m; j++){
		if(imap[i][j] > h)
			return false;
	}
	//cout << 'a' << endl;
	return true;
}

bool ycut(int i, int n, int h){
	for(int j = 0; j < n; j++){
		if(imap[j][i] > h)
			return false;
	}
	return true;
}

