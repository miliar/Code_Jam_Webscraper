#include <vector>
#include <iostream>

using namespace std;

int A[2000];
int B[2000];
int seq[2000];
int nin[2000];
vector<int> edges[2000];

void doCase()
{
	int N;
	
	cin >> N;
	
	for (int i=0; i<N; i++)
		cin >> A[i];
	for (int i=0; i<N; i++)
		cin >> B[i];
	for (int i=0; i<N; i++)
		edges[i].clear();
	for (int i=0; i<N; i++)
		nin[i] = 0;
	bool occured = true;
	for (int i=1; occured; i++)
	{
		occured = false;
		int lastPlay = -1;
		int lastSlay = -1;
		for (int j=0; j<N; j++)
		{
			if (A[j] == i-1)
				lastPlay = j;
			if (A[j] != i)
				continue;
			
			occured = true;
			
			if (lastPlay != -1)
			{
				edges[lastPlay].push_back(j);
				nin[j]++;
			}
			if (lastSlay != -1)
			{
				edges[j].push_back(lastSlay);
				nin[lastSlay]++;
			}
			lastSlay = j;
		}
	}
	
	occured = true;
	for (int i=1; occured; i++)
	{
		occured = false;
		int lastPlay = -1;
		int lastSlay = -1;
		for (int j=N-1; j>=0; j--)
		{
			if (B[j] == i-1)
				lastPlay = j;
			if (B[j] != i)
				continue;
			occured = true;
			
			if (lastPlay != -1)
			{
				edges[lastPlay].push_back(j);
				nin[j]++;
			}
			if (lastSlay != -1)
			{
				edges[j].push_back(lastSlay);
				nin[lastSlay]++;
			}
			lastSlay = j;
		}
	}
	
	for (int i=0; i<N; i++)
	{
		for (int j=0; j<N; j++)
		{
			if (nin[j])
				continue;
			
			for (int k=0; k<edges[j].size(); k++)
			{
				nin[edges[j][k]]--;
			}
			
			seq[j] = i+1;
			nin[j] = -1;
			
			break;
		}
	}
	
	for (int i=0; i<N; i++)
	{
		if (i)
			cout << " ";
		cout << seq[i];
	}
	cout << endl;
}


int main()
{
	int T;
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cout << "Case #" << i << ": ";
		doCase();
	}
	return 0;
}
