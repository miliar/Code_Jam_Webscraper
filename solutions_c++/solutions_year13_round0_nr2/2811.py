#include<iostream>
#include<algorithm>
#include<stdio.h>

using namespace std;

#define MAX 2

int findMin(int lawn[101][101], int N, int M)
{
	int least = 101;
	for(int i = 1; i <= N; i++)
	for(int j = 1; j <= M; j++)
	{
		least = min(least, lawn[i][j]);
	}
	return least;
}

void incCol(int lawn[101][101], int n, int N, int x)
{
	for(int i = 1; i <= N; i++)
	{
		lawn[i][n] = x;
	}
}

void incRow(int lawn[101][101], int n, int M, int x)
{
	for(int i = 1; i <= M; i++)
	{
		lawn[n][i] = x;
	}
}

void display(int lawn[101][101], int N, int M)
{
	for(int i = 1; i <= N; i++)
	{
		for(int j = 1; j <= M; j++)
		cout<<lawn[i][j]<<" ";
		cout<<endl;
	}
}

bool check(int lawn[101][101], int N, int M)
{
	int lowest = findMin(lawn, N, M);
	if(lowest == MAX)
	return true;
	
	int *cols = new int[M+1];
	int *rows = new int[N+1];
	
	for(int i = 1; i <= M; i++)
	cols[i] = 0;
	for(int i = 1; i <= N; i++)
	rows[i] = 0;
	
	for(int i = 1; i <= N; i++)
	for(int j = 1; j <= M; j++)
	if(lawn[i][j] == lowest)
	{
		cols[j]++;
		rows[i]++;
	}
	
	for(int i = 1; i <= M; i++)
	{
		if(cols[i] == N)
		incCol(lawn, i, N, lowest+1);
	}
	
	for(int i = 1; i <= N; i++)
	{
		if(rows[i] == M)
		incRow(lawn, i, M, lowest+1);
	}
	
	for(int i = 0; i <= N; i++)
	for(int j = 0; j <= M; j++)
	if(lawn[i][j] == lowest)
	return false;
	
	return check(lawn, N, M);
}

int main(void)
{
	freopen("C:/Downloads/GCJ-QR-B-Small-In.in", "r", stdin);
	freopen("C:/Downloads/GCJ-QR-B-Small-Out.txt", "w+", stdout);
	int T, N, M;
	cin>>T;
	int n = 1;
	int lawn[101][101];
	while(T--)
	{
		cin>>N>>M;
		for(int i = 1; i <= N; i++)
		for(int j = 1; j <= M; j++)
		cin>>lawn[i][j];
		cout<<"Case #"<<n++<<": ";
		if(check(lawn, N, M))
		cout<<"YES";
		else
		cout<<"NO";
		cout<<endl;
	}
}
