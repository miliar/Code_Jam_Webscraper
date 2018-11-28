#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> fairnsquare;

bool palindrome(long long n)
{
	long long num = n;
	long long res = 0ll;
	while (n > 0ll)
	{
		res = res * 10ll;
		res = res + (n % 10ll);
		n = n / 10ll;
	}
	if (num == res)
		return true;
	else
		return false;
}

void setup()
{
	for (long long i = 1ll; i < 10000000ll; i+=1ll)
	{
		if (palindrome(i) && palindrome(i*i))
		{
			fairnsquare.push_back(i*i);
		}
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	setup();
	scanf("%d",&T);
	for (int num = 1; num <= T; num++)
	{
		long long a,b;
		scanf("%lld %lld",&a,&b);
		int awal=fairnsquare.size(),akhir=fairnsquare.size();
		for (int i = 0; i < (int)fairnsquare.size(); i++)
		{
			if (fairnsquare[i] >= a && awal==(int)fairnsquare.size())
				awal = i;
			if (fairnsquare[i] > b && akhir==(int)fairnsquare.size())
				akhir = i;
		}
		printf("Case #%d: %d\n",num,akhir-awal);
	}
	return 0;
}
