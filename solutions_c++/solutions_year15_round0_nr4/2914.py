#include <iostream>
#include <cmath>
#include <queue>
#include <string>
using namespace std;
int main()
{
	int n,q;
	int i=1;
	cin>>n;
	string res;
	while(n--) {
		int x,r,c;
		cin>>x>>r>>c;
		switch(x) {
			case 1:
				res="GABRIEL";
				break;
			case 2:
				if((r*c)%2==0)
					res="GABRIEL";
				else
					res="RICHARD";
				break;
			case 3:
				if(r*c%3)
					res="RICHARD";
				else{
					if(min(r,c)==1)
						res="RICHARD";
					else
						res="GABRIEL";

				}
				break;

			case 4:
				if(max(r,c)==4 && min(r,c)>2)
					res="GABRIEL";
				else
					res="RICHARD";
				break;
		}


		cout<<"Case #"<<i++<<": ";
		cout<<res<<endl;
	}
}
