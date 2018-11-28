#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int main()
{
	ifstream cin("D-large.in");
	ofstream cout("out.txt");
	int T;
	cin>>T;
	for(int t(1);t<=T;t++){
		cout<<"Case #"<<t<<": ";
		int N;
		cin>>N;
		vector<double> naomi(N),ken(N);
		for(int i(0);i<N;i++)	cin>>naomi[i];
		for(int i(0);i<N;i++)	cin>>ken[i];
		sort(naomi.rbegin(),naomi.rend());
		sort(ken.rbegin(),ken.rend());
//		for(int i(0);i<N;i++)	cout<<naomi[i]<<" ";
//		cout<<endl;
//		for(int i(0);i<N;i++)	cout<<ken[i]<<" ";
		int optWar,optDecWar;

		int kenidx(0);
		for(int i(0);i<naomi.size();i++)
			if(naomi[i]<ken[kenidx])	kenidx++;

		optWar=N-kenidx;

		sort(naomi.begin(),naomi.end());
		sort(ken.begin(),ken.end());

		kenidx=0;
		for(int i(0);i<naomi.size();i++)
			if(naomi[i]>ken[kenidx])	kenidx++;

		optDecWar=kenidx;

		cout<<optDecWar<<" "<<optWar<<endl;
	}

	return 0;
}
