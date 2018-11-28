#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define fastin std::ios::sync_with_stdio(false);cin.tie(nullptr)
#define cout_precision(x) cout<<std::fixed<<setprecision(x)
using namespace std;

pair<bool, char> multiply( pair<bool, char> c1, pair<bool, char> c2 )
{
	pair<bool, char> ret( true, '1' );

	if ( c2.second < c1.second )
	{
		swap( c1, c2 );
		if ( c1.second != '1' )
		{
			ret.first = !ret.first;
		}
	}

	if ( c1.second == c2.second )
	{
		ret.second = '1';
		if ( c1.second != '1' )
		{
			ret.first = !ret.first;
		}
	}
	else if ( c1.second == '1' )
	{
		ret.second = c2.second;
	}
	else if ( c1.second == 'i' )
	{
		if ( c2.second == 'j' )
		{
			ret.second = 'k';
		}
		else if ( c2.second == 'k' )
		{
			ret.second = 'j';
			ret.first = !ret.first;
		}
	}
	else if ( c1.second == 'j' )
	{
		ret.second = 'i';
	}

	ret.first = !( ret.first ^ ( !( c1.first ^ c2.first ) ) );
	return ret;
}

void findI( const string& s, unsigned& start, pair<bool, char>& source )
{
	const auto end = s.size() - 1;

	auto target = mp( true, 'i' );
	auto res = source;

	while ( start <= end )
	{
		res = multiply( res, mp( true, s[start++] ) );
		if ( res == target )
		{
			break;
		}
	}
	source = mp( true, 'i' );
}

bool findJ( const string& s, unsigned start, const unsigned& end )
{
	assert( end < s.size() );

	auto target = mp( true, 'j' );
	auto res = mp( true, '1' );

	while ( start <= end )
	{
		res = multiply( res, mp( true, s[start++] ) );
	}
	if ( res == target )
	{
		return true;
	}
	return false;
}

void findK( const string& s, int& start, pair<bool, char>& source )
{
	auto target = mp( true, 'k' );

	while ( start >= 0 )
	{
		source = multiply( mp( true, s[start--] ), source );
		if ( source == target )
		{
			break;
		}
	}
}

int main()
{
	int t, testCase = 1;
	cin >> t;
	while ( t-- )
	{
		int l, x;
		string s;
		cin >> l >> x >> s;
		string sx;
		while ( x-- )
		{
			sx += s;
		}

		unsigned iStart = 0;
		pair<bool, char> iSource = mp( true, '1' );

		int kStart = ( int )sx.size() - 1;
		auto kSource = iSource;

		bool jFound = false;

		while ( ( int )iStart < kStart - 1 )
		{
			findI( sx, iStart, iSource );
			//print( iStart );
			if ( iStart == sx.size() )
			{
				break;
			}

			findK( sx, kStart, kSource );
			//print( kStart );
			if ( kStart == -1 )
			{
				break;
			}

			jFound = findJ( sx, iStart, kStart );
			if ( jFound )
			{
				break;
			}
		}
		string ans = jFound ? "YES" : "NO";
		cout << "Case #" << testCase++ << ": ";
		cout << ans << "\n";
	}
}
