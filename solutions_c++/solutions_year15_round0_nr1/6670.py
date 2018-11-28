#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
	int esetek, db, tmp, plusz, ossz;
	char tmpchar;
	cin>>esetek;
	for(int y=1; y<=esetek; y++) {
	cin>>db;
	plusz=0;
	ossz=0;
	for(int i=1; i<=db; i++)
	{
		cin>>tmpchar;
		tmp = atoi(&tmpchar);
		if(i<=(ossz+tmp)) ossz+=tmp;
		else {
			plusz+=(i-(ossz+tmp));
			ossz=i;
		}
	}
	cin>>tmpchar;
	cout<<"Case #"<<y<<": "<<plusz<<endl;
	}
	
	
	return 0;
}