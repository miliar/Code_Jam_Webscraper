#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
	// your code goes here
	
	
	int castT;
	ifstream fin ( "A-large.in" );
    ofstream fout ( "A-large.txt" );
    fin>> castT;
	for(int j=0; j<castT; j++){
		
		int N;
		
		fin>> N;
		fout << "Case #" << j+1<< ": ";
		
		if(N==0)fout << "INSOMNIA"<<endl;
		else{
			
			int done=0,i=1;
		long long int ret=0;
		int a[10]={0,0,0,0,0,0,0,0,0,0};
		
		while(done<10){
		
		long long int temp=i*N;
		ret=temp;
		i++;
		
		//break it in reverse
		while(temp>0){
			long long int t= temp%10;
			temp=temp/10;
			
			a[t]++;
			if(a[t]==1)done++;
		}
		}
		
		fout << ret<<endl;
			
		}
		
	}
	return 0;
}
