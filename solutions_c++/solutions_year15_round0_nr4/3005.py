#include <iostream>
using namespace std;
const string s1 = "GABRIEL";
const string s2 = "RICHARD";
int main()
{
	int T,X,R,C;
	cin >> T;
	for(int a=1;a<=T;a++){
		cin >> X >> R >> C;
		cout << "Case #" << a << ": " ;
		if(X==1)
			cout << s1;
		else if(X==2)
			(R*C < X || (R*C)%2==1)?cout << s2 : cout << s1;
		else if(X==3)
			(R==2 && C==3 || R==3 && C==2 || R == 3 && C==3 || R==3 && C==4 || R==4 && C==3 )?cout << s1:cout << s2;
		else
			(R==3 && C==4 || R==4 && C==3 || R==4 && C==4)?cout << s1 :cout << s2;
		cout << "\n";
	}
	return 0;
}
