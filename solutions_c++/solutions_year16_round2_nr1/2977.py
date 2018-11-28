#include <bits/stdc++.h>
using namespace std;

ifstream f("wow.in");
ofstream g("wow.txt");

string A[]={
		"NINE",
		"ZERO",
		"SIX",
		"EIGHT",
		"TWO",
		"FIVE",
		"THREE",
		"FOUR",
		"SEVEN",
		"ONE"
};

#define cout g

int cif[]={
		9,
		0,
		6,
		8,
		2,
		5,
		3,
		4,
		7,
		1
};

#define pb push_back
#define mp make_pair

string str;
int fr_good[666],aux[666];

template < class T >
std::ostream& operator << (std::ostream& os, const std::vector<T>& v)
{
    for (typename std::vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii)
    {
        os << *ii;
    }
    return os;
}

vector<int> result;


int main()
{
	int nrt;
	f>>nrt;

	for (int tt=1;tt<=nrt;++tt)
	{
		cout<<tt<<'\n';
		f>>str;

		for(auto &it:str) fr_good[it]++;

		int Nmax=str.length()/3;

		for(int i=0;i<=Nmax;++i)
			if (fr_good['N']>=i*2&&fr_good['I']>=i&&fr_good['E']>=i)
			{
				result.clear();
				for(int j=1;j<=i;++j) result.pb(9);

				for(int j='A';j<='Z';++j) aux[j]=fr_good[j];

				aux['N']-=i*2;
				aux['I']-=i;
				aux['E']-=i;


				for(int j=1;j<=9;++j)
				{
					while (true)
					{
						bool okz=true;

						for(auto &it:A[j])
							if (aux[it]==0)
								okz=false;

						if (okz==false) break;


						result.pb(cif[j]);
						for(auto &it:A[j]) aux[it]--;
					}
				}


				    bool okz=true;
					for(int j='A';j<='Z';++j) if (aux[j]) okz=false;

					if (okz)
					{
						sort(result.begin(),result.end());
						cout<<"Case #"<<tt<<": "<<result<<'\n';
						break;
					}
			}

		for(auto &it:str) fr_good[it]--;


	}
	return 0;
}
