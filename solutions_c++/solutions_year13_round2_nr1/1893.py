#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>
#include <queue>
#include <deque>
using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)

int main()
{ 
	ifstream in("large.in");
	ofstream out("output.txt");
	//ofstream log("log.log");
	int t,n;
	int a,b;
	ll sum = 0;
	in>>t;
	REP(q,t)
	{
		
		in>>a>>n;
		
		/*if (q == 73) 
			cout<<"LOL!";*/
		//	log<<q<<" : "<<a<<" "<<n<<"\n";
		
		//if ((a == 1) && ( n == 9))
		//if (q == 10)
		//cout<<q;
		//cout<<q<<"\n";*/
		sum = a;
		int rez = 0;
		vector<int> mas(n);
		REP(i,n)
		{
			in>>mas[i];
		//	log<<mas[i]<<" ";
		}
		//log<<"\n";
		if (a == 1)
		{
			out<<"Case #"<<q+1<<": "<<n<<'\n';
		//	log<<"ans="<<n<<"\n";
			continue;
		}
		set<int> kol;

		sort(mas.begin(), mas.end());
		REP(i,n)
		{
			if (mas[i] >= sum) 
			{
				int t = sum;
				int y = 0;
				while (t <= mas[i]) 
				{
					y++;
					t += (t-1);
				}
				if (y > n-i)
				{
					rez += (n-i);
					break;
				}
				else
				{
					kol.insert(rez + (n - i) );
					sum = t + mas[i];
					rez += y;
				}
				continue;
			}
			
			
			if (mas[i] < sum)
			{
				sum += mas[i];
				continue;
			}
			if (mas[i] < sum*2-1)
			{
				rez++;
				sum += (sum + mas[i] -1);
				continue;
			}
		}
		kol.insert(rez);
		out<<"Case #"<<q+1<<": "<<*kol.begin()<<'\n';
		//log<<"ans="<<*kol.begin()<<"\n";
	}
	in.close();
	out.close();
	//system("pause");
	return 0;
}