#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iostream>
typedef unsigned int uint;
typedef unsigned long long int ull;
typedef std::vector<int> vi;
typedef std::vector<uint> vu;
template <typename T> void sort(std::vector<T> &x) { std::sort(x.begin(),x.end()); }

struct pair
{
	pair() {}
	pair(int _a,int _b): a(_a),b(_b) {}
	bool operator< (pair const &rhs) const
	{
		if(a!=rhs.a)
			return a<rhs.a;
		return b<rhs.b;
	}
	int a,b;
};

struct pos
{
	pos(): x(), y() {}
	pos(int _x, int _y): x(_x), y(_y) {}
	pos &operator+= (pos const &rhs) { x+=rhs.x; y+=rhs.y; return *this; }
	pos &operator-= (pos const &rhs) { x-=rhs.x; y-=rhs.y; return *this; }
	pos operator+ (pos const &rhs) const { return pos(x+rhs.x,y+rhs.y); }
	pos operator- (pos const &rhs) const { return pos(x-rhs.x,y-rhs.y); }
	pos operator* (int rhs) const { return pos(x*rhs,y*rhs); }
	friend pos operator* (int lhs, pos const &rhs) { return pos(lhs*rhs.x,lhs*rhs.y); }
	bool operator== (pos const &rhs) const { return x==rhs.x && y==rhs.y; }
	bool operator!= (pos const &rhs) const { return x!=rhs.x || y!=rhs.y; }
	friend std::ostream& operator<< (std::ostream &o, pos const &p) { o << "(" << p.x << "," << p.y << ")"; return o; }
	void rot_ccw() { int m=y; y=x; x=-m; }
	void rot_cw() { int m=y; y=-x; x=m; }
	static pos rot_ccw(pos const &p) { return pos(-p.y,p.x); }
	static pos rot_cw(pos const &p) { return pos(p.y,-p.x); }
	static int dot(pos const &a, pos const &b) { return a.x*b.x+a.y*b.y; }
	static int cross(pos const &a, pos const &b) { return a.x*b.y-a.y*b.x; }
	static int dist2(pos const &a, pos const &b) { pos d=a-b; return dot(d,d); }

	int x, y;
};

main()
{
	uint T=0;
	scanf("%u\n",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0;
		scanf("%u",&N);
		char s[128][128];
		char sc[128][128];
		uint sr[128][128];
		uint ss[128];
		for(uint n=0; n<N; ++n)
		{
			scanf("%s",s[n]);
			uint k=0;
			for(uint i=0; s[n][i];)
			{
				char c=s[n][i];
				sc[n][k]=c;
				uint b=i;
				while(s[n][i]==c)
					++i;
				sr[n][k]=i-b;
				++k;
			}
			ss[n]=k;
			/*printf("%s %u ",s[n],k);
			for(uint i=0; i<ss[n]; ++i)
				printf("%u*%c,",sr[n][i],sc[n][i]);
			printf("\n");*/
		}
		bool ok=1;
		uint ss0=ss[0];
		for(uint n=1; ok && n<N; ++n)
		{
			ok=ss[n]==ss0;
			for(uint i=0; ok && i<ss0; ++i)
				ok=sc[n][i]==sc[0][i];
		}
		if(ok)
		{
			uint r=0;
			for(uint k=0; k<ss0; ++k)
			{
				uint ms=0;
				bool go=1;
				for(uint l=1; go; ++l)
				{
					uint s=0;
					go=0;
					for(uint n=0; n<N; ++n)
					{
						if(sr[n][k]<l)
							s+=l-sr[n][k];
						else
						{
							go=1;
							s+=sr[n][k]-l;
						}
					}
					if(l==1 || s<ms)
						ms=s;
				}
				r+=ms;
			}
			printf("Case #%u: %u\n",t,r);
		}
		else printf("Case #%u: Fegla Won\n",t);
	}
}
