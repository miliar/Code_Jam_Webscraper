#include<vector>
#include<string>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<stack>
#include<set>

using namespace std;

int dp[2][3][4][5][6][7][8][9][10];

int solve(vector<int> v)
{
	for(int i=1;i<10; ++i)
		v[i] = min(i,v[i]);
    
	int& res = dp[v[1]][v[2]][v[3]][v[4]][v[5]][v[6]][v[7]][v[8]][v[9]];
	if(res == -1)
	{
		int ind = 0;
		for(int i=9;i>0;--i)
		{
			if(v[i])
			{
				ind = i;
				break;
			}
		}
		if(ind < 4)
			res = ind;
		else
		{
			int r = ind;
			v[ind] -= 1;
			for(int i=1;i<ind; ++i)
			{
				v[i] += 1;
				v[ind-i] += 1;
				int tres = 1 + solve(v);
				if(tres < r)
					r = tres;
				v[i] -= 1;
				v[ind-i] -= 1;
			}
			res = r;
		}
	}
	return res;
}

int main()
{
	ifstream in("./input.txt");
	ofstream out("./output.txt");
	cin.rdbuf(in.rdbuf());
	cout.rdbuf(out.rdbuf());
	for(int i=0;i<=1; ++i)
		for(int j=0;j<=2; ++j)
			for(int k=0;k<=3; ++k)
				for(int l=0;l<=4; ++l)
					for(int m=0;m<=5; ++m)
						for(int n=0;n<=6;++n)
							for(int o=0;o<=7;++o)
								for(int p=0;p<=8;++p)
									for(int q=0;q<=9;++q)
										dp[i][j][k][l][m][n][o][p][q]=-1;
	
	int N;
	cin >> N;
	for (int t = 1; t <= N; ++t)
	{
		
		int d;
		cin>>d;
		std::vector<int> pancakes;
		pancakes.resize(10);
		for(int i=0;i<d;++i)
		{
			int temp;
			cin>>temp;
			pancakes[temp]++;
		}
		int res = solve(pancakes);
        
		cout<<"Case #"<<t<<": "<<res<<endl;
	}
}