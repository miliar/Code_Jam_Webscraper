#include <bits/stdc++.h>
using namespace std;
int done[12];
void mark(long long a){
	long long b;
	if(a==0)
		done[a]=1;
	while(a>0)
	{
		b=a%10;
		done[b]=1;
		a/=10;
	}
}
int alldone(){
	int i,j;
	for(i=0;i<10;i++)
	{
		if(!done[i])
			return 0;
	}
	return 1;
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("outcj16qAlarge.txt", "w", stdout);
    #endif
    std::ios_base::sync_with_stdio(false);
    long long t,i,j,k,l;
    cin>>t;
    for(i=0;i<t;i++)
    {
    	cin>>j;
    	k=1;
    	memset(done,0,sizeof(done));
    	if(j==0)
    	{
    		cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
    		continue;
    	}
    	while(!alldone()){
    		l=j*k;
    		k++;
    		mark(l);
    	}
    	cout<<"Case #"<<i+1<<": "<<l<<endl;
    }
    return 0;
}