#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <list>
#include <map>

using namespace std;

int main() {
	
	int nNumOfTCs,nCurTC = 1;

	cin  >> nNumOfTCs;
	while(nCurTC <= nNumOfTCs){
		int A,B,K, count = 0;
		cin>>A>>B>>K;
		
		for(int i = 0 ; i < A;i++)
			for(int j = 0; j < B;j++)
				if( (i & j) < K)
					count++;
		

		cout<<"Case #"<<nCurTC<<": "<< count<<"\n"; 
		
		nCurTC++;
	}
	return 0;
}
