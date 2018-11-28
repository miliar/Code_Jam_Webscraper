#include <bits/stdc++.h>

using namespace std;

const int N = 1000000;
const int M = 10*N;

int inv(int n)
{
   int r = 0;
   while(n)
   {
      r = 10*r + n%10;
      n /= 10;
   }
   return r;
}

/*int dyn[N+1];

void chemin(int n)
{
	if(n == 0)
	{
		cout << endl;
		return;
	}
	cout << n << " ";
	int x = inv(n);
	if(x < n && dyn[x] < dyn[n-1])
		chemin(x);
	else
		chemin(n-1);
}*/

int nbVus;
int t[M];

int main()
{
   queue< pair<int, int> > file;
   file.push(make_pair(0, 0));
   while(nbVus <= N+1)
   {
      pair<int, int> top = file.front();
      file.pop();
      if(top.first > M) //espérons
      {
         cerr << "Alerte" << endl;
         continue;
      }
      if(t[top.first])
         continue;
      t[top.first] = top.second;
      if(top.first <= N)
         nbVus++;
      file.push(make_pair(inv(top.first), top.second+1));
      file.push(make_pair(top.first+1, top.second+1));
   }
   /*for(int i=1; i<=N; i++)
      dyn[i] = 1 + min(dyn[i-1], inv(i) < i ? dyn[inv(i)] : N);*/
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      int x;
      cin >> x;
      //chemin(x);
      printf("Case #%d: %d\n", test, t[x]);
   }
   return 0;
}