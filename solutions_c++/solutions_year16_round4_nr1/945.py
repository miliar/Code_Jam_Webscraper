#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int u[100];
int v[100];
int r[100];
int ans[100][3][100];

int check(int u)
{
  if (u == 0) return 1;
  if (u == 1) return 0;
  if (u == 2) return 2;
}

int main()
{
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int t;
  cin >> t;
  for (int i = 0; i < t; i++)
    {
      int a,b,c,nn;
      cin >> nn >> a >> b >> c;
      int n = 1;
      for (int j = 0; j < nn; j++) n=n*2;
      cout << "Case #" << i + 1<< ": ";
      bool fl = true;
      int d,e,f;
      d = a;
      e = b;
      f = c;
      int pu;
      for (int j = 0; j < nn; j++)
	{
	  int dd,ee,ff;
	  u[j] = d;
	  v[j] = e;
	  r[j] = f;
	  dd = (d + f - e)/2;
	  ee = (d+e-f) /2;
	  ff = (e+f-d)/2;
	  if (dd <0 || ee <0 || ff < 0) {fl = false; break;}
	  d = dd;
	  e = ee;
	  f = ff;
	  if (d != 0) pu =0;
	  if (e !=0) pu = 1;
	  if (f!=0) pu = 2;
	}
      if (fl == false) cout << "IMPOSSIBLE\n"; 
      else{
	int oo = 1;
	for (int j = 0; j < 3; j++) ans[0][j][0] = j;
	for (int j =0 ;j < nn;j++)
	  {
	    for (int k = 0; k < 3; k++)
	      {
		int kk = (k + 2)%3;
		bool fl = true;
		for (int l = 0; l < oo; l++) 
		  {
		    if (check(ans[j][k][l]) < check(ans[j][kk][l])) {fl = false; break;}
		    if (check(ans[j][k][l]) > check(ans[j][kk][l])) break;
		  }
		if (fl == true) 
		  for (int l = 0; l < oo; l++)
		    {
		      ans[j+1][k][l] = ans[j][kk][l];
		      ans[j+1][k][l+oo] = ans[j][k][l];
		    }
		else 
		  for (int l = 0; l < oo; l++)
		    {
		      ans[j+1][k][l] = ans[j][k][l];
		      ans[j+1][k][l+oo] = ans[j][kk][l];
		    }
	      }
	    oo = oo*2;
	  }
	for (int j = 0; j < n; j++) 
	  {
	    int g = ans[nn][pu][j];
	    if (g == 0) cout << "R";
	    if (g == 1) cout << "P";
	    if (g == 2) cout << "S";
	    
	  }
	cout << "\n";
      }
    }
}
