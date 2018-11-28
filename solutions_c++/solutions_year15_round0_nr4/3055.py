#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		cout << "Case #"<<c<<": ";
		int X,R,C;
		cin >> X >> R >> C;
		if(X==1)
			cout << "GABRIEL" << endl;
		else if(X==2 && (R*C)%2==0)
			cout << "GABRIEL" << endl;
		else if(X==3 && ((R==3 && C==3) || (R==2 && C==3) || (R==3 && C==2) || (R==4 && C==3) || (R==3 && C==4)))
			cout << "GABRIEL" << endl;
		else if(X==4 && ((R==4 && C==3) || (R==3 && C==4) || (R==4 && C==4)))
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
	return 0;
}
