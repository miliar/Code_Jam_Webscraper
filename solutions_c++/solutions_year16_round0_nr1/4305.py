#include<cstdio>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

long getnum(long N)
{
	char buf[BUFSIZ];
	int i;
	set<int> unseen;
	set<int> seen;
	set<long> S;
	int done=1;

	for(i=0;i<10;i++) unseen.insert(i);
	long origN=N;
	
	while(N){
		if(S.count(N)) return -1;
		S.insert(N);
		sprintf(buf,"%ld",N);
		for(i=0;buf[i];i++){
			int x=buf[i]-'0';
			seen.insert(x);
			unseen.erase(x);
		}
		if(unseen.size()==0) return N;
		done++;
		N=done*origN;
	}

	return -1;
	
}

int main()
{
	int T,tc=1;
	scanf(" %d",&T);
	while(T--){
		long N;
		scanf(" %ld",&N);
		long x=getnum(N);
		printf("Case #%d",tc++);
		if(x==-1) printf(": INSOMNIA\n");
		else printf(": %ld\n",x);
	}
	return 0;
}
