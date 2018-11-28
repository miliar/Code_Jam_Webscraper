#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out789956.out","w",stdout);
	int test;
	cin>>test;
	for(int cases=1;cases<=test;++cases)
	{
		int B[10000]={-1};
		int y=0;
		string st;
		cin>>st;
		int k=st.length();
		int o=std::count(st.begin(),st.end(),'O');
		int e=std::count(st.begin(),st.end(),'E');
		int h=std::count(st.begin(),st.end(),'H');
		int f=std::count(st.begin(),st.end(),'F');
		int i=std::count(st.begin(),st.end(),'I');
		int g=std::count(st.begin(),st.end(),'G');
		int n=std::count(st.begin(),st.end(),'N');
		int r=std::count(st.begin(),st.end(),'R');
		int t=std::count(st.begin(),st.end(),'T');
		int w=std::count(st.begin(),st.end(),'W');
		int u=std::count(st.begin(),st.end(),'U');
		int v=std::count(st.begin(),st.end(),'V');
		int s=std::count(st.begin(),st.end(),'S');
		int x=std::count(st.begin(),st.end(),'X');
		int z=std::count(st.begin(),st.end(),'Z');
		if(z!=0)
		{
			int countz=z;
			while(z)
			{
				B[y++]=0;
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
				B[y++]=6;
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
				B[y++]=4;
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
				B[y++]=2;
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
				B[y++]=8;
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
				B[y++]=5;
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
				B[y++]=1;
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
				B[y++]=3;
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
				B[y++]=7;
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
			B[y++]=9;
			k-=4;
		}
		sort(B,B+y);
		cout<<"Case #"<<cases<<": ";
		for(int i=0;i<y;++i)
		cout<<B[i];
		cout<<endl;
	}
}
