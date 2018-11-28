#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
#include<algorithm>
#include<cmath>
using namespace std;


int main()
{
  ifstream in("in.txt");
  ofstream out("out.txt");
  int T;
  in >> T;
  for(int t = 1; t <= T; t++)
  {
  	int N, M;
  	in >> N >> M;
  	vector<int> cards(N+1, 0);
  	vector<int> endTimes;
  	long long max = 0;
  	for(int i = 0; i < M; i++)
  	{
  		int s, e, p;
  		in >> s >> e >> p;
  		max += p * ( (e-s)*N - (e-s)*(e-s-1)/2);
  		cards[s]+=p;
  		for(int j = 0; j < p; j++)
  			endTimes.push_back(e);
  	}
  	sort(endTimes.begin(), endTimes.end());
  	long long sum = 0;
  	for(int i = 0; i < endTimes.size(); i++)
  	{
  		int e = endTimes[i];
  		int k = 0;
  		while(cards[e-k] == 0) k++;
  		cards[e-k]--;
  		sum += k*N - k*(k-1)/2;
  	}
    out<<"Case #"<<t<<": "<<max-sum<<endl;
  } 
}
