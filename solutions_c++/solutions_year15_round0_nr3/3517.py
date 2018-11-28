#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
vector<int> prefix;
vector<int> suffix;
vector<int> tmp;

const int memcross[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int cross(int a,int b) {
	int neg=0;
	neg+=(a<0?1:0);
	neg+=(b<0?1:0);
	neg=neg&1;
	a=abs(a);b=abs(b);
	if (neg==0) return memcross[a][b];
	else return -memcross[a][b];
}

int main() {
	int T;
	scanf("%d",&T);
	bool ind;
	for (int z=1;z<=T;++z) {
		ind=false;
		ll L,X;
		scanf("%lld %lld",&L,&X);
		tmp.clear();
		for (int i=0;i<L;++i) {
			char c;
			scanf("\n%c",&c);
			if (c=='i') tmp.push_back(2);
			else if (c=='j') tmp.push_back(3);
			else tmp.push_back(4);
		}
		int n=tmp.size();
		prefix.clear();
		suffix.clear();
		prefix.resize(n+3,0);
		suffix.resize(n+3,0);
		int now=1;
		prefix[0]=1;
		for (int i=0;i<n;++i) {
			int val=tmp[i];
			prefix[i+1]=cross(now,val);
			now=cross(now,val);
		}
		prefix[n+1]=now;
		now=1;
		suffix[tmp.size()+1]=1;
		for (int i=tmp.size()-1;i>=0;--i) {
			int val=tmp[i];
			suffix[i+1]=cross(val,now);
			now=cross(val,now);
		}
		suffix[0]=now;
		for (int i=1;i<=n;++i) {
			if (ind) break;
			int now=1;
			for (int j=i;j<=i+n;++j) {
				int jc=(j>n?j-n:j);
				int val=tmp[jc-1];
				now=cross(now,val);
				if (j<=n && now!=3) continue;
				ll tX=X-1;
				if (j>n) {
					--tX;
					if (tX<0) continue;
					int front=suffix[i];
					int last=prefix[jc];
					int cnt=0;
					int vmid=1;
					int now=cross(front,last);
					while (cnt<4 && now!=3) {
						++cnt;
						vmid=cross(vmid,prefix[n+1]);
						now=cross(front,vmid);
						now=cross(now,last);
						--tX;
					}
					if (tX<0 || now!=3) continue;
				}
				int vf,vt;
				vf=prefix[i-1];
				vt=suffix[jc+1];
				if (i==1) {--tX;vf=cross(prefix[n+1],vf);}
				if (jc==n) {--tX;vt=cross(vt,prefix[n+1]);}
				if (tX<0) continue;
				int cnt=0;
				while (cnt<4 && vf!=2) {
					++cnt;
					vf=cross(prefix[n+1],vf);
					--tX;
				}
				if (vf!=2 || tX<0) continue;
				cnt=0;
				while (cnt<4 && vt!=4) {
					++cnt;
					vt=cross(vt,prefix[n+1]);
					--tX;
				}
				if (vt!=4 || tX<0) continue;
				if (tX%4==0) {ind=true;break;}
			}
		}
		if (ind) printf("Case #%d: YES\n",z);
		else printf("Case #%d: NO\n",z);
	}
}
