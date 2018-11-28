#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
#include <deque>
#include <set>
#include <unordered_map>

using namespace std;

double calculate(const vector <double>& P){
	int K=P.size();
	vector <vector <double> > pt(K);
	for(int i=0;i<K;i++) pt[i]=vector <double>(i+1,0);
	pt[0][0]=1;
	for(int i=1;i<K;i++){
		pt[i][0]=P[i-1]*pt[i-1][0];
		pt[i][i]=(1-P[i-1])*pt[i-1][i-1];
		for(int j=1;j<i;j++) pt[i][j]=(1-P[i-1])*pt[i-1][j-1]+P[i-1]*pt[i-1][j];
	}
	return (1-P[K-1])*pt[K-1][K/2-1]+P[K-1]*pt[K-1][K/2];
}

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{		
		int N, K;
		cin >> N; cin >> K;
		vector <double> P(N);
		for(int i=0;i<N;i++){
			cin >> P[i];
		}
		sort(P.begin(),P.end());
		vector <double> PK(K);
		for(int i=0;i<K;i++) PK[i]=P[i];
		double tie=calculate(PK);
		for(int i=0;i<K;i++){
			PK[K-i-1]=P[N-i-1];
			double temp=calculate(PK);
			if(temp>tie) tie=temp;
		}
		cout << "Case #" << t << ": " << tie << endl;
		//printf("Case #%d: %s\n",t,R.c_str());
	}
  return 0;
}
