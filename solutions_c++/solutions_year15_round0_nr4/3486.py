#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main() {
	// your code goes here
	
	int cases;
	cin>>cases;
	
	for(int q=0 ; q<cases ; q++)
	{
		int x, r, c;
		cin>>x>>r>>c;
		cout<<"Case #"<<q+1<<": ";
		if((r<x && c<x) || ((r*c)%x!=0) || (max(r,c) == x && max(r,c)-min(r,c)>=2))
			cout<<"RICHARD\n";
		else
			cout<<"GABRIEL\n";
		
	}
	
	return 0;
}
