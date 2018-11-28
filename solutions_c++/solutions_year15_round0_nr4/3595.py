#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int llt;

int main() {
	int t, x, r,c, j=1;
	char a2[4][4] ={
	                {'r', 'g', 'r', 'g'}, 
	                {'g', 'g', 'g', 'g'},
					{'r', 'g', 'r', 'g'},
					{'g', 'g', 'g', 'g'}
			       }; 
	char a3[4][4]= {
					{'r', 'r', 'r', 'r'},
					{'r', 'r', 'g', 'r'},
					{'r', 'g', 'g', 'g'},
					{'r', 'r', 'g', 'r'}
		     	   };
	char a4[4][4] ={
					{'r', 'r', 'r', 'r'},
					{'r', 'r', 'r', 'r'},
					{'r', 'r', 'r', 'g'},
					{'r', 'r', 'g', 'g'}
				   };
	cin>>t;
	while(t--) {
		cin>>x>>r>>c;
		cout<<"case #"<<j<<": ";
		if(x==1) {
			cout<<"GABRIEL\n";
		}
		else if(x==2) {
			if(a2[r-1][c-1] == 'r') {
				cout<<"RICHARD\n";
			}
			else {
				cout<<"GABRIEL\n";
			}
		}
		else if(x==3) {
			if(a3[r-1][c-1] == 'r') {
				cout<<"RICHARD\n";
			}
			else {
				cout<<"GABRIEL\n";
			}
		}		
		else if(x==4) {
			if(a4[r-1][c-1] == 'r') {
				cout<<"RICHARD\n";
			}
			else {
				cout<<"GABRIEL\n";
			}
		}		
		j++;
	}
	return 0;
}
