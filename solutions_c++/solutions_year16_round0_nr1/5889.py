#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
#include<cstdlib>
#include<fstream>

using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;

bool dreams[10]={0,0,0,0,0,0,0,0,0,0};
int final=0;

void tester(int n){
	if(n<10){
		dreams[n]=1;
	}
	else{
		dreams[n%10]=1;
		tester(n/10);	
	}	
}

int solve(int n) {
	
	bool checker=false;
	int nextDream=n;
	int k=1;
	int truth=0;
	while(checker==false){
		truth=0;
		tester(nextDream);
		for(int i=0; i<=9; i++){
			if(dreams[i]==1){
				truth=truth+1;
			}
		}
		if(truth==10){
			checker=true;
			break;
		}

		k=k+1;
		nextDream=n*k;
	}
	return nextDream;
}

int leer_int(istream& is){
int a;
is >> a;
return a;
};

ostream& escribir_int(int a, ostream& os){
os << a;
os << '\t';
return os;
};

int main() {


	ifstream ifs("A-large.in");
	ofstream ofs("salida.txt");
	
	int test_cases;
	ifs>>test_cases;
	cout<<test_cases;

	for (int test_case = 1; test_case <= test_cases; test_case++) {
		int n;
		ifs>>n;
        if(n==0){
			cout << "Case #" << test_case << ": " << "INSOMNIA" << endl;
			ofs<< "Case #" << test_case << ": " << "INSOMNIA" << endl;
		}
        else{
        	int k=solve(n);
        	cout << "Case #" << test_case << ": " << k<< endl;
        	ofs<< "Case #" << test_case << ": " << k << endl;
		}
		for(int i=0; i<=9; i++){
			dreams[i]=0;
		}
    }
    
	ifs.close();
	ofs.close();
	return 0;
}
