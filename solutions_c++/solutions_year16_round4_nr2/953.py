#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;

double a[3000];
double ans;
double b[3000];
double p[300][300];
  int k;

double cnt()
{
  memset(p,0,sizeof(p));
  p[0][0] = 1;
  for (int i = 0; i < k; i++)
    {
      for (int j = 0; j <= i; j++)
	{
	  p[i+1][j] += p[i][j] * b[i];
	  p[i+1][j + 1] += p[i][j] * (1-b[i]);
	}
    }
  return p[k][k/2];
}

int main()
{
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  int t;
  cin >> t;
  for (int i =0;i < t; i++)
    {
      int n;
      cin >> n >> k;
        for (int j = 0; j < n; j++) cin >> a[j];
        sort(a, a+n);
	  cout << "Case #" << i+1<< ": ";
	  ans = 0;
	  for (int j = 0; j <= k; j++)
	    {
	      for (int l = 0; l < j; l++) b[l] = a[l];
	      for (int l = 0; l < k-j; l++) b[j +l] = a[n - (k-j) + l];
	      double ret = cnt();
	      //for (int l = 0; l < k; l++) cout << b[l] << " ";
	      //cout << endl;
	      if (ret > ans) ans = ret;
	    }
	  printf("%.6lf\n", ans);
    }
}
