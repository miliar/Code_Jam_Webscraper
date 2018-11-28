#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>
#include <vector>
#include <cstdio>
#include <iostream>
#define S(x) scanf("%lld",&x)
#define P(x) printf("%lld",x)
#define LI long long int
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		string s;
		cin>>s;
		LI a[26],count=0,idx=0,n[1000],it=20;
		fill(a,a+26,0);
		for(int i=0;i<s.length();i++)
		{
			a[s.at(i)-'A']++;
		}
		//for(int i=0;i<26;i++) cout<<a[i]<<endl;
		while(count<s.length())
		{
			/*for(int i=0;i<26;i++) cout<<a[i];
			cout<<endl;
			for(int k=0;k<idx;k++) cout<<n[k];
			cout<<endl;*/
			if(a['z'-'a'] && a['e'-'a'] && a['r'-'a'] && a['o' -'a'])
			{
				count+=4;
				a['z'-'a']--;
				a['e'-'a']--;
				a['r'-'a']--;
				a['o' -'a']--;
				n[idx]=0;
				idx++;
				continue;
			}
			if(a['t'-'a'] && a['w'-'a'] && a['o'-'a'])
			{
				count+=3;
				a['t'-'a']--;
				a['w'-'a']--;
				a['o'-'a']--;
				n[idx]=2;
				idx++;
				continue;
			}
			if(a['f'-'a'] && a['o'-'a'] && a['u'-'a'] && a['r' -'a'])
			{
				count+=4;
				a['f'-'a']--;
				a['o'-'a']--;
				a['u'-'a']--;
				a['r' -'a']--;
				n[idx]=4;
				idx++;
				continue;
			}
			if(a['s'-'a'] && a['i'-'a'] && a['x'-'a'])
			{
				count+=3;
				a['s'-'a']--;
				a['i'-'a']--;
				a['x'-'a']--;
				n[idx]=6;
				idx++;
				continue;
			}
			if(a['f'-'a'] && a['i'-'a'] && a['v'-'a'] && a['e' -'a'])
			{
				count+=4;
				a['f'-'a']--;
				a['i'-'a']--;
				a['v'-'a']--;
				a['e' -'a']--;
				n[idx]=5;
				idx++;
				continue;
			}
			if(a['o'-'a'] && a['n'-'a'] && a['e'-'a'])
			{
				count+=3;
				a['o'-'a']--;
				a['n'-'a']--;
				a['e'-'a']--;
				n[idx]=1;
				idx++;
				continue;
			}
			if(a['t'-'a'] && a['h'-'a'] && a['r'-'a'] && a['e' -'a']>=2 && a['e' -'a'])
			{
				count+=5;
				a['t'-'a']--;
				a['h'-'a']--;
				a['r'-'a']--;
				a['e' -'a']--;
				a['e' -'a']--;
				n[idx]=3;
				idx++;
				continue;
			}
			if(a['s'-'a'] && a['e'-'a']>=2 && a['v'-'a'] && a['e' -'a'] && a['n' -'a'])
			{
				count+=5;
				a['s'-'a']--;
				a['e'-'a']--;
				a['v'-'a']--;
				a['e' -'a']--;
				a['n' -'a']--;
				n[idx]=7;
				idx++;
				continue;
			}
			if(a['n'-'a']>=2 && a['i'-'a'] && a['n'-'a'] && a['e' -'a'])
			{
				count+=4;
				a['n'-'a']--;
				a['i'-'a']--;
				a['n'-'a']--;
				a['e' -'a']--;
				n[idx]=9;
				idx++;
				continue;
			}
			
			
			if(a['e'-'a'] && a['i'-'a'] && a['g'-'a'] && a['h' -'a'] && a['t' -'a'])
			{
				count+=5;
				a['e'-'a']--;
				a['i'-'a']--;
				a['g'-'a']--;
				a['h' -'a']--;
				a['t' -'a']--;
				n[idx]=8;
				idx++;
				continue;
			}
		}
		sort(n,n+idx);
		cout<<"Case #"<<j<<": ";
		for(int i=0;i<idx;i++) cout<<n[i];
		cout<<endl;
	}
	return 0;
}
