#include<iostream>
#include<cstring>
#include<cstdio>
#include<queue>
#include<algorithm>
#define X first 
#define Y second
#define modulo 1000002013LL

using namespace std;

int N,banyak;
pair<pair<int,int>,int> rentang[2005];

long long cost(long long orang,long long jarak) {
	long long s1 = (jarak*(long long)N) % modulo;
	long long s2 = (jarak*(jarak-1LL) / 2LL) % modulo;
	return (orang * (s1-s2)) % modulo;
}

int main() {
	int kasus;
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;++l) {
		scanf("%d %d",&N,&banyak);
		long long jawab = 0;
		for (int i=1,a,b,c;i<=banyak;++i) {
			scanf("%d %d %d",&a,&b,&c);
			rentang[i*2-1].X.X = a;
			rentang[i*2-1].X.Y = 0;
			rentang[i*2-1].Y = c;
			rentang[i*2].X.X = b;
			rentang[i*2].X.Y = 1;
			rentang[i*2].Y = c;
			jawab = (jawab + cost(c,b-a)) % modulo;
		}
		sort(rentang+1,rentang+2*banyak+1);
		
		priority_queue<pair<int,int> > pq;
		for (int i=1;i<=2*banyak;++i) {
			if (rentang[i].X.Y == 0) {
				pq.push(make_pair(rentang[i].X.X,rentang[i].Y));
			} else {
				//cout<<i<<endl;
				long long sem = rentang[i].Y;
				while (sem > 0) {
					pair<int,int> atas = pq.top();
					pq.pop();
					if (atas.Y > sem) {
						atas.Y -= sem;
						pq.push(atas);
						jawab = (jawab + modulo - cost(sem,rentang[i].X.X-atas.X)) % modulo;
						sem = 0;						
					} else {
						sem -= atas.Y;
						jawab = (jawab + modulo - cost(atas.Y,rentang[i].X.X-atas.X)) % modulo;
					}
					//cout<<rentang[i].X.X-atas.X<<" "<<atas.Y<<endl;
				}
			}
		}
		cout<<"Case #"<<l<<": "<<jawab<<endl;
	}
	return 0;
}
