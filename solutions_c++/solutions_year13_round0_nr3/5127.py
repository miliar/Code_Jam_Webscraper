#include<cstdio>
#include<vector>
using namespace std;

int T,t,n;
vector<long long int> pal;

bool palchk(long long int x){
	vector<int> wtf;
	for(; x; x/=10) wtf.push_back(x-(x/10)*10);
	for(int i=0; i<wtf.size()/2; i++)
		if(wtf[i]!=wtf[wtf.size()-1-i]) return false;
	return true;
}

int main(){
	freopen("C-large-1.in","r",stdin);
	freopen("output.txt","w",stdout);

	long long int i,cnt,a,b;
	
	for(i=1; i<=10000000; i++){
		if(palchk(i)&&palchk(i*i)){
			pal.push_back(i*i);
			//printf("%lld\n",i*i);
		}
	}

	for(scanf("%d",&T), t=1; T--; t++){
		scanf("%lld%lld",&a,&b);
		for(i=0,cnt=0; i<pal.size(); i++)
			if(a<=pal[i]&&pal[i]<=b) cnt++;
		printf("Case #%d: %lld\n",t,cnt);
	}

	return 0;
}