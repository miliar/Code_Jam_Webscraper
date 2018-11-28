#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define inf 1000000000
#define maxn 1000000

#define ll long long
#define pii pair<int, int>
#define pb push_back
#define sin scanint
#define bitcount(x) __builtin_popcount(x)
#define fill(s, p) memset(s, p, sizeof(s));

#ifdef ONLINE_JUDGE
#define gc getchar_unlocked
#endif

#ifndef ONLINE_JUDGE
#define gc getchar
//freopen("input.txt", "r", stdin)
//freopen("output.txt", "w", stdout)
#endif

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

char mat[4][4] = {{'1', 'i', 'j', 'k'}, {'i', '1', 'k', 'j'}, {'j', 'k', '1', 'i'}, {'k', 'j', 'i', '1'}};
bool sign[4][4];

char str[maxn], s2[maxn];
bool revsign[maxn];
char revpro[maxn];
map<char, int> m1; 

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("o2.txt", "w", stdout);
	int t, l, i, j, k, x, c1, c2, neg1, neg2, n, case_num=1;
	m1['1'] = 0;
	m1['i'] = 1;
	m1['j'] = 2;
	m1['k'] = 3;
	fill(sign, false);
	sign[1][1] = true;
	sign[1][3] = true;
	sign[2][1] = true;
	sign[2][2] = true;
	sign[3][2] = true;
	sign[3][3] = true;
	sin(t);
	while(t--){
		sin(l);
		sin(x);
		scanf("%s", str);
		s2[0] = '\0';
		strcat(s2, str);
		i=1;
		while(i<x){
			strcat(str, s2);
			i++;
		}
		//cout << str << endl;
		n = strlen(str);
		char lc;
		bool ng;
		revpro[n-1] = str[n-1];
		revsign[n-1] = false;
		/*for(i=n-2; i>=0; i--){
			lc = revpro[i+1];
			ng = revsign[i+1];
			for(j=i+1; j<n; j++){
				c1 = m1[lc];
				c2 = m1[str[j]];
				lc = mat[c1][c2];
				if(sign[c1][c2]){
					if(ng)
						ng = false;
					else
						ng = true;
				}
			}
			revpro[i] = lc;
			revsign[i] = ng;
		}*/
		for(i=n-2; i>=0; i--){
			c1 = m1[revpro[i+1]];
			c2 = m1[str[i]];
			revpro[i] = mat[c2][c1];
			//cout << i << " " << revpro[i] << " " <<  c1 << " " << c2 << endl;
			if(sign[c2][c1]){
				if(revsign[i+1])
					revsign[i] = false;
				else
					revsign[i] = true;
			}
			else
				revsign[i] = revsign[i+1];
		}
		//for(i=0; i<n; i++)
		//	cout << revpro[i] << " " << revsign[i] << endl;
		//cout << "1\n";
		//cout << str << endl;
		char lastchar1, lastchar2, lastchar3;
		bool p1, p2, pos;
		neg1 = 0;
		pos = false;
		for(i=0; i<n-2; i++){
			if(i==0)
				lastchar1 = str[0];
			else{
				c1 = m1[lastchar1];
				c2 = m1[str[i]];
				if(sign[c1][c2])
					neg1 = (neg1+1)%2;
				lastchar1 = mat[c1][c2];
			}
			if(lastchar1!='i' || (neg1%2)!=0)
				continue;
			neg2 = 0;
			for(j=i+1; j<n-1; j++){
				if(j==i+1)
					lastchar2 = str[j];
				else{
					c1 = m1[lastchar2];
					c2 = m1[str[j]];
					if(sign[c1][c2])
						neg2 = (neg2+1)%2;
					lastchar2 = mat[c1][c2];
				}
				if(lastchar2!='j' || (neg2%2)!=0)
					continue;
				if(revpro[j+1]=='k' && revsign[j+1]==false){
					pos = true;
					break;
				}
			}
			if(pos)
				break;
		}
		if(pos)
			printf("Case #%d: YES\n", case_num++);
		else
			printf("Case #%d: NO\n", case_num++);
	}
	return 0;
}