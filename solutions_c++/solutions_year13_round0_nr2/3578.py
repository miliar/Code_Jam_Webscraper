#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

int lawn[100][100];
int highestCol[100];
int highestRow[100];
int N, M;


void eval(){
	cin>>N;
	cin>>M;

    for(int i=0; i<N; i++)
    {
		for(int j = 0; j<M; j++)
		{
			cin>>lawn[i][j];
		}
    }
	
    for(int i=0; i<N; i++)
    {
		highestCol[i] = 0;
		for(int j = 0; j<M; j++)
		{
			if(lawn[i][j] >= highestCol[i])
			{
				highestCol[i] = lawn[i][j];
			}
		}
    }	

    for(int j=0; j<M; j++)
    {
		highestRow[j] = 0;
		for(int i = 0; i<N; i++)
		{
			if(lawn[i][j] >= highestRow[j])
			{
				highestRow[j] = lawn[i][j];
			}
		}
    }	
	
    for(int i=0; i<N; i++)
    {
		for(int j = 0; j<M; j++)
		{
			if(lawn[i][j] < highestCol[i] && lawn[i][j] < highestRow[j])
			{
				cout<<"NO"<<endl;
				return;
			}
		}
    }
	cout<<"YES"<<endl;
	return;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
