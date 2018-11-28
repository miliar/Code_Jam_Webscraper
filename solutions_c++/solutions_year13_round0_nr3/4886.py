#include<fstream>
#include<iostream>
#include<sstream>
using namespace std;
bool IsFair(int a)
{
	ostringstream strst;
	strst << a;
	string st = strst.str();
	for (int i=0;i<sqrt(st.length());i++)
	{
		if (st[i]!=st[st.length()-i-1])
			return false;
	}
	return true;
}
inline bool IsSqrt(int j)
{
	int k = static_cast<int>(sqrt(j));
	return (j==k * k);
}
void main()
{
	ifstream _in("in.txt");
	ofstream _out("out.txt");
	if (_in && _out)
	{
		int T;
		_in >> T;
		for (int i=0;i<T;i++)
		{
			int a, b;
			_in >> a >> b;
			int sum = 0;
			for (int j=a;j<b+1;j++)
			{
				if (IsFair(j) && IsSqrt(j) && IsFair(sqrt(j)))
					sum++;
			}
			_out << "Case #" << i+1 << ": " << sum << endl;
		}
	}//if
}