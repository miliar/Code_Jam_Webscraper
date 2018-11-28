#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define rep(n) REP(i,n)

const int SIZE=4;
const int OX=2;
const int O=0,X=1;
string S[SIZE];

int solve()
{
	int l[OX]={0},r[OX]={0};
	REP(i,SIZE)
	{ 
		if(S[i][i]=='T'){ ++l[O]; ++l[X]; } 
		else if(S[i][i]=='X'){ ++l[X]; } 
		else if(S[i][i]=='O'){ ++l[O]; }

		if(S[i][3-i]=='T'){ ++r[O]; ++r[X]; } 
		else if(S[i][3-i]=='X'){ ++r[X]; } 
		else if(S[i][3-i]=='O'){ ++r[O]; }

		int p[OX]={0},q[OX]={0};
		REP(j,SIZE)
		{
			if(S[i][j]=='T'){ ++p[O]; ++p[X]; } 
			else if(S[i][j]=='X'){ ++p[X]; } 
			else if(S[i][j]=='O'){ ++p[O]; }

			if(S[j][i]=='T'){ ++q[O]; ++q[X]; } 
			else if(S[j][i]=='X'){ ++q[X]; } 
			else if(S[j][i]=='O'){ ++q[O]; }
		}
		if(p[O]==SIZE||q[O]==SIZE) return -1;
		if(p[X]==SIZE||q[X]==SIZE) return 1;
	}
	if(l[O]==SIZE||r[O]==SIZE) return -1;
	if(l[X]==SIZE||r[X]==SIZE) return 1;
	return 0;
}

bool is_filled()
{
	REP(i,SIZE) REP(j,SIZE) if(S[i][j]=='.') return false;
	return true;
}

int main()
{
	int n;
    cin>>n;

	REP(i,n)
	{
		REP(j,SIZE) cin>>S[j];
		int ans = solve();

		cout<<"Case #"<<(i+1)<<": ";
		if(ans== 1) cout<<"X won";
		if(ans==-1) cout<<"O won";
		if(ans==0){ if(is_filled()){ cout<<"Draw"; } else { cout<<"Game has not completed"; } }
		cout<<endl;
	}

	return 0;
}
