/*
    Copyrights to Bipin.B ;)
    AMRITA SCHOOL OF ENGINEERING, Amritapuri
*/
#include<bits/stdc++.h>
using namespace std;
// MY MACROS
#define pb(n) push_back(n)
#define mp(a,b) make_pair(a,b)
#define M(arr) memset(arr,0,sizeof(arr))
#define MOD 1000000007
#define LL long long int
#define ULL unsigned long long int
bool visited[1000][1000];
char graph[1000][1000];
// Google Code Jam: 2nd question:
int main()
{

	long long  int t;
	cin>>t;
	long int count=1;
	while(t--)
	{
		int N, n;
		cin>>N;
		vector<long int> first,second;
		int answer = 0;
		for (int i = 0; i < N; i++)
		{
			cin>>n;
			answer = max(answer, n);
			first.push_back(n);
			second.push_back(n);
		}
		int temp = 0;
		while (true)
		{
			if (first.size() == 0)
				break;
			sort(first.begin(), first.end() );
			reverse(first.begin(),first.end());
			int present = first[0];
			int temporary = temp + present;
			answer = min(answer, temporary);
			if (present <= 3)
				break;
			if (present == 6)
			{
				first[0] = 3;
				first.push_back(3);
			}
			else if (present == 9)
			{
				first[0] = 3;
				first.push_back(6);
			}
			else if (present % 2 == 0)
			{
				first[0] = present / 2;
				first.push_back(present / 2);
			}
			else
			{
				first[0] = present / 2 + 1;
				first.push_back(present / 2);
			}
			temp++;
		}
		temp = 0;
		while (true)
		{
			if (second.size() == 0)
				break;
			sort(second.begin(), second.end() );
			reverse(second.begin(),second.end());
			int present = second[0];
			int temporary = temp + present;
			answer = min(answer, temporary);
			if (present <= 3)
				break;
			if (present % 2 == 0)
			{
				second[0] = present / 2;
				second.push_back(present / 2);
			}
			else
			{
				second[0] = present / 2 + 1;
				second.push_back(present / 2);
			}
			temp++;
		}

		cout<<"Case #"<<count<<": "<<answer<<"\n";
		count=count+1;
	}
	return 0;
}
