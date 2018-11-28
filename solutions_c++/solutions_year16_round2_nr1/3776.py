#include<bits/stdc++.h>
#define endl '\n'
#define ll long long 
#define max 1000000
using namespace std;
ll t,n;
char a[100000];
vector<ll>v;
map<char,ll>m;
void f0()
{
	int temp[4]={m['Z'],m['E'],m['R'],m['O']};
	sort(temp,temp+4);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
		v.push_back(0);
		m['Z']=m['Z']-min;
		m['E']=m['E']-min;
		m['R']=m['R']-min;
		m['O']=m['O']-min;
	}
}
	void	f1()
	{
		int temp[3]={m['O'],m['N'],m['E']};
	sort(temp,temp+3);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
		v.push_back(1);
		m['O']=m['O']-min;
		m['N']=m['N']-min;
		m['E']=m['E']-min;
	}
		
	}
	void	f2()
	{
		int temp[3]={m['T'],m['W'],m['O']};
	sort(temp,temp+3);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
	v.push_back(2);
		m['T']=m['T']-min;
		m['W']=m['W']-min;
		m['O']=m['O']-min;
	}
		
		
	}
	void	f3()
	{
		
		int temp[5]={m['T'],m['H'],m['R'],m['E'],m['E']};
	sort(temp,temp+5);
	int min=temp[0];
	if(min>0&&m['E']>=2*min)
	{
		for(int i=0;i<min;i++)
	v.push_back(3);
		m['T']=m['T']-min;
		m['H']=m['H']-min;
		m['R']=m['R']-min;
		m['E']=m['E']-min;
		m['E']=m['E']-min;
	}
		
		
	}
	void	f4()
	{
			int temp[4]={m['F'],m['O'],m['U'],m['R']};
	sort(temp,temp+4);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
		v.push_back(4);
		m['F']=m['F']-min;
		m['O']=m['O']-min;
		m['U']=m['U']-min;
		m['R']=m['R']-min;
	}
	}
		void f5()
		{
				int temp[4]={m['F'],m['I'],m['V'],m['E']};
	sort(temp,temp+4);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
	v.push_back(5);
		m['F']=m['F']-min;
		m['I']=m['I']-min;
		m['V']=m['V']-min;
		m['E']=m['E']-min;
	}
		}
		void f6()
		{
				int temp[3]={m['S'],m['I'],m['X']};
	sort(temp,temp+3);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
		v.push_back(6);
		m['S']=m['S']-min;
		m['I']=m['I']-min;
		m['X']=m['X']-min;
	}
		}
	void	f7()
	{
		
		int temp[5]={m['S'],m['E'],m['V'],m['E'],m['N']};
	sort(temp,temp+5);
	int min=temp[0];
	if(min>0&&m['E']>=2*min)
	{
		for(int i=0;i<min;i++)
		v.push_back(7);
		m['S']=m['S']-min;
		m['E']=m['E']-min;
		m['V']=m['V']-min;
		m['N']=m['N']-min;
		m['E']=m['E']-min;
	}
		
		
	}
	void	f8()
	{
		int temp[5]={m['E'],m['I'],m['G'],m['H'],m['T']};
	sort(temp,temp+5);
	int min=temp[0];
	if(min>0)
	{
		for(int i=0;i<min;i++)
		v.push_back(8);
		m['E']=m['E']-min;
		m['I']=m['I']-min;
		m['G']=m['G']-min;
		m['H']=m['H']-min;
		m['T']=m['T']-min;
	}
		
		
	}
	void	f9()
	{
			
			int temp[4]={m['N'],m['I'],m['N'],m['E']};
	sort(temp,temp+4);
	int min=temp[0];
	if(min>0&&m['N']>=2*min)
	{
		for(int i=0;i<min;i++)
		v.push_back(9);
		m['N']=m['N']-min;
		m['I']=m['I']-min;
		m['E']=m['E']-min;
		m['N']=m['N']-min;
	}
	}
int main()
{
	ios_base::sync_with_stdio(0);
		freopen("A-small-attempt7.in","r",stdin);
	freopen("1.txt","w+",stdout);
	cin>>t;
	int test=t;
	while(t--)
	{
		cin>>a;
		for(int i=0;i<strlen(a);i++)
		m[a[i]]++;
		cout<<"Case #"<<test-t<<": ";
			if(m['Z'])
		f0();
		if(m['W'])
		f2();
		if(m['U'])
		f4();
		if(m['X'])
		f6();
		if(m['G'])
		f8();
		
		f0();
		f1();
		f2();
		f3();
		f4();
		f5();
		f6();
		f7();
		f8();
		f9();
		sort(v.begin(),v.end());
		for(int i=0;i<v.size();i++)
		cout<<v[i];
		cout<<endl;
		m.clear();
		v.clear();
	}
}
