#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <queue>
#include <set>

using namespace std;

void solve(int, int);
string next_string(set<int>, int);
void generate_ones(queue < set<int> >&, int);

int main()
{

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int Tc;
	cin >> Tc;
	int n, j;
	cin >> n >> j;
	
	solve(n, j);

	return 0;
}

void solve(int n, int J)
{
	cout<<"Case #1:\n";
  
    queue <set<int> > Q;
    
    generate_ones(Q, n);
    
	for (int i = 1; i <= J; ++i)
	{
       cout<< next_string(Q.front(), n);
       Q.pop();
       
		for (int j = 2; j <= 10; j++)
			cout << " " << j+1;
		cout << endl;
	}
}

void generate_ones(queue < set<int> >& Q, int n)
{
    set<int> tmp;
    for(int i=1;i<=n-3;i+=2)
    {
        for(int j=2;j<=n-2;j+=2)
        {
            tmp.insert(i);
            tmp.insert(j);
            Q.push(tmp);
            tmp.clear();
        }
    }
    for(int i=3;i<=n-3;i+=2)
    {
        for(int j=4;j<=n-2;j+=2)
        {
            tmp.insert(1);
            tmp.insert(2);
            tmp.insert(i);
            tmp.insert(j);
            Q.push(tmp);
            tmp.clear();
        }
    }
     for(int i=5;i<=n-3;i+=2)
    {
        for(int j=6;j<=n-2;j+=2)
        {
            tmp.insert(1);
            tmp.insert(2);
            tmp.insert(3);
            tmp.insert(4);
            tmp.insert(i);
            tmp.insert(j);
            Q.push(tmp);
            tmp.clear();
        }
    } 
}

string next_string(set<int> st, int n)
{
    string t = "";
	for (int i = 1; i <= n; ++i) t += '0';
	    t[0] = t[t.length() - 1] = '1';
    
    for(auto x: st)
        t[x]='1';

	return t;
}
