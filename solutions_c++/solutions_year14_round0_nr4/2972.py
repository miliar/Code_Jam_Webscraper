#include <cstdio>
#include <vector>
#include <algorithm>

struct Elem
{
	double number;
	bool used;
	Elem(): used(false){}
	bool operator<(const Elem &e)const
	{
		return number < e.number;
	}
};
void printVector(std::vector<Elem> n, std::vector<Elem> k, int N)
{
	int i = 0 ;
	printf("\n");
	for (; i < n.size(); i++){
		printf (" %lf", n[i].number);
	}
	printf("\n");
	for (i = 0; i < k.size(); i++){
		printf (" %lf", k[i].number);
	}
}
void playWar(std::vector<Elem> n, std::vector<Elem> k, int N, int &wins)
{
	wins = 0;
	int losses = 0;
	int npos, kpos = 0;
	for (npos = 0; npos < N; npos++){
		while (kpos < N){
			if (n[npos] < k[kpos]){
				losses++;
				kpos++;
				break;
			}
			kpos++;
		}
	}
	wins = N - losses;
}


void playDeceitfulWar(std::vector<Elem> n, std::vector<Elem> k, int N, int &wins)
{
	wins = 0;
	int losses = 0;
	int i, npos, kpos = N-1;
	for (i = 0; i < N; i++){
		if (n[0] < k[0]){
			n.erase(n.begin());
			k.erase(k.end()-1);
			losses++;
		}
		else {
			n.erase(n.begin());
			k.erase(k.begin());
		}
	}
	wins = N - losses;
}
void solve(int caseNo)
{
	int N;
	scanf("%d", &N);
	std::vector<Elem> naomi, ken;
	int i;
	Elem e;
	for (i = 0; i < N; i++){
		scanf("%lf", &e.number);
		naomi.push_back(e);
	}
	for (i = 0; i < N; i++){
		scanf("%lf", &e.number);
		ken.push_back(e);
	}

	std::sort(naomi.begin(), naomi.end());
	std::sort(ken.begin(), ken.end());
	
	int warWins, deceitfulWarWins;
	//printVector(naomi, ken, N);
	playDeceitfulWar(naomi, ken, N, deceitfulWarWins);
	playWar(naomi, ken, N, warWins);

	if (caseNo > 1)
		printf("\n");
	printf("Case #%d: %d %d", caseNo, deceitfulWarWins, warWins);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
