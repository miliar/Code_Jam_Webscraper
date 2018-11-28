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
	ifstream cin("B-large.in");
	ofstream cout("out.txt");
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(7);
	int T;
	cin>>T;
	for(int t(1);t<=T;t++){
		cout<<"Case #"<<t<<": ";
		double C,F,X;
		cin>>C>>F>>X;
		double nd=(F*X-2*C)/(F*C)-1;
		int n=max(0,int(ceil(nd)));
		double ans=0;
		ans+=X/(2.0+n*F);
		for(int i(0);i<n;i++)
			ans+=C/(2.0+i*F);

		cout<<ans<<endl;
	}
	return 0;
}
