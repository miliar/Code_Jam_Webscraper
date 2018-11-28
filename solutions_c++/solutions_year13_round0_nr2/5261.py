#include<iostream>
#include<cstdio>
using namespace std;

int board[101][101];
int N,M;
bool isCheck(int i, int j)
{
	int num = board[i][j];
	int cnt=0;
	int getMax = num;
	for(int k = 0 ; k < M ; k++ ){
		if( num == board[i][k])
			cnt++;
		if( getMax < board[i][k] ) getMax = board[i][k];
	}
	if( cnt == M || getMax == num) return true;
	cnt = 0;
	getMax = num;
	for(int k = 0 ; k < N; k++ ){
		if( num == board[k][j])
				cnt++;
		if( getMax < board[k][j] ) getMax = board[k][j];
	}
	if( cnt == N || getMax == num) return true;
	return false;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int nCases;

	cin>>nCases;
	int cnt =0;
	for(int i =1 ; i <= nCases ; i++)
	{
		cin>>N>>M;
		cnt = 0;
		for(int j = 0 ; j < N ; j++)
			for(int k = 0 ; k < M ; k++)
				cin>>board[j][k];

		for(int j = 0 ; j < N ; j ++){
			for(int k = 0 ; k < M ; k ++)
			{
				if(isCheck(j,k))
					cnt++;

			}
		}
		if( M*N == cnt) cout<<"Case #"<<i<<": YES"<<endl;
		else  cout<<"Case #"<<i<<": NO"<<endl;

	}



	return 0;
}
