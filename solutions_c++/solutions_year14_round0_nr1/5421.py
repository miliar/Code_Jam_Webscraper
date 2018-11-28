#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;

int main()
{
  int N;
  cin >> N;
  for (int caso = 1; caso <= N; caso++)
  {
    cout << "Case #" << caso << ": ";
    VB pos (16, true);
    fi(2)
    {
      int row;
      cin >> row;
      row--;
      fj(4)
      {
	fk (4)
	{
	  int x;
	  cin >> x;
	  if (j != row) pos[x-1] = false;
	}
      }
    }
    int sm = 0;
    fi (16) if (pos[i]) sm++;
    if (sm == 0) cout << "Volunteer cheated!" << endl;
    else if (sm > 1) cout << "Bad magician!" << endl;
    else fi (16) if (pos[i]) cout << i+1 << endl;
  }
}