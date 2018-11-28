#include<iomanip>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<sstream>
#include<map>
#include<string>
#include<algorithm>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<cmath>

using namespace std;
int main()
{
	int T,t=1;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	while(t<=T)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double res,newres;
		double sum =2;
		double sum1 =0;
		while(true)
		{
			res = sum1 + X / sum;
			sum1 += C/ sum ;
			newres = (sum1 + X/(sum+=F));
			if(newres < res)
				res = newres;
			else
				break;
		}
		cout<<"Case #"<<t<<": "<<setprecision(7)<<fixed<<res<<endl;
		t++;
	}
}