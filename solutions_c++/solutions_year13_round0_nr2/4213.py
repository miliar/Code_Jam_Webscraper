/*
ID: rohamhe1
PROB: proximity
LANG: C++
*/
#include<iostream>
#include<cstring>
#include<iomanip>	
#include<vector>
#include<map>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<set>
#include<complex>
#include<queue>
#include<utility>

using namespace std;

//typedef complex<long double> point;
#define pb push_back
#define mk make_pair
#define x first
#define y second
#define error(x) cout << #x << " : " << (x) << endl;
typedef long long LL;
typedef long double LD;
//#define cin fin
//#define cout fout

LL n , m , k;
const int maxn = 110;
char array[maxn][maxn];
bool mark[maxn];
queue<int>nums;

int main()
{
	int T = 1;
	int t;
	cin >> t;
	while(t--)
	{
		fill(mark , mark+maxn , 0);
		bool ans = true;
		cin >> n >> m;
		for(int i=0 ; i<n ; i++)
			for(int j=0 ; j<m ; j++)
			{
				int a;
				cin >> a;
				array[i][j] = a;
				mark[a] = true;
			}
		for(int i=1 ; i<= 100 ; i++)
			if(mark[i] == true)
					nums.push(i);
		for(int a=1 ; a<=100 ; a++)
		{
			if(mark[a] == false)
				continue;
		//	error(a);
			nums.pop();
			bool M[maxn][maxn];
			memset(M , 0 , sizeof M);
			for(int i=0 ; i<n ; i++)
			{
				int p =0;
				for(int j=0 ; j<m ; j++)
					if(array[i][j] == a)
						p++;
				if(p == m)
					for(int j=0 ; j<m ; j++)
						M[i][j] = true;
			}
			for(int i=0 ; i<m ; i++)
			{
				int p =0;
				for(int j=0 ; j<n ; j++)
					if(array[j][i] == a)
						p++;
				if(p == n)
					for(int j=0 ; j<n ; j++)
						M[j][i] = true;
			}
			for(int i=0 ; i<n ; i++)
				for(int j=0 ; j<m ; j++)
					if(array[i][j] == a && M[i][j] == false)
						ans = false;
			if(!nums.empty())
			{
				for(int i=0 ; i<n ; i++)
					for(int j=0 ; j<m ; j++)
						if(array[i][j] == a)
							array[i][j] = nums.front();
			}
		}
		if(ans == true)
			cout << "Case #" << T << ": YES" << endl;
		else
			cout << "Case #" << T << ": NO" << endl;
		T++;
	}
}
