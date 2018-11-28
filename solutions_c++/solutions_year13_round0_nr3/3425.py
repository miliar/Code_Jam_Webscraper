#include <iostream>
using namespace std;

int main()
{
	int num[]={1,4,9,121,484};
	int z,t,l,r,a,b;
	cin >> t;
	for(z=1;z<=t;z++)
	{
		cin >> a >> b;
		l=0;r=4;
		while(a>num[l])
			l++;
		while(b<num[r])
			r--;
		cout << "Case #" << z << ": " << (r-l+1) << endl;
	}
	return 0;
}	
