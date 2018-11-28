#include <iostream>
#include <string>
using namespace std;

string result;

void list(int N, long long P)
{
	if(N==0) return;
	if(P>1<<(N-1))
	{
		result += 'L';
		list(N-1,P-(1LL<<(N-1)));
	}
	else
	{
		result += 'W';
		list(N-1,P);
	}
}

string getbest(int N, long long p)
{
	long long ans = (1LL<<N) - p;
	int c = 0;
	ans >>= 1;
	while(ans)
	{
		c++;
		ans >>= 1;
	}
	string re ="";
	for(int i=0;i<c;i++)
	{
		re += 'W';
	}
	for(int i=c;i<N;i++)
	{
		re += 'L';
	}
	return re;
}

string getworst(int N, long long p)
{
	long long ans = p+1;
	int c = 0;
	ans >>= 1;
	while(ans)
	{
		c++;
		ans >>= 1;
	}
	string re ="";
	for(int i=0;i<c;i++)
	{
		re += 'L';
	}
	for(int i=c;i<N;i++)
	{
		re += 'W';
	}
	return re;
}

long long findworst(string standard, int N)
{
	long long left = 0;
	long long right = (1LL<<N) - 1;
	while(left < right)
	{
		long long mid = (left + right + 1) >> 1;
		string temp = getworst(N,mid);
		if(temp < standard)
		{
			right = mid-1;
		}
		else
		{
			left = mid;
		}
	}
	return left;
}

long long findbest(string standard, int N)
{
	long long left = 0;
	long long right = (1LL<<N) - 1;
	while(left < right)
	{
		long long mid = (left + right) >> 1;
		string temp = getbest(N,mid);
		if(temp >= standard)
		{
			left = mid + 1;
		}
		else
		{
			right = mid;
		}
	}
	return left;
}


int main()
{
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		int N;
		long long P;
		cin >> N >> P;
		if(P == (1 << N))
		{
			cout << "Case #" << c << ": " << ((1LL << N)-1) << " " << ((1LL << N)-1) << endl;
		}
		else
		{
			result = "";
			list(N,P);
			string standard = result;
			//cout << "Last price: " << standard << endl;
			long long record1 = findworst(standard,N);
			//cout << "First none price: " << standard << endl;
			long long record2 = findbest(standard,N);
			//cout << result << endl;
			cout << "Case #" << c << ": " << record1 << " " << record2-1 << endl;
		}
	}
}