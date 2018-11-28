#include<iostream>
using namespace std;

int n, k;
int calgood(int cur)
{
	int rank = 0;
	int need = 1;
	int remain = (1<<n) - cur - 1;
	for(int i = 0; i < n; ++i)
	{
		rank *= 2;
		if(remain < need)
		    rank++;
		need += (need+1);
	}
	return rank;
}

int calbad(int cur)
{
	int rank = 0;
	int need = 1;
	int remain = cur ;
	for(int i = 0; i < n; ++i)
	{
		rank *= 2;
		if(remain >= need)
		    rank++;
		need += (need+1);
	}
	return rank;
}

int main()
{
	freopen("c:\\2.txt","r",stdin);
    freopen("c:\\2-out.txt","w",stdout);
	int T;
	cin>>T;
    for(int caseIndex =1; caseIndex <= T; ++caseIndex)
    {
    	cin>>n>>k;
    	int len = 1<<n;
    	int good = 0, bad = 0;
    	for(int i = 0; i < len; ++i)
    	{
    		int curgood = calgood(i);
    		int curbad = calbad(i);
    		if(curgood < k)
    		    good = i;
    		if(curbad < k)
    		    bad = i;
    	}
    	cout<<"Case #"<<caseIndex<<": ";
    	cout<<bad<<" "<<good<<endl;
    }
    return 0;
} 
