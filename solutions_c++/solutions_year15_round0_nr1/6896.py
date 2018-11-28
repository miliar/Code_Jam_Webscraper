#include <fstream>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
	private:
		int s_max;
		string audience;
	public:
		Solution( int m, string a ) : s_max(m), audience(a) {}
		void Set( int m, string a )
		{
			s_max = m;
			audience = a;
		}
		int MinimumFriends()
		{
			if ( s_max == 0 )
				return 0;
			int cur_f = 0;
			int cur_clap = 0;
			for ( size_t i = 0; i <= s_max; ++ i )
			{
				if ( audience[i] > '0' )
				{
					if ( i <= cur_clap )
						cur_clap += audience[i] - 48;
					else
					{
						cur_f += i - cur_clap;
						cur_clap += i - cur_clap + audience[i] - 48;
					}
				}
			}
			return cur_f;	
		}
};

int main()
{
	ifstream ifs;
	ofstream ofs;
	ifs.open( "A-large.in", ios::in );
	ofs.open( "A-large.out", ios::out );
	int t;
	ifs >> t;
	Solution s( 0, "" );
	int count = 0;
	while ( t -- )
	{
		++ count;
		int max_m;
		string audience;
		ifs >> max_m >> audience;
		s.Set( max_m, audience );
		int result = s.MinimumFriends();
		ofs << "Case #" << count << ": " << result << endl;
	}
	ifs.close();
	ofs.close();
}
