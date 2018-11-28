#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	vector<double> v1, v2;
	vector<double>::iterator it1, it2;
	int N, a1[1020], a2[1020], j, k;
	for( int i = 1; i <= T; i++ )
	{
		cin >> N;
		v1.clear();
		v2.clear();
		double temp, l1, l2;
		for( j = 0; j < N; j++ )
		{	
			cin >> temp;
			v1.push_back(temp);
			//cout << "For1" << endl;
		}
		for( k = 0; k < N; k++ )
		{
			cin >> temp;
			v2.push_back(temp);
			//cout << "For2" << endl;
		}
		sort(v1.begin(), v1.end() );
		sort(v2.begin(), v2.end() );
		
		int count = 0;
		/*		
		for( j = 0; j < v1.size(); j++ )
			cout << v1[j] << " ";
		cout << endl;
		
		for( j = 0; j < v2.size(); j++ )
			cout << v2[j] << " ";
		cout << endl;
		*/
		// first part of algo		
		int count3 = N - 1, count4 = N - 1;
		for( j = 0; j < N; j++ )
		{
			if( v1[count3] > v2[count4] )
			{
				count3--;
				count++;
			}
			else
			{
				count4--;
				count3--;
			}
		}
		count3 = N - 1;
		count4 = N - 1;
		int countd = 0;
		for( j = 0; j < N; j++ )
		{
			if( v1[count3] > v2[count4] )
			{
				count3--;
				count4--;
				countd++;
			}
			else
			{
				count4--;			
			}
		}
		cout << "Case #" << i << ": " << countd << " " << count << endl;
			
	}
	return 0;
}
