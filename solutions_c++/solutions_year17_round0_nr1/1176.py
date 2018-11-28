#include<cstdio>
#include<algorithm>
#include<iostream>
#include<bitset>
using namespace std;
bitset<1000>a,b;
int main()
{
	int T,cases=0;
	cin>>T;
	while(T--){
		int k,cnt=0;
		a.reset();
		string s;
		cin>>s>>k;
		for(int i=0;i<s.size();i++)
			a[i]=s[i]=='+';
		b.reset();
		for(int i=0;i<k;i++)
			b.set(i);
		for(int i=0;i+k<=s.size();i++)
			if(!a[i])
				a^=b<<i,cnt++;
		printf("Case #%d: ",++cases);
		if(a.count()==s.size())
			cout<<cnt<<endl;
		else
			puts("IMPOSSIBLE");
	}
}
