#include <iostream>
#include <vector>

using namespace std;

void getCiph(vector<int>& ciph, int n)
{
	
	ciph.clear();
	do
	{
		int x = n%10;
		n /= 10;
		ciph.push_back(x);
	}
	while(n > 0);
	
}

void setFalse(vector<bool>& v)
{
	for(unsigned i=0; i<v.size(); i++) v[i] = false;
}

void mark(vector<bool>& found, const vector<int>& ciph)
{
	for(int x : ciph)
	{
		found[x] = true;
	}
}

bool allMarked(const vector<bool>& found)
{
	for(bool b : found) if(!b) return false;
	return true;
}

int main()
{
	unsigned nn;
	cin >> nn;
	vector<int> ciph;
	vector<bool> found(10);
	for(unsigned kk=1; kk<=nn; kk++)
	{
		
		int n;
		cin >> n;
		
		if(n == 0)
		{
			cout << "Case #" << kk << ": " << "INSOMNIA" << endl;
			continue;
		}
		
		
		setFalse(found);
		
		int res = n;
		
		do
		{
			getCiph(ciph, res);
			mark(found, ciph);
			if(allMarked(found)) break;
			res += n;
		}
		while(true);
		
		cout << "Case #" << kk << ": " << res << endl;
		
	}
}
