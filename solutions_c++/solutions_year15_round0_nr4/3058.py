#include <iostream>
#include <stdio.h>

using namespace std;

string v[16] =
{
	"GRRR",
	"GGRR",
	"GRRR",
	"GGRR",
	"GGRR",
	"GGRR",
	"GGGR",
	"GGRR",
	"GRRR",
	"GGGR",
	"GRGR",
	"GGGG",
	"GGRR",
	"GGRR",
	"GGGG",
	"GGRG"
};


int main() {
	int tc;
	cin>>tc;
	int cs = 1;
	while(tc--) {
		int x,r,c;
		cin>>x>>r>>c;

		int idx = (r-1)*4 + c - 1;	
		char win = v[idx][x-1];
		if(win == 'R') cout<<"Case #"<<cs<<": RICHARD"<<endl;
		else cout<<"Case #"<<cs<<": GABRIEL"<<endl;
		cs++;
	}
	return 0;
}