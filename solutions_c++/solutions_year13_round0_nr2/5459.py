#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define aij 2
vector<vector<int> > initializeSquare(int n, int m, int h){
    vector<vector<int> > a;
    for(int i = 0; i<n; i++){
	vector<int> b;
	for(int j = 0; j<m; j++){
	    b.push_back(h);
	}
	a.push_back(b);
    }
    return a;
}

void print(vector<vector<int> > a){
   for(int i = 0; i<a.size(); i++){
	for(int j = 0; j<a[i].size(); j++){
	    cout << a[i][j] << " ";
	}
	cout << endl;
    } 
}

int maxRow(vector<vector<int> > a, int r){
    return *max_element(a[r].begin(), a[r].end());
}

int maxCol(vector<vector<int> > a, int c){
   int max = a[0][c];
   for(int i = 1; i<a.size(); i++){
	int instance = a[i][c];
	if(max < instance){
	    max = instance;
	}
   }
   return max;
}

bool changed = false;
vector<vector<int> > trimRow(vector<vector<int> > a, vector<vector<int> > b){
   for(int i = 0; i<a.size(); i++){
	int max = maxRow(a, i);
	for(int j = 0; j<b[i].size(); j++){
	    if(b[i][j] > max){
		b[i][j] = max;
		changed = true;
	    }
	}
   }
   return b;
}


vector<vector<int> > trimCol(vector<vector<int> > a, vector<vector<int> > b){
   for(int i = 0; i<a[0].size(); i++){
	int max = maxCol(a, i);
	for(int j = 0; j<b.size(); j++){
	    if(b[j][i] > max){
		b[j][i] = max;
		changed = true;
	    }
	}
   }
   return b;
}



vector<vector<int> > trim(vector<vector<int> > a, vector<vector<int> > b){
    do{
	changed = false;
	b = trimRow(a, b);
//	print(b);

	b = trimCol(a, b);
//	print(b);
	
    }while(changed);

    return b;

}

string compare(vector<vector<int> > a, vector<vector<int> > b){
    for(int i = 0; i<a.size(); i++){
	for(int j = 0; j<a[0].size(); j++){
	    if(a[i][j] != b[i][j]){
		return "NO";
	    }
	}
    }
    return "YES";
}

vector<string> save;
void startTrim(){
    int n, m;
    cin >> n;
    cin >> m;
    vector<vector<int> > a;
    for(int i = 0; i<n; i++){
	vector<int> instance;
	for(int j = 0; j<m; j++){
	    int input;
	    cin >> input;
	    instance.push_back(input);
	}
	a.push_back(instance);
    }
    vector<vector<int> > b = initializeSquare(a.size(), a[0].size(), aij);
//    print(b);
  b = trim(a, b);
//print(b);
save.push_back(compare(a, b));
    
}

int main(){
 //   cout << "Hello" << endl;
//    vector<vector<int> > instance = initializeSquare(3, 5, 10);
  //  print(instance);
   // cout << maxRow(instance, 1) << endl;
   // cout << maxCol(instance, 2) << endl;
    int caseNumber;
    cin >> caseNumber;

    for(int i = 0; i<caseNumber; i++){
	startTrim();
    }
    for(int i = 0; i<save.size(); i++){
	cout << "Case #" << i+1 << ": " << save[i] << endl;
    }

    return 0;
}
