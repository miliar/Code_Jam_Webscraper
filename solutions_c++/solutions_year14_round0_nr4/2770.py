#include <iostream>
#include <string>
#include <vector>
//#include <boost/multiprecision/cpp_int.hpp>
#include <math.h>
#include <typeinfo>
#include <algorithm>
using namespace std;
typedef vector<double> vdouble;

template <class T>
std::vector<T> readarray(int n)
{
    std::vector<T> v;
    for (int i = 0; i < n; ++i)
    {
        T k;
        cin >> k;
        v.push_back(k);
    }
    return v;
}

template <typename T> 
const bool Contains( std::vector<T>& Vec, const T& Element ) 
{
    if (std::find(Vec.begin(), Vec.end(), Element) != Vec.end())
        return true;

    return false;
}


int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) 
	{
		int N;
		cin >> N;

		auto Nnaomi = readarray<double>(N);
		sort(Nnaomi.begin(),Nnaomi.end());
		// Ascending order

		auto Nken = readarray<double>(N);
		sort(Nken.begin(),Nken.end());
		// Ascending order

		int warNaomiWon = 0;
		// Desc order
		for(auto itNaomiDesc = Nnaomi.rbegin(), itKenDesc = Nken.rbegin(); 
				itNaomiDesc != Nnaomi.rend(); 
				itNaomiDesc++)
		{
			if (*itKenDesc < *itNaomiDesc)
			{
				warNaomiWon++;
			}
			else
			{
				itKenDesc++;
			}
		}

#if 0
		auto blocks = Nnaomi;
		blocks.insert( blocks.end(), Nken.begin(), Nken.end() );
		sort(blocks.begin(),blocks.end());

		for(int i = 0; i< 2*N;i++)
		{
			auto x = blocks[i];
			cout << x << " ";
			if (Contains( Nnaomi, x ))
				cout << "N";
			else
				cout << "K";
			cout << endl;
		}
		cout << endl;
#endif

		int decWarNaomiWon = 0;

		auto itNaomiDesc = Nnaomi.rbegin(); 
		auto itKenDesc = Nken.rbegin();
		for(; itKenDesc != Nken.rend(); itKenDesc++)
		{
			if (*itKenDesc < *itNaomiDesc)
			{
				decWarNaomiWon++;
				itNaomiDesc++;
			}
			else
			{
			}
		}

		cout << "Case #" << (t+1) << ": " << decWarNaomiWon << " " << warNaomiWon << endl;
	}
	return 0;
}


