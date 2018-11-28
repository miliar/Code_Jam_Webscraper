#include <iostream>
#include <vector>
using namespace std;

bool check_col(vector< vector< unsigned > > & lawn, unsigned & N, unsigned & M, unsigned &h, unsigned & m)
{
	for(unsigned i = 0; i < N; ++i)
	{
		if(lawn[i][m] > h) return false;
	}
	return true;
}


bool check_row(vector< vector< unsigned > > & lawn, unsigned & N, unsigned & M, unsigned &h, unsigned & n)
{
	for(unsigned j = 0; j < M; ++j)
	{
		if(lawn[n][j] > h) return false;
	}
	return true;
}

bool cut(vector< vector< unsigned > > & lawn, unsigned & N, unsigned & M)
{
	unsigned i = 0;
	unsigned j = 0;
	for(; i < N; ++i)
	{
		for(j = 0; j < M; ++j)
		{
			if (!(check_row(lawn, N, M, lawn[i][j], i) || check_col(lawn, N, M, lawn[i][j], j))) return false;		
		}
	}	

	return true;

}

void outp(vector< vector< unsigned > > & lawn, unsigned & N, unsigned & M, unsigned i)
{
	cout << "Case #" << i << ": ";
	if(cut(lawn, N, M))
	{
		cout << "YES";
	}
	else
	{
		cout << "NO";
	}

}

vector < vector< unsigned > > make_lawn(const unsigned & N, const unsigned & M)
{
	vector < vector<unsigned> > lawn;
	vector<unsigned> v;
	unsigned height;
	for(unsigned i = 0; i < N; ++i)
	{
		v.clear();
		for(unsigned j = 0; j < M; ++j)
		{
			cin >> height;
			v.push_back(height);
		}
		lawn.push_back(v);
	}		
	return lawn;	
}



int main()
{
	unsigned T, N, M;
	cin >> T;
	vector< vector<unsigned> > lawn;
	unsigned ntl = T-1;
	for(unsigned i = 0; i < T; ++i)
	{
		cin >> N >> M;
		lawn = make_lawn(N, M);
		outp(lawn, N, M, i+1);
		if(i < ntl) cout << endl;
	}
	return 0;
}
