/*input
1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3

*/

#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long int ull;
typedef long long int lli;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i = 0; i < n; i++)
#define INF    0x3f3f3f3f
#define NEGINF 0xC0C0C0C0
#define LINF   0x3f3f3f3f3f3f3f3fLL
#define all(v) v.begin(), v.end()
#define NULO -1
#define EPS 1e-10
#define PI 2 * acos(0)
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define F first
#define S second

inline int cmp(double x, double y = 0, double tol = EPS)
{ return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1; }

void arquivo()
{
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("B-small-attempt1.out", "wt", stdout);
}



map<vector<int>, int> todos;
vector<vector<int> > v;
int n;

bool pode(vector<int> a, vector<int> b)
{
	for(int i = 0; i < n; i++)
		if(b[i] <= a[i])
			return false;
	
	return true;
}

void print(vector<int> v)
{
	for(int i = 0; i < v.size(); i++)
		printf("%d ", v[i]);
	printf("\n");
}

bool solve(int id, vector<vector<int> > vAux)
{
	if(vAux.size() == n)
	{
		// for(auto v : vAux)
		// 	print(v);
		// printf("----\n");

		vector<int> aux[n];
		for(int i = 0; i < n; i++)
			aux[i].assign(n, 0);

		int totalNao = 0, id;
		set<vector<int> > usadosLinha;
		for(auto v : vAux)
			usadosLinha.insert(v);
		for(int j = 0; j < n; j++)
		{
			for(int i = 0; i < n; i++)
			{
				aux[j][i] = vAux[i][j];
			}		
		}

		for(int i = 0; i < n; i++)
		{
			
			if(usadosLinha.find(aux[i]) != usadosLinha.end() && todos[aux[i]] < 2)
			{
			
				// printf("entrei 1  ");
				// print(aux[i]);
				// printf("\n");
				totalNao++;
				id = i;
			}
			else if(usadosLinha.find(aux[i]) == usadosLinha.end() && !todos[aux[i]])
			{
				// printf("entrei 2 ");
				// print(aux[i]);
				// printf("\n");
				totalNao++;
				id = i;
			}

		}

		if(totalNao == 1)
		{
			for(int i = 0; i < n; i++)
				printf(" %d", aux[id][i]);
			return true;
		}
		return false;
	}

	for(int i = id + 1; i < 2 * n - 1; i++)
	{
		if(id == -1 || pode(v[id], v[i]))
		{
			vector<vector<int> > a = vAux;
			a.push_back(v[i]);
			if(solve(i, a))
				return true;
		}
	}
	return false;
}

int main()
{	
	arquivo();
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		todos.clear();
		v.clear();
		
		for(int i = 0; i < 2 * n - 1; i++)
		{
			vector<int> aux(n, 0);
			for(int j = 0; j < n; j++)
				scanf("%d", &aux[j]);

			v.push_back(aux);
			todos[aux]++;
		}

		
				
		sort(v.begin(), v.end());
		printf("Case #%d:", t);
		solve(-1, vector<vector<int> >());
		printf("\n");
		
	}
	return 0;
}


// for(auto aux : v)
// 		{
// 			for(int i = 0; i  < n; i++)
// 				printf("%d ", aux.vet[i]);
// 			printf("\n");
// 		}