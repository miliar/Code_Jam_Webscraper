
#include <set>
#include <vector>
#include <string>
#include <cstddef>
#include <iostream>
#include <algorithm>

using namespace std;

int senators[3];

void main2( )
{
    for( int& senator : senators )
    {
        senator = 0;
    }

    /// Input
    int N;
    cin >> N;

    int senator_count( 0 );

    for( int i( 0 ); i < N; ++i )
    {
        cin >> senators[i];
        senator_count += senators[i];
    }

    while( senator_count > 0 )
    {
		typedef std::pair<int, double> party_power;
		std::vector<party_power> parties_power(N, std::make_pair(-1, 0.0));
        for( int i( 0 ); i < N; ++i )
        {
            const double power( senators[i] / static_cast<double>( senator_count ) );

			parties_power[i].first = i;
			parties_power[i].second = power;
        }

		std::sort(std::begin(parties_power), std::end(parties_power), []( const party_power& lhs, const party_power& rhs ){
			return lhs.second > rhs.second;
		});

		bool all_even(true);
		int remaining_parties(0);
		for (int i(0); i < N; ++i)
		{
			remaining_parties += senators[i] > 0 ? 1 : 0;
		}
		for (int i(1); i < N; ++i)
		{
			all_even &= senators[i] == senators[0];
		}

		cout << " ";
		if(remaining_parties > 2)
		{
			if (!all_even)
			{
				if (parties_power[0].second > 0.0)
				{
					const int idx(parties_power[0].first);
					const char party('A' + idx);
					cout << party;
					--senators[idx];
					--senator_count;
				}
				if (parties_power[1].second > 0.0)
				{
					const int idx(parties_power[1].first);
					const char party('A' + idx);
					cout << party;
					--senators[idx];
					--senator_count;
				}
			}
			else
			{
				if (parties_power[0].second > 0.0)
				{
					const int idx(parties_power[0].first);
					const char party('A' + idx);
					cout << party;
					--senators[idx];
					--senator_count;
				}
			}
		}
		else
		{
			if (parties_power[0].second > 0.0)
			{
				const int idx(parties_power[0].first);
				const char party('A' + idx);
				cout << party;
				--senators[idx];
				--senator_count;
			}
			if (parties_power[1].second > 0.0)
			{
				const int idx(parties_power[1].first);
				const char party('A' + idx);
				cout << party;
				--senators[idx];
				--senator_count;
			}
		}
    }

    cout << endl;
} 

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t(1); t <= T; ++t)
    {
        cout << "Case #" << t << ":";
        main2( );
    }
    return 0;
}
