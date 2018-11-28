#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <ctime>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
#define REP(i, a, b) for(int i = int(a); i <= int(b); i++)
#define LOOP(i, v) for(int i = 0; i < v.size(); i++)
#define EPS 1e-9
#define INF 1e12
#define debug(x) cerr << "DEBUG : " << (#x) << " => " << (x) << endl

int N;
int pred[105];
vector<int> suiv[105];
int after[105];
bool poss[105];

int compute(int x)
{
	if(suiv[x].size() == 0)
	{
		return after[x] = 1;
	}
	else
	{
		int tot = 1;
		LOOP(i, suiv[x])
		{
			tot += compute(suiv[x][i]);
		}
		return after[x] = tot;
	}
}

string s;
string finish;

void random_walk(int step)
{
	if(step == N) return;
	int t = rand() % (N-step);
	//cerr << "random ";
	//cerr << t << endl;
	int a = 0;
	int x = -1;
	int somme = 0;
	REP(i, 1, N)
	{
		if(poss[i])
		{
			if(a + after[i] > t)
			{
				x = i;
				break;
			}
			a += after[i];
			somme += after[i];
		}
	}
	
	if(x == -1) fprintf(stderr, "ERROR %d/%d\n", somme, N-step);
	
	poss[x] = false;
	LOOP(i, suiv[x]) poss[suiv[x][i]] = true;
	finish.push_back(s[x-1]);
	random_walk(step+1);
}

int main()
{
	int TW;
	scanf("%d", &TW);
	
	REP(tw, 1, TW)
	{
		printf("Case #%d:", tw);
		fprintf(stderr, "Case #%d.\n", tw);
		
		scanf("%d", &N);
		
		REP(i, 0, N) suiv[i].clear();
		
		REP(i, 1, N)
		{
			scanf("%d", &pred[i]);
			suiv[pred[i]].push_back(i);
			//printf("%d -> %d\n", pred[i], i);
		}
		scanf("\n");
		s.clear();
		getline(cin, s); // Attention -1
		int M;
		scanf("%d\n", &M);
		string w[5];
		int val[5];
		REP(i, 0, M-1)
		{
			cin >> w[i];
			val[i] = 0;
		}
		
		compute(0);
		int K = 10000;
		
		/*
		REP(i, 1, N)
		{
			cerr << i << " " << after[i] << endl;
		}
		*/
		
		//LOOP(i, poss) cerr << poss[i] << endl;
		REP(i, 1, K)
		{
			REP(i, 1, N) poss[i] = false;
			LOOP(i, suiv[0]) poss[suiv[0][i]] = true;
			finish.clear();
			random_walk(0);
			//cerr << finish << endl;
			REP(j, 0, M-1)
			{
				std::size_t found = finish.find(w[j]);
				if(found != std::string::npos)
				{
					val[j]++;
				}
			}
		}
		
		REP(j, 0, M-1)
		{
			double score = val[j] / (double)K;
			printf(" %.6lf", score);
		}
		printf("\n");
	}

  return 0;
}
