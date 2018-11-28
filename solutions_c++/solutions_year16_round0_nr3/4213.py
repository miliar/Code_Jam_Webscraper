#include <iostream>
#include <bitset>
#define int long long
using namespace std;
int dl, ile;
bool check(int i);
int getFactor(int i);
main()
{
	int ilez;
	cin>>ilez;
	for(int aa=0; aa<ilez; aa++)
	{
		cout<<"Case #"<<aa+1<<": "<<endl;
		cin>>dl>>ile;
		int znalezione=0;
		dl-=2;
		for(int k=0; k<(1<<dl); k++)
		{
			if(check(k))
				znalezione++;
			if(znalezione==ile)
				break;
		}
	}
}
bool check(int i)
{
	bitset<14> foo(i);
	//string s = bitset<2>(i).to_string<string>();
	string s = foo.to_string();
	s="1"+s+"1";
	int factors[11] = {0};
	for(int f=2; f<=10; f++)
	{
		factors[f]=getFactor(stoll(s, nullptr, f));
		if(factors[f]==0)
			return 0;
	}
	cout<<s<<" ";
	for(int f=2; f<11; f++)
	{
		cout<<factors[f]<<" ";
	}
	cout<<endl;
	return 1;
}
int getFactor(int i)
{
	for(int a=2; a*a<=i; a++)
	{
		if(i%a==0)
			return a;
	}
	return 0;
}
