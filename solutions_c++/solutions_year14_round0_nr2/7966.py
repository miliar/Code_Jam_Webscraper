#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int t, i;
	double r, c, f, x, y, tc1, tc2;

	cin>>t;
	for(int ca=1;ca<=t;ca++){
		r=2;y=0;
		cin>>c>>f>>x;
		cout<<"Case #"<<ca<<": "; 
		while(1){
			tc1=x/r;
			tc2=(c/r)+(x/(r+f));
			if(tc1>tc2){
				y+=(c/r);
				r+=f;
			}
			else{
				y+=tc1;
				break;
			}
		}
		printf("%0.7lf", y);
		if(ca<t)	cout<<"\n";
	}

	return 0;
}