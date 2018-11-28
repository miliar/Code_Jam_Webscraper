#include<iostream>
using namespace std;
int tmp[50];
bool Check(long long x)
{
	if (x == 0) return true;
	int l=0;
	while (x>0)
	{
		tmp[l++]=x % 10;
		x/=10;
	}
	for (int i=0;i<l/2;++i)
	if (tmp[i]!=tmp[l-1-i]) return false;
	return true;
}
int result[5000000],rn=0;
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-ans.txt","w",stdout);
	for (long long i=0;i<=10000000;++i)
	if (Check(i) && Check(i*i)) result[rn++] = i;
	//cout<<rn<<endl;
	long long T,A,B; 
	cin>>T;
	for (int i=1;i<=T;++i)
	{
		cin>>A>>B;
		int cnt=0;
		for (int j=0;j<rn;++j)
		if (result[j]*result[j]>=A && result[j]*result[j]<=B) cnt++;
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}
