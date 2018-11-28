#include <iostream>
#include <list>
#include <cmath>

using namespace std;

typedef long long ll;

//a = a * b


void mulLet( bool &negative, char &a, char b  )
{
	//cout << "Multiply " << a << " " << b << endl;
	if( a == '1' )
		a = b;
	else if( a == 'i' && b == 'i' )
	{
		a = '1';
		negative = !negative;
	}else if( a == 'i' && b == 'j' )
	{
		a = 'k';
	}
	else if( a == 'i' && b == 'k' )
	{
		a = 'j';
		negative = !negative;
	}else if( a == 'j' && b == 'i' )
	{
		a = 'k';
		negative = !negative;
	}else if( a == 'j' && b == 'j' )
	{
		a = '1';
		negative = !negative;
	}else if( a == 'j' && b == 'k' )
	{
		a = 'i';
	}else if( a == 'k' && b == 'i' )
	{
		a = 'j';
	}else if( a == 'k' && b == 'j' )
	{
		a = 'i';
		negative = !negative;
	}else if( a == 'k' && b == 'k' )
	{
		a = '1';
		negative = !negative;
	}
}

void addj( ll &j, ll &lCount, string &equation, ll &l )
{
	j++;
	if( j == equation.size() )
	{
		if( lCount < l - 1 )
		{
			j = 0;
			//cout << " " << endl;
			lCount++;
		}
	}
}

bool isValid( list<char> &v1, list<char> &v2, list<char> &v3 )
{
	char temp = '1';
	bool negative = false;
	for( ll i = 0; i < v1.size(); i++ )
	{
		//cout << v1.front();
		mulLet( negative, temp, v1.front() );
		v1.push_back(v1.front());
		v1.pop_front();
	}
	if( temp != 'i' )
		return false;
	temp = '1';
	negative = false;
	for( ll i = 0; i < v2.size(); i++ )
	{
		//cout << v2.front();
		mulLet( negative, temp, v2.front() );
		v2.push_back(v2.front());
		v2.pop_front();
	}
	if( temp != 'j' )
		return false;
	//cout << endl;
	temp = '1';
	negative = false;
	for( ll i = 0; i < v3.size(); i++ )
	{
		//cout << v3.front();
		mulLet( negative, temp, v3.front() );
		v3.push_back(v3.front());
		v3.pop_front();
	}
	if( temp != 'k' )
		return false;
	//cout << endl;
	//cout << endl;
	//cout << endl;
	return true;
}

int main()
{
	/*ll casses;
	cin >> casses;
	ll x, l;
	ll v1Size, v2Size, v3Size;
	string equation;
	bool good;
	list<char> list2;
	list<char> v1;
	list<char> v2;
	list<char> v3;
	for( int i2 = 0; i2 < casses; i2++ )
	{
		good = false;
		list2.clear();
		v1.clear();
		v2.clear();
		v3.clear();
		cin >> x >> l;
		cin.ignore();
		cin >> equation;
		for( ll n = 0; n < l; n++ )
		{
			for( ll o = 0; o < x; o++ )
			{
				v1.push_back( equation.at(o) );
			}
			cout << n << endl;
		}
		//for( ll b = 0; b < list2.size(); b++ )
		//{
		//	v1.push_back( list2.front() );
		//	list2.push_back(list2.front());
		//	list2.pop_front();
		//}
		
		//for( ll v = 0; v < v1.size(); v++ )
		//{
		//	//cout << v1.front();
		//	v1.push_back(v1.front());
		//	v1.pop_front();
		//}
		
		//cout << endl << endl;;
		v1Size = v1.size();
		for( ll j = 0; j + 1 < v1Size; j++ )
		{
			v2.push_front( v1.back() );
			v1.pop_back();
			v2Size = v2.size();
			for( ll k = 0; k + 1 < v2Size; k++ )
			{
				v3.push_front( v2.back() );
				cout << " : " << v2.back() << endl;
				v2.pop_back();
				if( isValid(v1, v2, v3) )
				{
					good = true;
				}
			}
			for( ll k = 0; !v3.empty(); k++ )
			{
				v2.push_back( v3.front() );
				v3.pop_front();
			}
		}
		cout << "Irun" << endl;
		if( good )
		{
			cout << "Case #" << i2 + 1 << ": YES" << endl;
		}else
		{
			cout << "Case #" << i2 + 1 << ": NO" << endl;
		}
	}*/
	ll casses;
	ll x, l;
	ll lCount;
	string equation;
	char letter;
	char temp;
	bool negative;
	cin >> casses;
	for( int i = 0; i < casses; i++ )
	{
		lCount = 0;
		cin >> x >> l;
		cin.ignore();
		cin >> equation;
		letter = 'i';
		negative = false;
		temp = equation.at(0);
		for( ll j = 1; j < equation.size(); addj( j, lCount, equation, l ) )
		{
			//cout << equation.at(j);
			
			//if( negative )
			//	cout << "-" << temp << endl;
			//else
			//	cout << temp << endl;
			
			if( letter != '1' && temp == letter )
			{
				if( letter == 'i' )
				{
					letter = 'j';
					//cout << "Run1" << endl;
					temp = equation.at(j);
				}else if( letter == 'j' )
				{
					letter = 'k';
					//cout << "Run2" << endl;
					temp = equation.at(j);
				}else if( letter == 'k' )
				{
					letter = '1';
					//cout << "Run3" << endl;
					temp = equation.at(j);
					
				}
			}else
			{
				mulLet( negative, temp, equation.at(j) );
			}
		}
		//cout << endl;
		//cout << letter << endl;
		//cerr << temp << endl;
		if( letter == '1' && temp == '1' && !negative || letter == 'k' && temp == 'k' && !negative )
			cout << "Case #" << i + 1 << ": " << "YES" << endl;
		else
			cout << "Case #" << i + 1 << ": " << "NO" << endl;
		
		
	}
	
	/*cin >> casses;
	for( int i = 0; i < casses; i++ )
	{
		for( ll j = 0; j <  )
	}*/
	return 0;
}
