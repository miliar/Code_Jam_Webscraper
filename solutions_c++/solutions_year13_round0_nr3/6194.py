#include<cstdio>
#include<string>
#include<vector>
using namespace std;

bool palin(long long x)
{
	string s="";
	
	while(x)
	{
		s+=(x%10)+'0';
		x/=10;
	}
	
	for(int i=0;i<s.size()/2;i++)
		if(s[i]!=s[s.size()-i-1])
			return 0;
    
	return 1;
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
	int T,k=0;
	vector<long long> v;
	
	scanf("%d",&T);
	
	for(int i=0;i<10000000;i++)
		if(palin(i) && palin((long long)i*i))
			v.push_back((long long)i*i);
	
	while(T--)
	{
	    k++;
		int A,B,ret=0;
		scanf("%d %d",&A,&B);
		
		for(int i=0;i<v.size();i++)
            if(v[i]>=A && v[i]<=B)
                ret++;
        
        printf("Case #%d: %d\n",k,ret);
	}
}







