#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string NUMS[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE"
					,"SIX","SEVEN","EIGHT","NINE"};
int order[10] = {6,0,2,4,8,5,7,9,3,1}	;
			
string  find(int ind , vector<int> &S , int &n)
{
	vector<int> temp = S;
	int found = 0;
	string num = NUMS[ind];
	string result = "";
	int count = 0;
	while( 1 )
	{
		if( count == num.length() )
		{
			n += count;
			S = temp;
			found++;
			count = 0;
			result = result + char(ind + '0');
		}
		else if( temp[num[count]] > 0 )
		{			
			temp[num[count]]--;
			count++;
		}
		else 
		{
			break;
		}
		
	}
	return result;
}
int main()
{
	int T;
	string S;
	string r;
	cin >> T;
	vector<int> letters;
	int n;
	for( int i = 1 ; i <= T ; i++ )
	{
		n = 0;
		r = "";
		letters.clear();
		letters.resize(256,0);
		cin >> S;	
		for( int j = 0 ; j < S.length() ; j++ )
		{
			letters[S[j]]++;
		}
		cout << "Case #" << i << ": ";
		for( int j = 0 ; j < 10 ; j++ )
		{
			r += find( order[j] , letters , n );
		}
		if( n != S.length() )
		{
			cerr << "Error" << endl;
		}
		sort(r.begin(),r.end());
		cout << r << endl;
			
	}
	
	return 0;
}
