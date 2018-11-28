#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <fstream>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define maxn 110
#define datat int
#define ansdatat int

int n;

string s_ans[39] = {"1","4","9","121","484","10201","12321","14641","40804","44944","1002001","1234321","4008004","100020001","102030201","104060401","121242121","123454321","125686521","400080004","404090404","10000200001","10221412201","12102420121","12345654321","40000800004","1000002000001","1002003002001","1004006004001","1020304030201","1022325232201","1024348434201","1210024200121","1212225222121","1214428244121","1232346432321","1234567654321","4000008000004","4004009004004"};
long long a_ans[39];

void init_deal(){
}

bool check_p(long long a){
	vector<int> d;
	long long now = a;
	while(now>0){
		d.push_back(now%10);
		now/=10;
	}

	bool res = true;
	for (int i = 0, j = d.size()-1; i<j; i++,j-- )
	if(d[i] != d[j])
	{
		res = false;
		break;
	}
	return res;
}

long long str_to_ll(string s){
	stringstream ss(s);
	long long res;
	ss>>res;
	return res;
}

int main(){

	
	for (int i = 0; i<39; i++)
	{
		a_ans[i] = str_to_ll(s_ans[i]);
		//cout<<a_ans[i]<<endl;
	}
	
	

	int tttt;
	scanf("%d", &tttt);
	for(int ttt = 1;ttt<=tttt;ttt++){
		printf("Case #%d: ",ttt);
		long long a,b;
		cin>>a>>b;
		long long now = 1, n2 = 1;
		int ans = 0;
		for (int i = 0; i<39; i++)
		if(a<=a_ans[i] && a_ans[i]<=b)
		{
			ans++;
		}
		cout<<ans<<endl;
	}
	

	return 0;
};

