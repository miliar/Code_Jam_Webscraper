#include <iostream>
#include <vector>
#include <string>
using namespace std;

bool test2(int i, int k, int di, int dk, vector<string> &v)
{
	while (true)
	{
		i += di; k += dk;
		if (i < 0) return false;
		if (k < 0) return false;
		if (i >= v.size()) return false;
		if (k >= v[0].length()) return false;
		if (v[i][k] != '.') return true;
	}
}

bool test1(int i, int k, int d, vector<string> &v)
{
	switch (d)
	{
	case 0: 
		return test2(i, k, -1, 0, v);
		break;
	case 1: 
		return test2(i, k, 0, 1, v);
		break;
	case 2: 
		return test2(i, k, 1, 0, v);
		break;
	case 3: 
		return test2(i, k, 0, -1, v);
		break;
	}
	return false;
}

int test(int i, int k, int d, vector<string> &v)
{
	if (test1(i, k, d, v)) return 0;
	else for (int dd = 0; dd<4; dd++)
	{
		if (dd != d)
			if (test1(i, k, dd, v)) return 1;
	}
	return -1;
}


int main()
{
  string str = "^>v<";
  int T; cin >> T;
  for (int ii = 0; ii<T; ii++)
  {
    int r, c; cin >> r >> c;
    vector<string> v(r);
    
    for (int i=0; i<r; i++)
    {
      cin >> v[i];
    }  
    
    int count = 0;
    for (int i=0; (i<r) && (count >= 0); i++)
    {
    	for (int k=0; (k<c) && (count >= 0); k++)
    	{
    		if (v[i][k] != '.')
    		{
    			int d = str.find(v[i][k]);
    			int delta = test(i, k, d, v);
    			if (delta < 0) count = -1;
    			else count += delta;
    		} 
    	}
    }	
    if (count < 0)
    	cout << "Case #" << ii+1 << ": " << "IMPOSSIBLE" << endl;
    else	
    	cout << "Case #" << ii+1 << ": " << count << endl;
  }
  return 0;
}
