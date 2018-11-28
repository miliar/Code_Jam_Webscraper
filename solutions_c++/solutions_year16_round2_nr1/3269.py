#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out90.out","w",stdout);
	int test;
	cin>>test;
	for(int h1=1;h1<=test;++h1)
	{
		int A1[10000]={-1};
		int y=0;
		string s1;
		cin>>s1;
		int k=s1.length();
		int o=std::count(s1.begin(),s1.end(),'O');
		int e=std::count(s1.begin(),s1.end(),'E');
		int h=std::count(s1.begin(),s1.end(),'H');
		int f=std::count(s1.begin(),s1.end(),'F');
		int i=std::count(s1.begin(),s1.end(),'I');
		int g=std::count(s1.begin(),s1.end(),'G');
		int n=std::count(s1.begin(),s1.end(),'N');
		int r=std::count(s1.begin(),s1.end(),'R');
		int t=std::count(s1.begin(),s1.end(),'T');
		int w=std::count(s1.begin(),s1.end(),'W');
		int u=std::count(s1.begin(),s1.end(),'U');
		int v=std::count(s1.begin(),s1.end(),'V');
		int s=std::count(s1.begin(),s1.end(),'S');
		int x=std::count(s1.begin(),s1.end(),'X');
		int z=std::count(s1.begin(),s1.end(),'Z');
		if(z!=0)
		{
			int countz=z;
			while(z)
			{
				A1[y++]=0;
				z--;
			}
			e-=countz;
			r-=countz;
			o-=countz;
			k-=4*countz;
		}
		if(x!=0)
		{
			int countx=x;
			while(x)
			{
				A1[y++]=6;
				x--;
			}
			s-=countx;
			i-=countx;
			k-=3*countx;
		}
		if(u!=0)
		{
			int countu=u;
			while(u)
			{
				A1[y++]=4;
				u--;
			}
			f-=countu;
			o-=countu;
			r-=countu;
			k-=4*countu;
		}
		if(w!=0)
		{
			int countw=w;
			while(w)
			{
				A1[y++]=2;
				w--;
			}
			t-=countw;
			o-=countw;
			k-=3*countw;
		}
		if(g!=0)
		{
			int countg=g;
			while(g)
			{
				A1[y++]=8;
				g--;
			}
			e-=countg;
			i-=countg;
			h-=countg;
			t-=countg;
			k-=5*countg;
		}
		if(f!=0)
		{
			int countf=f;
			while(f)
			{
				A1[y++]=5;
				f--;
			}
			i-=countf;
			v-=countf;
			e-=countf;
			k-=4*countf;
		}
		if(o!=0)
		{
			int counto=o;
			while(o)
			{
				A1[y++]=1;
				o--;
			}
			o-=counto;
			e-=counto;
			k-=3*counto;
		}
		if(r!=0)
		{
			int countr=r;
			while(r)
			{
				A1[y++]=3;
				r--;
			}
			t-=countr;
			h-=countr;
			e-=countr;
			e-=countr;
			k-=5*countr;
		}
		if(v!=0)
		{
			int countv=v;
			while(v)
			{
				A1[y++]=7;
				v--;
			}
			s-=countv;
			n-=countv;
			e-=countv;
			e-=countv;
			k-=5*countv;
		}
		while(k)
		{
			A1[y++]=9;
			k-=4;
		}
		sort(A1,A1+y);
		cout<<"Case #"<<h1<<": ";
		for(int ggg=0;ggg<y;++ggg)
		cout<<A1[ggg];
		cout<<endl;
	}
}

