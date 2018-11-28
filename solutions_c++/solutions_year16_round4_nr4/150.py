#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int N,P[26],O[26],U[26],C[26]; char S[26][26];

int find(int x)
{
	if (x != P[x]) P[x] = find(P[x]);
	return P[x];
}

struct o{
	o(int s, int m, int c)
	{
		size = s; mach = m; cost = c;
	}

	int size,mach,cost;

	o operator +(o t){
		return o(size+t.size,mach+t.mach,cost+t.cost+size*t.mach+mach*t.size);
	}
};

int ans = 0x7fffffff;

void go(vector<o> grp, int sum)
{
	if (ans < sum) return;
	if (grp.empty()){
		ans = sum;
		return;
	}
	int s = 0, m = 0;
	for (int i=0;i<grp.size();i++){
		s += grp[i].size; m += grp[i].mach;
	}
	for (int i=0;i<grp.size();i++){
		if (grp[i].size > grp[i].mach && s - grp[i].size >= m - grp[i].mach){
			auto n = grp;
			n.erase(n.begin()+i);
			go(n,sum+(grp[i].size-grp[i].mach)*grp[i].size+grp[i].cost);
		}
	}

	for (int i=0;i<grp.size();i++) for (int j=i+1;j<grp.size();j++){
		auto n = grp;
		n.erase(n.begin()+j);
		n.erase(n.begin()+i);
		auto w = grp[i] + grp[j];
		if (w.size == w.mach) go(n,sum+w.cost);
		else{
			n.push_back(w);
			go(n,sum);
		}
	}
}

void proc()
{
	scanf ("%d",&N);
	for (int i=0;i<N;i++) scanf ("%s",S[i]);
	for (int i=0;i<N;i++){
		P[i] = i;
		U[i] = 0;
		C[i] = 1;
		for (int j=0;j<N;j++) if (S[i][j] == '1') U[i] |= (1 << j);
		O[i] = U[i];
	}

	for (int i=0;i<N;i++) for (int j=i+1;j<N;j++) if (find(i) != find(j) && U[find(i)] & U[find(j)]){
		U[find(i)] |= U[find(j)];
		C[find(i)] += C[find(j)];
		P[find(j)] = find(i);
	}

	vector<o> grp;
	int sum = 0;
	for (int i=0;i<N;i++) if (P[i] == i){
		int x = U[i], c = 0;
		while (x){
			c++;
			x -= x & (-x);
		}
		int s = C[i] * c;
		for (int j=0;j<N;j++) if (find(j) == i){
			int y = O[j];
			while (y){
				s--;
				y -= y & (-y);
			}
		}
		if (C[i] != c) grp.push_back(o(C[i],c,s));
		else sum += s;
	}

	ans = 0x7fffffff;
	go(grp,sum);
	printf ("%d\n",ans);
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		fprintf (stderr,"%d\n",Case);
		printf ("Case #%d: ",Case);
		proc();
	}

	return 0;
}