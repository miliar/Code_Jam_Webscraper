#include<iostream>
using namespace std;
string test(int n)
{
	if(n==0)return string("INSOMNIA");
	bool used[10];
	for(int i=0;i<10;i++)used[i]=false;
	int cnt=0;
	int i;
	for(i=1;i<=1000;i++)
	{
		int a=n*i;
		while(a>0)
		{
			if(!used[a%10])cnt++;
			used[a%10]=true;
			a/=10;
		}
		if(cnt==10)break;
	}
	return to_string(i*n);

}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;

	for(int i=1;i<=t;i++)
	{
		int in;
		cin >> in;
		string ans=test(in);
		cout << "Case #"<<i<<": "<<ans<<"\n";
	}
}
