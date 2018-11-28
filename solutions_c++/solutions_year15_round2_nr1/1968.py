#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <deque>
using namespace std;

typedef long long LL;
typedef pair<int,int> PI;
typedef vector<int> VI;
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define FT first
#define SD second
#define Y first
#define X second

vector<string>token(string a) {
    vector<string>w;a.push_back(' ');
    while(!a.empty()){w.push_back(a.substr(0,a.find(" ")));a=a.substr(a.find(" ")+1,a.size()-1);}return w;
}

map<string,int> mapik;
vector<string> amapik;
int dodaj(string a) {if(mapik.count(a)==0) {mapik[a]=mapik.size()-1;amapik.PB(a);}return mapik[a];}

const int INF = 1000000000;
const LL INFINF = 1000000000000000000LL;

char tmp_str[1000];
string scanf_string() {
	scanf("%s",tmp_str);
	return tmp_str;
}

const int N = 10000;
int n;

inline bool get_bit(int w, int i) {
	return (w>>i)&1;
}

LL wyznacz_skret(PI pkt1, PI pkt2, PI cel)
{
	// -X na lewo, 0 prosto, +X na prawo
	PI wektorA = MP(pkt2.first - pkt1.first, pkt2.second - pkt1.second);
	PI wektorB = MP(cel.first - pkt1.first, cel.second - pkt1.second);
	return (LL)wektorB.first * wektorA.second - (LL)wektorA.first * wektorB.second;
}


LL binarka(LL a, LL b, LL target, LL map(LL)) // [a,b]
{
	// [mniejsze od target][wieksze rowne target]
	// znajdz i pierwszego elementu [wieksze...]
	while (a < b)
	{
		LL c = (a + b) / 2;
		if (map(c) >= target) {
			b = c;
		}
		else {
			a = c + 1;
		}
	}
	return a;
}

LL wyznacz_skret2(PI &pkt1, PI &pkt2, PI &cel)
{
	// -X na lewo, 0 prosto, +X na prawo
	int WA1 = pkt2.first - pkt1.first; 
	int WA2 = pkt2.second - pkt1.second;

	int WB1 = cel.first - pkt1.first;
	int WB2 = cel.second - pkt1.second;
	return (LL)WB1 * WA2 - (LL)WA1 * WB2;
}

// ==========================================================

LL k;
map<LL, int> dist;

char data[15];
LL flip(LL start)
{
	int i = 0;
	LL mn = 1;
	LL res = 0;
	LL tmp = start;
	while (tmp)
	{
		tmp /= 10;
		mn *= 10;
	}
	mn /= 10;
	while(start) 
	{
		res += (start % 10) * mn;
		mn /= 10;
		start /= 10;
	}
	return res;
}

typedef pair<LL, int> KO;
deque<KO> kolejka;

map<LL, int> kol;

int bfs(int start)
{
	kolejka.clear();
	kolejka.push_back(MP(start, 1));
		kol.clear();
	while (kolejka.size() > 0)
	{
		KO top = kolejka.front();
		kolejka.pop_front();
		if (top.first == 1) {
			return top.second;
		}
		if (kol.count(top.first-1) == 0)
		{
			kolejka.push_back(MP(top.first-1, top.second+1));
			kol[top.first - 1] = top.second + 1;
			// dorzuc

			// daj do kol


		}
		if (top.first % 10 != 0)
		{
			int flipp = flip(top.first);
			if (kol.count(flipp) == 0)
			{
				kolejka.push_back(MP(flipp, top.second + 1));
				kol[flipp] = top.second + 1;
			}
		}
	}
}

int bfsfor(int end)
{
	kolejka.clear();
	kolejka.push_back(MP(1, 1));
	kol.clear();
	int res = end;
	if (kol.count(end) != 0)
		return kol[end];

	while (kolejka.size() > 0)
	{
		KO top = kolejka.front();
		kolejka.pop_front();
		//if (top.first <= end){
		//	res = min(res, end - top.first + top.second);
	//}
		//if (top.first >= 1000000) {
			if (top.first == end) {
				return top.second;
			}
			int flipp = flip(top.first);
			if (kol.count(flipp) == 0)
			{
				kolejka.push_back(MP(flipp, top.second + 1));
				kol[flipp] = top.second + 1;
			}
			if (kol.count(top.first + 1) == 0)
			{
				kolejka.push_back(MP(top.first + 1, top.second + 1));
				kol[top.first + 1] = top.second + 1;
				// dorzuc

				// daj do kol


			}
		//}
	}
	return -111;
}

int goback(LL start)
{
	if (start == 1)
		return 1;

	if (dist.count(start) == 0)
	{
		int res = goback(start - 1);
		int fliped = flip(start);
		if (fliped != start)
			res = min(res, goback(fliped));
		dist[start] = res + 1;
	}
	return dist[start];
}

int main() {
	int d;scanf("%d",&d);
	for(int ind=1;ind<=d;ind++) {
		
		scanf("%I64d", &k);
		//int res = goback(k);
		int res = bfsfor(k);
		
		printf("Case #%d: ",ind);
		printf("%d\n", res);
	}
	return 0;
}
