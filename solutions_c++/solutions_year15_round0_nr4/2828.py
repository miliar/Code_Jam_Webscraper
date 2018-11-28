#include <iostream>
using namespace std;
int main ()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	
	int t;
	cin >> t;
	for (int tn = 0 ; tn < t ; tn++)
	{
		bool can =false;
		int x,r,c;
		cin >> x >> r >> c ;
		//cout << x<<" "<<r<<" "<<c<<" ";
		if(x==1)
		{
			can =true;
		}
		else if (x==2)
		{
			if((r*c)%2 == 0)
			{
				can =true;
			}

		}
		else if (x==3)
		{
			if( ((r*c)%3) ==0 && (r*c) > 5 && (r>1) && (c>1))
			{
				can =true;
			}

		}
		else if(x==4)
		{
			if(r*c>=12)
			{
				can =true;
			}
		}
		//cout<<can<<endl;
		
		if(can)
		{
			cout << "Case #" << (tn+1) << ": GABRIEL" << endl;
		}
		else
		{
			cout << "Case #" << (tn+1) << ": RICHARD" << endl;
		}
		
	}

}