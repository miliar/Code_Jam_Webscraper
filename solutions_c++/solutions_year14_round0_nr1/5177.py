#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <stdlib.h>
#include <vector>
using namespace std;

int main() {
	int n = 0;
	vector< vector<int> > p(4,vector<int>(4));
	vector< vector<int> > o(4,vector<int>(4));
	cin >> n;
	for(int q = 1 ; q <= n; ++q ){
		int a=0,b=0,c=0,k=0,l=0;
		cin>>b;
		for(int i = 0; i < 4 ; ++i ){
			for (int j = 0; j < 4 ; ++j ){
				cin>>a;
				p[i][j]=a;
			}
		}
		cin>>c;
		for(int i = 0; i < 4 ; ++i ){
			for (int j = 0; j < 4 ; ++j ){
				cin>>a;
				o[i][j]=a;
			}
		}
		for(int i = 0 ; i < 4;++i)
			for(int j=0; j < 4; ++j)
				if(p[b-1][i]==o[c-1][j]){
					++k;
					l=p[b-1][i];
				}
		if ( k == 0)
			cout<<"Case #"<<q<<": Volunteer cheated!"<<endl;
		if ( k == 1)
			cout<<"Case #"<<q<<": "<< l<<endl;
		if ( k > 1 )
			cout<<"Case #"<<q<<": Bad magician!"<<endl;
			
	}

}