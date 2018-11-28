#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int M,N,X,C,cnt[1024],u[1024];
string V[10]; char S[12];

void go(int r, int b, int s)
{
	if (r == 1){
		s += cnt[b];
		if (X < s){
			X = s; C = 1;
		}
		else if (X == s) C = (C + 1) % 1000000007;
	}
	else{
		go(r-1,b,s);
		for (int j=b;j;j=(j-1)&b){
			go(r-1,b^j,s+cnt[j]);
		}
	}
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test);
	for (int Case=1;Case<=Test;Case++){
		fprintf (stderr,"Case %d st\n",Case);
		scanf ("%d %d",&M,&N);
		for (int i=0;i<M;i++){
			scanf ("%s",S);
			V[i] = S;
		}
		sort(V,V+M);
		X = 0, C = 0;

		for (int i=0;i<M;i++) u[1<<i] = i;
		for (int i=1;i<(1<<M);i++){
			int x = i & (-i);
			if (i == x){
				cnt[i] = V[u[i]].length() + 1;
			}
			else{
				cnt[i] = cnt[i-x];
				string a = V[u[x]];
				int y = i - x; y &= -y;
				string b = V[u[y]];

				int c = a.length();
				for (int i=0;i<a.length()&&i<b.length();i++){
					if (a[i] != b[i]) break;
					c--;
				}
				cnt[i] += c;
			}
		}
		go(N,(1<<M)-1,0);

		printf ("Case #%d: %d %d\n",Case,X,C);

		fprintf (stderr,"Case %d ed\n",Case);
	}

	return 0;
}