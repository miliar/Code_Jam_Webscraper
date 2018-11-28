#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

const int MAXV = 10000000;
bool checkPalindrome(long long v)
{
	if(v == 0) return true;
	const int MAXL = 20;
	char s[MAXL];
	int len = 0, hl;
	while(v)
	{
		s[len++] = v%10;
		v /= 10;
	}
	
	hl = len>>1;
	for(int i = 0; i < hl; i++)
		if(s[i] != s[len-1-i])
			return false;
	return true;
}

vector <long long> sroot;

int main()
{
	for(long long i = 1; i <= MAXV; i++)
		if( checkPalindrome(i) && checkPalindrome(i*i) )
			sroot.push_back( i );
	//fprintf(stderr, "SR %d\n", sroot.size());
	int T;
	scanf("%d", &T);
	
	for(int tc = 1; tc <= T; tc++)
	{
		long long A, B;
		cin>>A>>B;
		int low = 0, up = sroot.size()-1, mid, lowm = -1, upm = -1;
		
		while(low <= up)
		{
			mid = (low+up)/2;
			if(sroot[mid]*sroot[mid] < A) low = mid+1;
			else lowm = mid, up = mid-1;
		}
		
		low = 0, up = sroot.size()-1;
		while(low <= up)
		{
			mid = (low+up)/2;
			if(sroot[mid]*sroot[mid] > B) up = mid-1;
			else upm = mid, low = mid+1;
		}
		printf("Case #%d: ", tc);
		if(lowm == -1 || upm == -1) cout<<0<<endl;
		else cout<<upm-lowm+1<<endl;
	}
	
	return 0;
}