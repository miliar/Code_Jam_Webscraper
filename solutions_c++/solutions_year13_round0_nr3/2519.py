#include <iostream>
#include <vector>
using namespace std;
bool isP(long long x)
{
	long long x_=x;
	long long y=0;
	while(x_)
	{
		y *= 10;
		y += x_%10;
		x_ /=10;
	}
	if(x==y)return true;
	else return false;
}
vector<long long>D;
int F(long long x)
{
	int ans = 0;
	for(vector<long long>::const_iterator itr=D.begin();itr!=D.end();++itr,++ans)
		if(*itr > x)
			break;
	return ans;
}
int main()
{
	for(long long i=1;i<10000001;++i)
	{
		long long y=i*i;
		if(isP(i)&&isP(y))
			D.push_back(y);
	}
	int T;int idx=0;
	cin >> T;
	while(T--)
	{
		++idx;
		long long A,B;
		cin >> A >> B;
		cout << "Case #" <<idx<<": "<<(F(B)-F(A-1))<<endl;
	}
	return 0;
}
