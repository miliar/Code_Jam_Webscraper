#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int I=0;I<T;I++)
	{
		int res = 0;	//0->no se puede rellenar; 1->se puede rellenar
		int x,r,c;
		cin >> x >> r >> c;
		if(x==1)
			res = 1;
		else if((r*c)%x)
			res = 0;
		else if(x==2)
			res = 1;
		else if(r==1 || c==1)
			res = 0;
		else if(x==3)
			res = 1;
		else if(r==2 || c==2)
			res = 0;
		else
			res = 1;
		cout << "Case #" << I+1 << ": ";
		if(res)
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
}
