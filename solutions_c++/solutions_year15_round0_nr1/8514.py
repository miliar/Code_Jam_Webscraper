#include<set>
#include<map>
#include<list>
#include<iomanip>
#include<cmath>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<complex>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;

const int oo = 1 << 29;

int main(int argc, char **argv) {

	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "w", stdout);

	int num;
	cin>>num;

	for (int i=0 ; i<num ; i++){
		int Smax;
		cin>>Smax;


		//4
		//4 11111
		//1 09
		//5 110011
		//0 1
		string S;
		cin>>S;
		int total = 0;
		int required = 0;
		for(int i=0; i<=Smax; i++) {
			int curNum = S[i] - '0';
			//cout<<total<<" , ";
			if(total < i)
				total ++,required++;
			total += curNum;
		}
		cout<<"Case #"<<i+1<<": "<<required<<endl;
	}

}
