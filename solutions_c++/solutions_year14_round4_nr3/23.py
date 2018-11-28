#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

void read();
void kill();
void kill2();

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;

	cin>>t;

	for (int i=1; i<=t; ++i){
		read();
		cout<<"Case #"<<i<<": ";
		kill();
		//kill2();
	}

	return 0;
}

#define M 2014

struct seg
{
	int l,r;
	void read(){
		cin>>l>>r;
		if (l>r)
			swap(l,r);
	}
};

struct rect{
	seg x,y;
	void read(){
		cin>>x.l>>y.l;
		cin>>x.r>>y.r;
		++x.r;
		++y.r;	
	}
};

int dist(seg x, seg y){
	if (x.r>y.r)
		swap(x,y);
	if (x.r >= y.l)
		return 0;
	return y.l-x.r;
}

int dist(const rect &x, const rect &y){
	return max(dist(x.x,y.x),dist(x.y,y.y));
}

rect a[M];
int n,w,h,d[M][M],f[M];
bool u[M];
priority_queue<pair<int,int> > q;

void read(){
	cin>>w>>h>>n;
	for (int i=1; i<=n; ++i)
		a[i].read();
}

void relax(int v){
	u[v]=1;
	for (int i=0; i<=n+1; ++i)
	if (!u[i]){
		if (f[i]>f[v]+d[v][i]){
			f[i]=f[v]+d[v][i];
			q.push(make_pair(-f[i],i));
		}
	}
}

void kill(){
	int s = 0, fin = n+1;
	for (int i=1; i<=n; ++i)
		for (int j=1; j<=n; ++j)
			d[i][j]=dist(a[i],a[j]);

	for (int i=1; i<=n; ++i)
		d[s][i]=d[i][s]=a[i].x.l;

	for (int i=1; i<=n; ++i)
		d[fin][i]=d[i][fin]=w-a[i].x.r;

	d[s][fin]=d[fin][s]=w;
	d[s][s]=d[fin][fin]=0;

	for (int i=0; i<=fin; ++i){
		u[i]=0;
		f[i]=w+10;
	}

	f[0]=0;

	q.push(make_pair(0,s));

	while (!q.empty()){
		int x = q.top().second;
		q.pop();
		if (!u[x])
			relax(x);
	}


	cout<<f[fin]<<"\n";


}

void kill2(){
	int s = 0, f = n+1;
	for (int i=1; i<=n; ++i)
		for (int j=1; j<=n; ++j)
			d[i][j]=dist(a[i],a[j]);

	for (int i=1; i<=n; ++i)
		d[s][i]=d[i][s]=a[i].x.l;

	for (int i=1; i<=n; ++i)
		d[f][i]=d[i][f]=w-a[i].x.r;

	d[s][f]=d[f][s]=w;
	d[s][s]=d[f][f]=0;

	/*cout<<"\n";
	for (int i=0; i<=n+1; ++i,cout<<"\n")
		for (int j=0; j<=n+1; ++j,cout<<" ")
			cout<<d[i][j];
	*/

	for (int k=0; k<=n+1; ++k)
		for (int i=0; i<=n+1; ++i)
			for (int j=0; j<=n+1; ++j)
				d[i][j]=min(d[i][j],d[i][k]+d[k][j]);

	cout<<d[s][f]<<"\n";
}