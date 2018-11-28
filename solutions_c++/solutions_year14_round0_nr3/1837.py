#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <algorithm>

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

int di[8] = {1,1,1,0,0,-1,-1,-1};
int dj[8] = {1,0,-1,1,-1,1,0,-1};

int main()
{
  int N;
  cin >> N;
  for (int caso = 1; caso <= N; caso++)
  {
    cout << "Case #" << caso << ":" << endl;
    int R, C, M;
    cin >> R >> C >> M;
    if (R*C == M+1)
    {
      cout << 'c';
      fi (C-1) cout << '*';
      cout << endl;
      fi (R-1) 
      {
        fj(C) cout << '*';
        cout << endl;
      }
      continue;
    }
    bool pos = false;
    VI v (R*C,0);
    fi (M) v[i] = -1;
    sort(v.begin(),v.end());
    do
    {
      VVI tab (R, VI (C));
      fi (R) fj(C) tab[i][j] = v[i*C+j];
      fi (R) fj(C) 
      {
	if (tab[i][j] == -1) continue;
	fk (8)
	{
	  int ni = i + di[k];
	  int nj = j + dj[k];
	  if (ni < 0 or ni >= R or nj < 0 or nj >= C) continue;
	  if (tab[ni][nj] == -1) tab[i][j]++;
	}
      }
      int ci,cj;
      ci = cj = -1;
      fi (R) fj(C)
      {
	if (tab[i][j] != 0) continue;
	ci=i;cj=j;
      }
      if (ci == -1) continue;
      VVI vis (R, VI (C,false));
      QI q;
      q.push(ci);
      q.push(cj);
      vis[ci][cj] = true;
      while (not q.empty())
      {
	int ai = q.front();
	q.pop();
	int aj = q.front();
	q.pop();
	fk (8)
	{
	  int ni = ai + di[k];
	  int nj = aj + dj[k];
	  if (ni < 0 or ni >= R or nj < 0 or nj >= C) continue;
	  if (vis[ni][nj]) continue;
	  vis[ni][nj] = true;
	  if (tab[ni][nj] == 0)
	  {
	    q.push(ni);
	    q.push(nj);
	  }
	}
      }
      bool ok = true;
      fi (R) fj (C)
	if (tab[i][j] >= 0 and not vis[i][j]) ok = false;
      if (ok)
      {
        pos = true;
        fi (R)
        {
          fj(C)
          {
            if (tab[i][j] == -1) cout << '*';
            else if (i == ci and j == cj) cout << 'c';
            else cout << '.';
          }
          cout << endl;
        }
      }
    }while (not pos and next_permutation(v.begin(),v.end()));
    if (not pos) cout << "Impossible" << endl;
  }
}