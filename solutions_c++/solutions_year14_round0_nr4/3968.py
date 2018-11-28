#include<vector>
#include<fstream>
//#include<iostream>
#include<string>
#include<algorithm>
#include<ctime>
#include<iomanip>
using namespace std;
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for( int q = 0 ; q < T ; q++)
	{
	int n;
	cin >> n;
	vector < double > vec1(n), vec2(n);
	for ( int i = 0 ; i < n ; i++ )
		cin >> vec1[i];
	for ( int i = 0 ; i < n ; i++ )
		cin >> vec2[i];
	sort(vec1.begin(), vec1.end());
	sort(vec2.begin(), vec2.end());

	int mark = 0;
	int count1 = 0;
	for ( int i = 0 ; i < n ; i++ ) 
	{
		if(vec1[i] > vec2[mark])
		{
			mark++;
			count1++;
		}
	}

	mark = n-1;
	int count2 = 0;
	for ( int i = n-1 ; i >= 0 ; i-- ) 
	{
		if(vec1[i] < vec2[mark])
		{
			mark--;
			count2++;
		}
	}
	cout << "Case #" << q+1 << ": " << count1 << " " << n-count2 << endl;
	}
}