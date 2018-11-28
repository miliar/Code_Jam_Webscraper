#include <iostream>
#include <cmath>

using namespace std;

int main()
{

	int t,i,j,z;
	int a,b,rez;

	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);

	cin>>t;

    for (z=0;z<t;z++) {
		
		rez=0;
		cin>>a>>b;

		if (a==1) {
			if (b<4) rez=1;
			else if (b<9) rez=2;
				else if (b<121) rez=3;
					else if (b<484) rez=4;
					else rez=5;
		}
		if (a>1) {
			if (b<4) rez=0;
			else if (b<9) rez=1;
				else if (b<121) rez=2;
					else if (b<484) rez=3;
					else rez=4;
		}
		if (a>4) {
			if (b<9) rez=0;
				else if (b<121) rez=1;
					else if (b<484) rez=2;
						else rez=3;
		}
		if (a>9) {
			if (b<121) rez=0;
				else if (b<484) rez=1;
					else rez=2;
		}
		if (a>121) {
			if (b<484) rez=0; else rez=1;
		}
		if (a>484) rez=0;

        cout<<"Case #"<<z+1<<": "<<rez<<endl;

    }


}