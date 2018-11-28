#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <sstream>
#include <bitset>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <fstream>

using namespace std;

int i , j , k;

int main ()
{
	int ncases;
	int maximo;
	string txt;
	cin >>ncases;
	ofstream outfile;
    outfile.open("timilargo.txt");
   
	
	for ( i =1; i<=ncases;i++){
		
		cin >> maximo;
		cin >> txt;
		int conta =0;
		int invi =0;
		for ( j =0; j < txt.size();j++){
			
			if ( txt[j] != '0'){//alguine es timido aqui
				
				if ( conta < j){ //falta
				
					int dif = j - conta;
				
			//		cout <<"falta "<<dif<<" llevo "<<conta<<endl;
					invi += dif;
					conta += dif;
					
					//agrega actual
					conta += ( txt[j] -'0');
					
				}else{
						conta += ( txt[j] -'0');
				}
			}
			
			
		}
		
	//	cout <<"**"<<conta<<" invi "<<invi<<endl;

	cout    <<"Case #"<<i<<": "<<invi<<endl;
	outfile <<"Case #"<<i<<": "<<invi<<endl;
	//	outfile <<"Case #"<<i<<": ";
		
	
	}
	
		
	return 0;
	

}




