#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <set>
#include <map>
#include <queue> 
#include <climits>
#include <cassert>

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz size()
#define ln length()
#define forr(i,a,b)                 for(int i=a;i<b;i++)
#define rep(i,n)                    forr(i,0,n) 
#define all(v)                      v.begin(),v.end()	
#define uniq(v)                     sort(all(v));v.erase(unique(all(v)),v.end())
#define clr(a)                      memset(a,0,sizeof a)
	
#define debug                       if(1)
#define debugoff                    if(0)	

#define print(x)                 cerr << x << " ";    
#define pn()				     cerr << endl;
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

#define MAX 100010
#define MOD 1000000007
#define endl '\n'
int mat[5][5][5];
void pre(){
	for(int i=1;i<5;i++)
		for(int j=1;j<5;j++){
			mat[1][i][j] = 1;
			mat[2][i][j] = 1;
		}

	mat[2][1][1] = mat[2][3][1] = mat[2][1][3] = mat[2][3][3] = 0;
	mat[3][3][3] = mat[3][2][3] = mat[3][3][2] = mat[3][4][3] = mat[3][3][4] = 1;
	mat[4][4][4] = mat[4][4][3] = mat[4][3][4] = 1;
}
int main()
{
	memset(mat,0,sizeof mat);
	pre();
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t,x,r,c,n,cases=1;
	cin>>t;
	while(t--)
	{
		cin>>x>>r>>c;
		if(mat[x][r][c])
			cout<<"Case #"<<cases<<": GABRIEL"<<endl;
		else
			cout<<"Case #"<<cases<<": RICHARD"<<endl;
		cases++;
	}
	return 0; 
}