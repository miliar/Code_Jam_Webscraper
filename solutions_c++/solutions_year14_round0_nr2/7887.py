#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <string>
#include <fstream>
#include <iomanip>
using namespace std;

int n,N;
string ans;
//9.10 - 9.54
bool small=false;
string challenge="B";
string empty;

ifstream fin(""+challenge+"-large-0.in");
ofstream fout(""+challenge+"-large-0.out");
ofstream fdbg(challenge+".debug");

double c,f,x;

double t=0.0;
double nc = 2.0;
double delta = 0e-6;



double compute(){
	while(true){
		double tfin = x/nc;

		//if(tfin < c/nc+x/(nc+f))return t+tfin;


		double tnext = c/nc + x/(nc+f);

		//double tnext = compute2(t+c/nc, nc+f, x/nc, 0);


		if(tnext>=tfin || tnext<delta){
			return t+tfin;
		} else {

			t += c/nc;
			nc += f;

		}
	}
}

int main(){

	fin >> n;
	//cout << n;
	getline(fin,empty);
	fdbg<<n<<endl;
	
	for(N=1; N<=n; N++){
		
		fin >> c >> f >> x;
		//cout << c << " " << f << " " << x << endl;
		t=0.0;
		nc=2.0;
		double r = compute();//0.0, c);//, 999999999999999999.0,0);
		fout.setf( std::ios::fixed, std:: ios::floatfield );
		fout << "Case #"<<N<<": "<< r<<endl;
		cout << "Case #"<<N<<": "<<  r<<endl;

	}

	return 0;
}