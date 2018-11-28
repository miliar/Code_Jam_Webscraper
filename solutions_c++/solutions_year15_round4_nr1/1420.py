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

const int N = 110;
int n,m;
string pola[N];

PI poprzednik[N][N];
PI nastepnik[N][N];
PI pusty = MP(-1, -1);

PI przesun(PI pos, PI r)
{
	return MP(pos.first + r.first, pos.second + r.second);
}

bool w_polu(PI pos)
{
	return 0 <= pos.first && pos.first < n && 0 <= pos.second && pos.second < m;

}

int main() {
	int daa;scanf("%d",&daa);
	for(int ind=1;ind<=daa;ind++) {
		scanf("%d%d", &n, &m);

		for (int i = 0; i < n; i++)
			pola[i] = scanf_string();

		for (int i = 0; i < n; i++)
			for (int i2 = 0; i2 < m; i2++)
				poprzednik[i][i2] = nastepnik[i][i2] = pusty;

		int res = 0;
		for (int i = 0; i < n; i++)
			for (int i2 = 0; i2 < m; i2++) if (pola[i][i2] != '.')
			{

				PI ruch;
				if (pola[i][i2] == '^')
				{
					ruch = MP(-1, 0);
				}
				if (pola[i][i2] == '<')
				{
					ruch = MP(0, -1);
				}
				if (pola[i][i2] == '>')
				{
					ruch = MP(0, 1);
				}
				if (pola[i][i2] == 'v')
				{
					ruch = MP(+1, 0);
				}

				PI pos = MP(i, i2);
				PI st = pos;
				// czy jest ktos dalej
				int ok = 0;
				while (1)
				{
					pos = przesun(pos, ruch);
					if (w_polu(pos) == false)
						break;

					if (pola[pos.FT][pos.SD] != '.')
					{
						poprzednik[pos.FT][pos.SD] = st;
						nastepnik[st.FT][st.SD] = pos;
						ok = 1;
						break;
					}
				}
			}
		
		for (int i = 0; i < n; i++)
			for (int i2 = 0; i2 < m; i2++)  if (pola[i][i2] != '.')
				if (nastepnik[i][i2] == pusty && poprzednik[i][i2] != pusty)
					res++;

		for (int i = 0; i < n; i++)
			for (int i2 = 0; i2 < m; i2++)  if (pola[i][i2] != '.')
			{
				if (nastepnik[i][i2] == pusty && poprzednik[i][i2] == pusty)
				{
					// spróbuj obróciæ i zobacz czy trafisz w kogokolwiek
					int sam = 1;
					for (int k = 0; k < m; k++)
						if (pola[i][k] != '.' && k != i2) 
						{
							res++;
							sam = 0;
							break;
						}
					if (sam)
					{
						for (int k = 0; k < n; k++)
							if (pola[k][i2] != '.' && k != i)
							{
								res++;
								sam = 0;
								break;
							}

					}
					
					if (sam == 1) {
						i =i2=res = 10000;
					}
				}

			}
				

		printf("Case #%d: ",ind);
		if (res == 10000)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", res);
	}
	return 0;
}
