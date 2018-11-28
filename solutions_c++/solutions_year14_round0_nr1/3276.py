#include <iostream>
#include <set>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;
	int a, b, j, k;
	int temp1, temp2;
	set<int> u1, u2, u3;
	vector<int> s;
	
	set<int>::iterator it;
	for( int i = 1; i <= T; i++ )
	{
		//cout << T << endl;
		s.clear();
		u1.clear();
		u2.clear();
		u3.clear();
		cin >> a;
		//cout << "torba";
		for( j = 0; j < 4; j++ )
			for( k = 0; k < 4; k++ )
				if( j == (a-1) ) 
				{ 
					cin >> temp1;
					u1.insert(temp1);
				}
				else cin >> temp1;
		cin >> b;
		//cout << "torba2";
		int count = 0, value;
		for( j = 0; j < 4; j++ )
			for( k = 0; k < 4; k++ )
				if( j == (b-1) ) 
				{ 
					cin >> temp2;
					temp1 = u1.size();
					u1.insert(temp2);
					if( temp1 == u1.size() )
					{
						value = temp2;
						count++;
					}
				}
				else cin >> temp2;

		if( count > 1 )
			cout << "Case #" << i << ": Bad magician!" << endl;
		else 
		{
			if( count == 0 )
				cout << "Case #" << i << ": Volunteer cheated!" << endl;
			else cout << "Case #" << i << ": " << value << endl;
		}


	}
	return 0;
}
