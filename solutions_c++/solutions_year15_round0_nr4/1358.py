#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>

using namespace std;

int X,R,C;

vector<vector<pair<int,int> > >table(5);

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	
	
	int T; cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		
		cin>>X>>R>>C;
		if( R > C )
			swap( R, C );
		
		if( ((R*C) % X) != 0 ){
			cout<<"RICHARD\n";
			continue;
		}
		
		if( X == 3 ){
			if( R == 1 ){
				cout<<"RICHARD\n";
				continue;
			}
		}
		
		if( X == 4 ){
			if( (R >= 3) && (C==4) )
				cout<<"GABRIEL\n";
			else
				cout<<"RICHARD\n";
			continue;
		}
			
		cout<<"GABRIEL\n";
	}
	
}
