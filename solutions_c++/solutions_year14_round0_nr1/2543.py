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
	ifstream cin("A-small-attempt0.in");
	ofstream cout("out.txt");

	int T;
	cin>>T;

	for(int i(1);i<=T;i++){
		cout<<"Case #"<<i<<": ";
		int row1,row2;

		cin>>row1;
		vector<vector<int> > arrang1(4,vector<int>(4));
		for(int i(0);i<4;i++)
			for(int j(0);j<4;j++)
				cin>>arrang1[i][j];

		cin>>row2;
		vector<vector<int> > arrang2(4,vector<int>(4));
		for(int i(0);i<4;i++)
			for(int j(0);j<4;j++)
				cin>>arrang2[i][j];

		vector<int> intersection;
		for(int i(0);i<4;i++)
			for(int j(0);j<4;j++){
				if(arrang1[row1-1][i]==arrang2[row2-1][j])
					intersection.push_back(arrang1[row1-1][i]);
			}

		if(intersection.size()==1)	cout<<intersection[0];
		else if(intersection.size()>1) cout<<"Bad magician!";
		else if(intersection.empty())	cout<<"Volunteer cheated!";
		cout<<endl;
	}

	return 0;
}
