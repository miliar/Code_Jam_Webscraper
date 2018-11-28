#include <iostream>

#define MAX_S 4
char l[MAX_S];
char c[MAX_S];
char mat[MAX_S][MAX_S];
char d[2];
//N none
//D draw
//X p x
//O p o
using namespace std;
int main()
{
  int T = 1;
  int n;
  char win;
  bool comp;
  cin >> T;
  for(int k = 1; k <= T;k++)
    {
      for(int i = 0; i < MAX_S;i++)
	{
	  l[i] = c[i] = 'N';
	  for(int j = 0; j < MAX_S;j++)
	    {
	      cin >> mat[i][j];
	    }
	}
      comp = true;
      for(int i = 0; i < MAX_S;i++)
	{
	  for(int j = 0; j < MAX_S;j++)
	    {
	      
	      if(mat[i][j] == '.')
		{
		  comp = false;
		  l[i] = c[j] = 'D';
		}
	      else
		{
		  if(l[i] == 'N' && mat[i][j] != 'T')
		    l[i] = mat[i][j];
		  else if(l[i] != mat[i][j] && mat[i][j] != 'T')
		    {
		      l[i] = 'D';
		    }

		  if(c[j] == 'N' && mat[i][j] != 'T')
		    c[j] = mat[i][j];
		  else if(c[j] != mat[i][j]  && mat[i][j] != 'T')
		    {
		      c[j] = 'D';
		
		    }
		}

	      
	      
	    }
	}
      win = 'D';
      for(int i = 0; i < MAX_S && win == 'D';i++)
	{
	  if(l[i] == 'X' || l[i] == 'O')
	    win = l[i];
	  else if(c[i] == 'X' || c[i] == 'O')
	    win = c[i];
	}

      
      if(win == 'D')
	{
	  d[0] = d[1] = 'N';
	  for(int i = 0; i < MAX_S;i++)
	    {
	      if(d[0] == 'N' && mat[i][i] != 'T') d[0] = mat[i][i];
	      else if( mat[i][i] != 'T' && d[0] != mat[i][i] )
		d[0] = 'D';

	      if(d[1] == 'N' && mat[i][MAX_S-1-i] != 'T') d[1] = mat[i][MAX_S-1-i];
	      else if( mat[i][MAX_S-1-i] != 'T' && d[1] != mat[i][MAX_S-1-i] )
		d[1] = 'D';
	    }
	  if(d[0] == 'X' || d[0] == 'O')
	    win = d[0];
	  else if(d[1] == 'X' || d[1] == 'O')
	    win = d[1];	  
	}
      
      cout << "Case #" << k << ": ";
      if(win != 'D' && win != 'N' && win != 'T' && win != '.')
	{
	  cout << win << " won" << endl;
	}
      else if (comp)
	{
	  cout << "Draw" << endl;
	}
      else
	{
	  cout << "Game has not completed" << endl;
	}
    }
}
