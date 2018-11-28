#include<iostream>

using namespace std;

int main()
{
    int T;	cin >> T;
    for (int i = 1;i <= T; i++)
    {
    	int x,r,c;
    	cin >> x;
    	cin >> r >> c;
		if(x==1) 
			cout << "Case #" << i << ": GABRIEL\n";
		if(x==2)
		{
			if((r*c)%2==0) 
				cout << "Case #" << i << ": GABRIEL\n";
			else 
				cout << "Case #" << i << ": RICHARD\n";

		}
		if(x==3)
		{
			if((r%3==0 && c%2==0) || (r%2==0 && c%3==0) || (r==3 && c==3)) 
				cout << "Case #" << i << ": GABRIEL\n";
			else 
				cout << "Case #" << i << ": RICHARD\n";
		}
		if(x==4)
		{
			if((r==3 && c==4) || (r==4 && c==3) || (c==4 && r==4)) 
				cout << "Case #" << i << ": GABRIEL\n";

			else 
				cout << "Case #" << i << ": RICHARD\n";
		}
   }
	return 0;
}