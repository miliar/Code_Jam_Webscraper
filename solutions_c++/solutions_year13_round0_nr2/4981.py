#include <iostream>
#include <vector>

using namespace std;

int p[100+1][100+1];
int N,M;


int min()
{
	int min=p[0][0];
	for (int i=0;i<N;i++)
	{
		for (int j=0;j<M;j++)
		{
			if (p[i][j] < min)
				min = p[i][j];
			
		}
	}
	return min;	
}

vector<int> band(int h, bool horiz)
{
	vector<int> res;
	for (int i=0; i<(horiz?N:M); i++)
	{
		for (int j=0; j<(horiz?M:N); j++)
			if (p[(horiz?i:j)][(horiz?j:i)] != h)
				goto next;
		res.push_back(i);
next:;
	}
	return res;
}

void inc(int i, int h, bool horiz)
{
	for (int j=0; j<(horiz?M:N); j++)
	{
		if(p[(horiz?i:j)][(horiz?j:i)] != h && p[(horiz?i:j)][(horiz?j:i)] != h+1)
		{
			cout << "wrong height " << i << " " << j  << endl;
			for (int i=0; i<M; i++)
			{
				for (int j=0; j<M; j++) cout << p[i][j]<< " ";
				cout << endl;
			}
			exit(0);
		}
		p[(horiz?i:j)][(horiz?j:i)] = h+1;
	}
}

void solve()
{
    vector<int> rows;
    vector<int> cols;
    do
    {
	int h = min();
	if (h == 100)
	{
		cout << "YES";
		return;
	}
	rows = band(h,true);
	cols = band(h,false);
	for (int i=0;i<rows.size();i++)
		inc(rows[i],h,true);
	for (int i=0;i<cols.size();i++)
		inc(cols[i],h,false);
    } while (rows.size()>0 || cols.size()>0);	
    cout << "NO";
}


int main(int argc, char* argv[])
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		cin >> N >> M;
		for (int i=0;i<N;i++)
		{
			for (int j=0;j<M;j++)
			{
				cin >> p[i][j];
			}
		}

		cout << "Case #" << (t+1) << ": ";
		solve(); 
		cout << endl;		

	}
	return 0;
}
