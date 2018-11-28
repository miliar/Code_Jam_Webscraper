#include <stdio.h>
#include <string>
#include <map>
using namespace std;

map<pair<int, int>, int> u[13][3];
map<pair<int, int>, string> s[13][3];

void init()
{
	u[0][0][make_pair(1,0)] = 1;
	u[0][1][make_pair(0,1)] = 1;
	u[0][2][make_pair(0,0)] = 1;
	s[0][0][make_pair(1,0)] = "R";
	s[0][1][make_pair(0,1)] = "P";
	s[0][2][make_pair(0,0)] = "S";

	for (int n=1;n<=12;n++){
		for (int k=0;k<3;k++){
			for (auto v : u[n-1][k]){
				int l = (k + 2) % 3;
				for (auto w : u[n-1][l]){
					int a = v.first.first + w.first.first;
					int b = v.first.second + w.first.second;
					u[n][k][make_pair(a,b)] = 1;
					string &S = s[n][k][make_pair(a,b)];
					string t = s[n-1][k][v.first] + s[n-1][l][w.first];
					if (S == "") S = t;
					else if (S > t) S = t;
					t = s[n-1][l][w.first] + s[n-1][k][v.first];
					if (S == "") S = t;
					else if (S > t) S = t;
				}
			}
		}
	}
}

char S[(1<<12)+10]; int L;

void proc()
{
	int n,r,p;
	scanf ("%d %d %d %*d",&n,&r,&p);
	for (int k=0;k<3;k++){
		if(u[n][k].count(make_pair(r,p))){
			puts(s[n][k][make_pair(r,p)].c_str());
			return;
		}
	}
	puts("IMPOSSIBLE");
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	init();

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);
		proc();
	}

	return 0;
}