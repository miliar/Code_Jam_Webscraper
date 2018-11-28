#include <fstream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <set>
using namespace std;


int x,r,c;

bool can()
{
	if (x<3)
		return true;
	if ((x>6)&&(r>=3))
		return false;
	if (x>c)
		return false;
	if (x>=2*r+1)
		return false;
	if ((r>2)&&(c>1)&&((c+3<=x)))
		return false;
	if (((r==3)||(r==2))&&(c>1)&&(c+1<=x))
		return false;
	if ((r==2)&&(x>=4))
		return false;
	return true;
}



int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int q;
	cin>>q;
	for (int qq=0;qq<q;qq++)
	{
		cout<<"Case #"<<qq+1<<": ";
		cin>>x>>r>>c;
		if (r>c)
				swap(r,c);
		if (((r*c)%x==0)&&(can()==true))
		{
					cout<<"GABRIEL"<<endl;
		}
		else
		{
			cout<<"RICHARD"<<endl;
		}	
	}
	return 0;
}
