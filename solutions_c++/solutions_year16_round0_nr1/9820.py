#include<bits/stdc++.h>
using namespace std;
     
#define ll long long
#define mset(m,v) memset(m,v,sizeof(m))
#define iter(a,it) for(auto it: a)
#define f(it,o) f(aut(it, (o).begin()); it != (o).end(); ++ it)
#define tr(cont, it) for(typeof(cont.begin()) it = cont.begin(); it != cont.end(); it++)    
#define dbg(x)  cout<< #x << ": " << (x) << endl; 
#define all(o) (o).begin(), (o).end()
#define UNIQUE(c) (c).resize(unique(all(c)) - (c).begin())  // use with vectors
#define present(cont, e) (cont.find(e) != cont.end()) // find for set/map
#define vpresent(cont, e) (find(all(cont),e) != cont.end())  //find for vectors
#define pb push_back
#define mp make_pair
#define sz(x) (x.size())
#define vii vector<pair<int,int>>
#define pii pair<int,int>

int main()
{
	
	int t,n,i,j,k;
	cin>>t;

	for(k=1;k<=t;k++)
	{
		cin>>n;
		if(n==0){
			printf("Case #%d: INSOMNIA\n",k);
			continue;
		}
		
		int a[11]={0},x,y,f;
		for(j=1;;j++)
		{
			int p=n*j;
			y=p;
			while(p!=0){
				x=p%10;
				a[x]=1;
				p/=10;
			}
			f=0;
			for(i=0;i<=9;i++){
				if(a[i]!=1)
					f=1;
			}

			if(f==0)
			{
				break;
			}
		}

		if(f==0){
			printf("Case #%d: %d\n",k,y);
		}
	}
	return 0;

}