#include<bits/stdc++.h>
using namespace std;
int arr[26];
int main()
{
	freopen("archivo.in","r",stdin);
	freopen("archivo.out","w",stdout);
	int tc;
	cin >> tc;
	string numbers[] = {"ZERO","SIX","SEVEN","FIVE","FOUR","TWO","EIGHT","THREE","NINE","ONE"};
	int ind[] = {0,6,7,5,4,2,8,3,9,1};
	for ( int t = 1 ; t <= tc ; t ++ )
	{
		string s;
		cin >> s;
		memset ( arr, 0 , sizeof(arr));
		for ( int i = 0 ; i < s.size(); i ++ )
		{
			arr[s[i]-'A'] ++ ;
		}
		int c = 0;
		vector < int > ans;
		while ( true )
		{
//			cout << numbers[c] << endl;
			if ( c == 10 )
				break;
			bool flag = true;
			int clet[26] ;
			memset ( clet, 0 , sizeof(clet));

			for ( int i = 0 ; i <numbers[c].size() ; i ++ )
			{
				 clet[numbers[c][i]-'A'] ++;
			}	
			for ( int i = 0 ; i < 26 ; i ++ )
			{
//				cout << (char)(i+'A') << " " << clet[i] << endl;
			}
			for ( int i = 0 ; i < 26 ; i ++ )
			{
				if ( clet[i] > arr[i])
				{
//					cout << i << endl;
					flag = false;
					break;
				}
			}
			if ( !flag ) 
			{
				c++;
				continue;
			}
			for ( int i = 0 ; i < 26 ; i ++ )
			{
				arr[i] -= clet[i];
			}
			ans.push_back(ind[c]);
		}
		sort ( ans.begin() ,ans.end());
		cout << "Case #"<<t<<": " ;
		for ( int i = 0 ; i < ans.size() ; i ++ )
		{
			cout << ans[i];
		}
		cout << "\n";
	}

}
