#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

bool isPalidrome(unsigned long n)
{
	char strn[20];
	sprintf(strn,"%ld",n);
	//cout << strn << endl;
	int len = strlen(strn);

	for( int i=0; i<len; i++ )
		if( strn[i]!=strn[len-i-1])
			return false;
	return true;
}


int main()
{
	int t,i=1;
	cin >> t;

	while( t-- )
	{
		unsigned long A, B, squar, count=0;

		cin >> A >> B;

		unsigned long root = ceil(sqrt(A));

		while( (squar=root*root) <= B )
		{
			if( isPalidrome(root) && isPalidrome(squar) )
			{
				count++;
			}
			root++;
		}
		cout << "Case #" << i << ": " << count << endl;
		i++;	
	}

	return 0;
}