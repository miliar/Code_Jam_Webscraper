#include<iostream>
#include<string>
#include<set>
#include<algorithm>
#include<list>
#include<vector>
#include<ctime>
#include<stack>
#include<cstring>
#include<cassert>
#include<queue>
#include<cmath>
#include<cstdio>
#include<climits>
#include<stack>

using namespace std;
typedef long long Long;
typedef pair<Long,Long> PII;
typedef pair<PII,Long> PPI;
int idx[100];
int cmp(PII a,PII b)
{
	return a.first!=b.first ? a.first < b.first : idx[a.second] < idx[b.second];
}

int main()
{
	freopen("/Users/carlosjosetoribio/Desktop/GCJ_R2/B-small-attempt1.in","r",stdin);
	freopen("/Users/carlosjosetoribio/Desktop/GCJ_R2/B-small-attempt1.out","w",stdout);

	int N,P;
//	cin >> N >> P;
//	P--;
/*
	int s = 3;
	PII arr[1<<s];
	int mi[40]; for(int i = 0; i < 20; ++i)mi[i] = 10000;
	int ma[40]; for(int i = 0; i < 20; ++i)ma[i] = 0;

	for(int i = 0; i < (1<<s); ++i)
	{
		arr[i] = PII(0,i);
		idx[i] = i;
	}
	int sz = 10000;
	do
	{
		if(sz--==0)break;
		for(int i = 0; i < (1<<s); ++i)
			arr[i].first = 0;
		sort(arr,arr+(1<<s),cmp);
//		for(int i = 0; i < (1<<s); ++i)
//			cout << arr[i].second << " ";
//		cout << endl;
		for(int i = 0; i < s; ++i)
		{
			sort(arr,arr+(1<<s),cmp);
			for(int j = 0; j < (1<<s); j += 2)
			{
				if(arr[j].second < arr[j+1].second)
					arr[j+1].first |= (1<<(s-1-i));
				else
					arr[j].first |= (1<<(s-1-i));
			}
		}
		sort(arr,arr+(1<<s),cmp);

		for(int i = 0; i < (1<<s); ++i)
		{
//			cout <<arr[i].second<< " ";
			mi[arr[i].second] = min(mi[arr[i].second] , i);
			ma[arr[i].second] = max(ma[arr[i].second] , i);
		}
//		cout << endl;
		random_shuffle(idx,idx+(1<<s));
	}
	while(sz>0);
	for(int i = 0; i < (1<<s); ++i)
		cout <<i<<": "<< mi[i]+1 <<" " << ma[i]+1<< endl;
*/
	Long TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC; ++tc)
	{
		cout << "Case #" << tc << ": ";
		cin >> N >> P;
		{
			Long cand = 0 , tmi = 1, d = (1LL)<<(N-1) , dif_pos = 2; 
			while( tmi + d <= P && d>0)
			{
				cand += dif_pos;
				tmi += d;
				dif_pos <<= 1;
				d >>= 1;
			}
			cout << min((1LL<<N)-1,cand) << " ";
		}
		{
			//max that got min of P or less
			Long cand = 0 , tmi = 1, d = 1 , dif_pos = (1LL)<<(N-1);
			while( tmi + d <= P )
			{
				cand += dif_pos;
				tmi += d;
				dif_pos >>= 1;
				d <<= 1;
			}
			cout << cand << "\n";
		}
	}
	
	
	
    return 0;
}


