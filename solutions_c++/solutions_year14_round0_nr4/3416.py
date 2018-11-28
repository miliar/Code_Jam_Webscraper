#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

#define rep(i,n) for (int i = 0; i<n; i++)

using namespace std;

vector<double> A;
vector<double> B;
int n;

int resD; int resW;

void getInput()
{
  A.clear(); B.clear();
  double a,b;
  rep(i,n)
    {
      cin >> a;
      A.push_back(a);
    }
  rep(i,n)
    {
      cin >> b;
      B.push_back(b);
    }
}

void solve()
{
  sort(A.begin(),A.end());
  sort(B.begin(),B.end());
  resD=0;
  resW=0;
  int Abegin = 0; int Aend = n-1;  int Bbegin = 0; int Bend = n-1;
  rep(i,n)
    {
      if (A[Abegin] > B[Bbegin])
	{
	  Abegin++;
	  Bbegin++;
	  resD++;
	}
      else
	{
	  Abegin++;
	  Bend--;
	}
    }

  Abegin = 0;  Aend = n-1;   Bbegin = 0;  Bend = n-1;
    rep(i,n)
    {
      if (A[Aend] > B[Bend])
	{
	  Aend --;
	  Bbegin++;
	  resW++;
	}
      else
	{
	  Aend--;
	  Bend--;
	  
	}

    }
}


int main(int arc, char* arv[])
{
  int T;
  cin >> T;
  rep(c,T)
    {
      cin >> n;
      getInput();
      solve();
      cout << "Case #" << c+1 << ": " << resD << " " << resW << endl;
    }
}
