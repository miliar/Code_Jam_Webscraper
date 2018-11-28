#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

#define MOD (1000002013)

int N, M;

struct stat {
	int num, pass;
	bool in;
};

struct ticket {
	int start, pass;
};

vector<stat> line;
vector<ticket> counter;

bool cmp(const stat &a, const stat &b)
{
	if( a.num != b.num )
		return a.num < b.num;
	return a.in;
}

long long pay(long long start, long long stop)
{
	long long diff = stop - start;
	return ((2 - diff)*(diff + 1)/2)%MOD;
}

int main()
{
	long long org, cheat;
	int cas, cas_n, start, stop, pass;
	stat tmp;
	ticket t_tmp;
	scanf("%d", &cas_n);
	for(cas=1; cas<=cas_n; cas++) {
		line.clear();
		counter.clear();
		org = 0;
		cheat = 0;
		scanf("%d %d", &N, &M);
		for(int i=0; i<M; i++) {
			scanf("%d %d %d", &start, &stop, &pass);
			org += (pay(start, stop) * pass)%MOD;
			tmp.num = start;
			tmp.pass = pass;
			tmp.in = true;
			line.push_back(tmp);
			tmp.num = stop;
			tmp.in = false;
			line.push_back(tmp);
		}
		sort(line.begin(), line.end(), cmp);
		//for(int i=0; i<line.size(); i++)
		//	printf("%d %d %d\n", line[i].num, line[i].pass, line[i].in);
		for(int i=0; i<line.size(); i++) {
			if(line[i].in) { //in
				t_tmp.pass = line[i].pass;
				t_tmp.start = line[i].num;
				counter.push_back(t_tmp);
			} else { // out
				tmp.pass = line[i].pass;
				tmp.num = line[i].num;
				while( tmp.pass ) {
					t_tmp.pass = counter.back().pass;
					t_tmp.start = counter.back().start;
					counter.pop_back();
					if( t_tmp.pass <= tmp.pass ) {
						tmp.pass -= t_tmp.pass;
						cheat += (pay(t_tmp.start, tmp.num)*t_tmp.pass)%MOD;
					} else {
						t_tmp.pass -= tmp.pass;
						cheat += (pay(t_tmp.start, tmp.num)*tmp.pass)%MOD;
						counter.push_back(t_tmp);
						break;
					}
				}
			}
		}
		printf("Case #%d: %lld\n", cas, (org - cheat)%MOD);
	}
	return 0;
}
