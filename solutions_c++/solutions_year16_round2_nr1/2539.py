#include "bits/stdc++.h"

using namespace std;

#define mp make_pair
typedef long long int ll;
typedef vector<int> vi;
typedef vector<pair<int,int> > vii;

int A[30], n[11];
void solve()
{
    string S;
    cin >> S;
    memset(A,0,sizeof(A));
    memset(n,0,sizeof(n));
    for(int i = 0;i<S.size();++i){
    	A[S[i] - 'A']++;
    }
    n[0] = A['Z'-'A'];
        A['Z'-'A']-=n[0];	
A['E'-'A']-=n[0];	
A['R'-'A']-=n[0];	
A['O'-'A']-=n[0];

n[2] = A['W'-'A'];
A['T'-'A']-=n[2];	
A['W'-'A']-=n[2];	
A['O'-'A']-=n[2];

n[4] = A['U'-'A'];
A['F'-'A']-=n[4];	
A['O'-'A']-=n[4];	
A['U'-'A']-=n[4];	
A['R'-'A']-=n[4];	

n[6] = A['X'-'A'];
A['S'-'A']-=n[6];	
A['I'-'A']-=n[6];	
A['X'-'A']-=n[6];	

n[3] = A['R' - 'A'];
A['T'-'A']-=n[3];	
A['H'-'A']-=n[3];	
A['R'-'A']-=n[3];	
A['E'-'A']-=n[3];	
A['E'-'A']-=n[3];

n[5] = A['F' - 'A'];
A['F'-'A']-=n[5];	
A['I'-'A']-=n[5];	
A['V'-'A']-=n[5];	
A['E'-'A']-=n[5];	

n[7] = A['V' - 'A'];
A['S'-'A']-=n[7];	
A['E'-'A']-=n[7];	
A['V'-'A']-=n[7];	
A['E'-'A']-=n[7];	
A['N'-'A']-=n[7];	

n[8] = A['G'-'A'];
	A['E'-'A']-=n[8];	
A['I'-'A']-=n[8];	
A['G'-'A']-=n[8];	
A['H'-'A']-=n[8];	
A['T'-'A']-=n[8];	

n[9] = A['I'-'A'];
A['N'-'A']-=n[9];	
A['I'-'A']-=n[9];	
A['N'-'A']-=n[9];	
A['E'-'A']-=n[9];	

n[1] = A['N'-'A'];
	A['O'-'A']-=n[1];	
A['N'-'A']-=n[1];	
A['E'-'A']-=n[1];	

for(int i = 0;i<=9;++i){
	for(int j = 0;j<n[i];++j) cout << i;
}
cout << '\n';
/*
    int minzero = min(A[25],A[4]);
    minzero = min(minzero,A['R'-'A']);
    minzero = min(minzero,A['O'-'A']);
    for(int i = 0;i<minzero;++i) cout << 0;
    A['Z'-'A']-=minzero;	
A['E'-'A']-=minzero;	
A['R'-'A']-=minzero;	
A['O'-'A']-=minzero;

minzero = INT_MAX;
minzero = min(minzero,A['O'-'A']);
minzero = min(minzero,A['N'-'A']);
minzero = min(minzero,A['E'-'A']);
for(int i = 0;i<minzero;++i) cout << 1;
	A['O'-'A']-=minzero;	
A['N'-'A']-=minzero;	
A['E'-'A']-=minzero;	

minzero = INT_MAX;
minzero = min(minzero,A['T'-'A']);
minzero = min(minzero,A['W'-'A']);
minzero = min(minzero,A['O'-'A']);
for(int i = 0;i<minzero;++i) cout << 2;
A['T'-'A']-=minzero;	
A['W'-'A']-=minzero;	
A['O'-'A']-=minzero;	



minzero = INT_MAX;
minzero = min(minzero,A['T'-'A']);
minzero = min(minzero,A['H'-'A']);
minzero = min(minzero,A['R'-'A']);
minzero = min(minzero,A['E'-'A']/2);
for(int i = 0;i<minzero;++i) cout << 3;
A['T'-'A']-=minzero;	
A['H'-'A']-=minzero;	
A['R'-'A']-=minzero;	
A['E'-'A']-=minzero;	
A['E'-'A']-=minzero;	

minzero = INT_MAX;
minzero = min(minzero,A['F'-'A']);
minzero = min(minzero,A['O'-'A']);
minzero = min(minzero,A['U'-'A']);
minzero = min(minzero,A['R'-'A']);
for(int i = 0;i<minzero;++i) cout << 4;
A['F'-'A']-=minzero;	
A['O'-'A']-=minzero;	
A['U'-'A']-=minzero;	
A['R'-'A']-=minzero;	

minzero = INT_MAX;
minzero = min(minzero,A['F'-'A']);
minzero = min(minzero,A['I'-'A']);
minzero = min(minzero,A['V'-'A']);
minzero = min(minzero,A['E'-'A']);
for(int i = 0;i<minzero;++i) cout << 5;
A['F'-'A']-=minzero;	
A['I'-'A']-=minzero;	
A['V'-'A']-=minzero;	
A['E'-'A']-=minzero;	

minzero = INT_MAX;
minzero = min(minzero,A['S'-'A']);
minzero = min(minzero,A['I'-'A']);
minzero = min(minzero,A['X'-'A']);
for(int i = 0;i<minzero;++i) cout << 6;
A['S'-'A']-=minzero;	
A['I'-'A']-=minzero;	
A['X'-'A']-=minzero;	

minzero = INT_MAX;
minzero = min(minzero,A['S'-'A']);
minzero = min(minzero,A['E'-'A']/2);
minzero = min(minzero,A['V'-'A']);
minzero = min(minzero,A['N'-'A']);
for(int i = 0;i<minzero;++i) cout << 7;
A['S'-'A']-=minzero;	
A['E'-'A']-=minzero;	
A['V'-'A']-=minzero;	
A['E'-'A']-=minzero;	
A['N'-'A']-=minzero;	

minzero = INT_MAX;
minzero = min(minzero,A['E'-'A']);
minzero = min(minzero,A['I'-'A']);
minzero = min(minzero,A['G'-'A']);
minzero = min(minzero,A['H'-'A']);
minzero = min(minzero,A['T'-'A']);
for(int i = 0;i<minzero;++i) cout << 8;
	A['E'-'A']-=minzero;	
A['I'-'A']-=minzero;	
A['G'-'A']-=minzero;	
A['H'-'A']-=minzero;	
A['T'-'A']-=minzero;	


minzero = INT_MAX;
minzero = min(minzero,A['N'-'A']/2);
minzero = min(minzero,A['I'-'A']);
minzero = min(minzero,A['E'-'A']);
for(int i = 0;i<minzero;++i) cout << 9;
A['N'-'A']-=minzero;	
A['I'-'A']-=minzero;	
A['N'-'A']-=minzero;	
A['E'-'A']-=minzero;	
cout << '\n';*/

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int i = 1;i<=T;++i){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}