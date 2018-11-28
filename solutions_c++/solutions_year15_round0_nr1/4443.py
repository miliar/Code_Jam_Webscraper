#include <iostream>
#include <cstdio>

using namespace std;

int main(int argc, char *argv[]) {
	freopen( "input_s.txt", "r", stdin );
	freopen( "output_s.txt", "w", stdout );
	
	int cases,max_shyness;
	
	cin>>cases;
	
	for(int i=0;i<cases;i++){
		string audience="";
		int stand_people=0, needed_people=0;
		
		cin>>max_shyness>>audience;
		
		for(int j=0;j<=max_shyness;j++){
			
			if(j>stand_people){
			needed_people+=j-stand_people;
			stand_people=j;
			}
			stand_people+=(int)audience[j]-48;
		}
		cout<<"Case #"<<i+1<<": "<<needed_people<<"\n";
	}
	return 0;
}

