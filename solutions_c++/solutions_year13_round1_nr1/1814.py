#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <cmath>
#include <cctype>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
#include <cctype>
#include<fstream>
using namespace std;
int main() {
		 ifstream fin("in.in");     
	 ofstream fout;
	 fout.open("A.out");
	 int T; 
	 fin>>T;

	 for(int i = 0 ; i < T ; i++)
	 {
	unsigned long long r,t; 


	fin>>r>>t;



	unsigned long long result =0 ;

	
	
	while(1)
	{
		unsigned long long rad = r+1;
		if(((rad*rad)- (r*r)) <=t)
		{
			result++;
			t = t -((rad*rad)- (r*r));
		}	
		else
			break;
		r= r+2;
	}
	fout<<"Case #"<<i+1<<": "<<result<<endl;
	 }
    return 0 ;
}