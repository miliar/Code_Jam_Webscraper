#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>
#include <sstream>
#include <set>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 1e-14
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
typedef vector<string> VS;
typedef map<char,int> MCI;
typedef vector<PD> VPD;
typedef map<string, int> MSI;
typedef set<int> SI;

VVI fr;
VI fra, eng;
int n;

int back (int a)
{
  if (a == n)
  {
    int ans = 0;
    fi (fra.size())
      if (fra[i] > 0 and eng[i] > 0) ans++;
    return ans;
  }
  int ans = fra.size();
  fi (fr[a].size())
  {
    fra[fr[a][i]]++;
  }
  
  ans = min (ans, back(a+1));
  
  fi (fr[a].size())
  {
    fra[fr[a][i]]--;
    eng[fr[a][i]]++;
  }
  
  ans = min (ans, back(a+1));
  fi (fr[a].size())
  {
    eng[fr[a][i]]--;
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    cin >> n;
    MSI dic;
    fr = VVI(n);
    string s;
    getline(cin,s);
    fi (n)
    {
      getline(cin,s);
      stringstream ss(s);
      while (ss >> s)
      {
        if (dic.find(s) == dic.end())
        {
          int np = dic.size();
          dic[s] = np;
        }
        fr[i].push_back(dic[s]);
      }
    }
    
    eng = fra = VI(dic.size());
    fi (fr[0].size()) eng[fr[0][i]]++;
    fi (fr[1].size()) fra[fr[1][i]]++;
    
    cout << back(2) << endl;
  }
}