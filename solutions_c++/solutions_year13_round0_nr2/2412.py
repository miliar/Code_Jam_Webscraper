#include <cstdio>
#include <set>

using namespace std;

int mat[123][123];
bool pode[123][123];

int main(void)
{
  int N;
  scanf("%d\n", &N);
  for(int cas = 1; cas <= N; cas++)
  {
    int n, m;
    set<int> st;

    scanf("%d %d\n", &n, &m);
    for(int i = 0; i < n; i++)
    {
      for(int j = 0; j < m; j++)
      {
        int p;
        scanf("%d\n", &p);
        mat[i][j] = p;
        st.insert(p);

        pode[i][j] = false;
      }
    }

    while(!st.empty())
    {
      int pv = *st.begin();
      st.erase(st.begin());
      for(int i = 0; i < n; i++)
      {
        bool vai = true;
        for(int j = 0; j < m; j++)
        {
          vai &= (mat[i][j] == pv || mat[i][j] == 0);
        }

        if(vai)
        {
          for(int j = 0; j < m; j++) mat[i][j] = 0;
        }
      }

      for(int i = 0; i < m; i++)
      {
        bool vai = true;
        for(int j = 0; j < n; j++)
        {
          vai &= (mat[j][i] == pv || mat[j][i] == 0);
        }

        if(vai)
        {
          for(int j = 0; j < n; j++) mat[j][i] = 0;
        }
      }
    }
    
    bool res = true;        

    for(int i = 0; i < n; i++)
    {
      for(int j = 0; j < m; j++)
      {
        res &= mat[i][j] == 0;
      }
    }

    printf("Case #%d: %s\n", cas, res ? "YES" : "NO");

  }

  return 0;
}
