#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <cmath>
#include <sstream>
using namespace std;

// sqrt

bool palin(int n){
	int m = n;
	int remain;
	remain = m%10;
	m = m/10;
	while(m>0){
		remain = remain * 10 + (m % 10);
		m = m/10;
	}
	if(n == remain){
		return true;
	}
	return false;
}
int process(int A, int B)
{
	float begin = sqrt(A);
	int end = sqrt(B);
	if((int)begin < begin )
	{
		begin ++;
	}
	int count= 0;
	for(int i = begin; i<= end; i++){
		if( palin(i)){
			if( palin(i*i)){
				count ++;
				//cout<< "::"<<i<<endl;
			}
		}
	}
	return count;
}
int main()
{
	int T, N = 1;
	
	int symbolT;
	bool haveWin;
	bool haveEmpty = false;
	ofstream out;
	out.open("e:/problem_C.out");
	ifstream in;
	in.open("e:/C-small-attempt0.in");
	string line;
	getline(in, line);
	T = atoi(line.c_str());
	int A, B; // care 1000
	while(N <= T){
		getline(in, line);
		stringstream ss(line);
		ss >> A >>B;
		//cout << A<< " " << B <<endl;
		out<<"Case #"<<N<<": "<< process(A, B)<<endl;
		//cout <<"Case #"<<N<<": "<< process(A, B)<<endl;
		
		N++;
	}
	
	out.close();
	in.close();
	return 0;
}
