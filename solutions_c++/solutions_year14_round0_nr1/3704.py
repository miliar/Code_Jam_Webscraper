//#include <simplecpp>
#include<iostream>
#include<string>
#include<fstream>

using namespace std;

bool belongs(int n, int array[]){
	for (int i=0; i<4; i++) {if (n==array[i]) return true;}
	return false;
}

int main(int argc, char* argv[ ])
{
	int T, grid[16], cache[4], r;
	cin>>T;
	
	for (int t=1; t<=T; t++) {
		cin>>r;
		for (int i=0; i<16; i++) cin>>grid[i];
		for (int i=0; i<4; i++) cache[i]=grid[(r-1)*4+i];
		cin>>r;
		for (int i=0; i<16; i++) cin>>grid[i];
		int count=0;
		int answer=0;
		for (int i=0; i<4; i++){
			if (belongs(grid[(r-1)*4+i], cache)) {
				count++;
				answer=grid[(r-1)*4+i];
			}
		}
		if (count==0) cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		else if (count==1) cout<<"Case #"<<t<<": "<<answer<<endl;
		else cout<<"Case #"<<t<<": Bad magician!"<<endl;
	}
}