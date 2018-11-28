#include <iostream>
#include <vector>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int main ()
{
  int tab[4][4];
  int T;
  cin >> T;
  for(int cas=0; cas<T;cas++)
    {
      vector<int> v;
      v.clear();
      int a,b;
      cin >> a;
      a--;
      for(int i =0; i<4;i++)
	{
	  for(int j =0; j<4;j++)
	    {
	      cin >> tab[i][j];
	    }
	}
      for(int i =0; i<4;i++)
	{
	  v.push_back(tab[a][i]);
	}
      cin >> b;
      b--;
      for(int i =0; i<4;i++)
	{
	  for(int j =0; j<4;j++)
	    {
	      cin >> tab[i][j];
	    }
	}
      int r =0;
      int res =0;
      rep(i,4)
	{
	  rep(j,4)
	    {
	      if (tab[b][j]==v[i])
		{
		  r +=1;
		  res=v[i];
		    
		}
	    }
	}
      if (r==0)
	cout <<"Case #" << cas+1 << ": Volunteer cheated!" <<  endl;
      if (r==1)
	cout << "Case #" << cas+1 << ": " << res << endl;
      if (r>1)
	cout << "Case #" << cas+1 << ": Bad magician!"  << endl;
    }
}
