#include<iostream>
#include<string>

using namespace std;

class quaternion
{
	public:
	bool signe;
	char value;
	quaternion( const char a ) : signe(false) , value(a) {}
	quaternion product(const char , const char);
	void operator*(const quaternion  & A) 
	{
		quaternion tmp =	product(value , A.value );
		value = tmp.value;
		signe = tmp.signe ^ ( signe ^ A.signe );
	}
};

quaternion quaternion::product( const char a , const char b )
{
	bool sign(false);
	char out;
	if(a == '1' || b == '1')
	{
		if(a == '1')
			out = b;
		else
			out = a;
	}
	else
	{
		if(a == 'i')
		{
			if(b == 'i')
			{
				out = '1';
				sign = true;
			}
			else if( b == 'j')
				out = 'k';
			else 
			{
				out = 'j';
				sign = true;
			}
		}
		else if(a == 'j')
		{
			if(b == 'i')
			{
				out = 'k';
				sign = true;
			}
			else if( b == 'j')
			{
				out = '1';
				sign = true;
			}
			else 
			{
				out = 'i';
			}
		}
		else
		{
			if(b == 'i')
			{
				out = 'j';
			}
			else if( b == 'j')
			{
				out = 'i';
				sign = true;
			}
			else 
			{
				out = '1';
				sign = true;
			}
		}
	}
		quaternion tmp(out);
		tmp.signe = sign;
		return tmp;
}
													
int main()
{
	std::ios::sync_with_stdio(false);
	int T;
	cin >>T;
	for( int t(1); t <= T ; ++t)
	{
		//init
		int L,X;
		cin >> X >> L;
		string elem;
		cin >> elem;
		string data(elem);
		for(int i(0) ; i < L-1; ++i)
		 data += elem;

		//cout << data << "\n";
		//Processing
		L*=X;
		quaternion i('1'), tmp('1');
		int it(0);
		bool cond(true);
		while( it < L-2  && cond)
		{
			tmp.value = data[it] ;
			i*tmp;
			if(i.value == 'i' && !i.signe )
			{
				quaternion j('1');
				int it2(it+1);
				while(it2 < L-1  && cond)
				{
					tmp.value = data[it2];
					j*tmp;
					if(j.value == 'j' && !j.signe )
					{
						quaternion k('1');
						for(int it3(it2 +1); it3 <L; ++it3)
						{
							tmp.value = data[it3];
							k*tmp;
						}
						if(k.value == 'k' && !k.signe )
						{
							cond = false;
						}
					}
					it2++;
				}
			}
			it++;
		}
		if(cond)
		{
			cout <<"Case #" << t <<": NO\n";
		}
		else
		{
			cout <<"Case #" << t <<": YES\n";
		}
	}
	return 0;
}
