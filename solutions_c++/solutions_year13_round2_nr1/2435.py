#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <boost/regex.hpp>

using namespace std;

typedef vector<string>::iterator vst;
typedef vector<int>::iterator vit;

typedef map<pair<int,int>, int>::iterator mIt;

int osmos(int A, vector<int>& v, int i, int ans);
map<pair<int, int>, int> memo;

deque<int> Q;

int main(int argc, char** argv)
{
	if(argc<2)
		exit(0);

	//file input
	ifstream in;
	in.open(argv[1]);

	vector<int> v;

	int T = 0;
	in >> T;
	for(int _i=0; _i<T; _i++)
	{
		Q.clear();
		v.clear();
		memo.clear();
		int ans=0, A, N;

		cout << "Case #" << _i+1 << ": ";
		//cout << endl;

		in >> A >> N;

		for(int i=0; i<N; i++)
		{
			int _a;
			in >> _a;

			v.push_back(_a);
		}

		sort(v.begin(), v.end());

		// skip ahead to the smallest mote we can't absorb
		int i=0;
		for(;i<v.size(); i++)
		{
			//cout << "A: " << A << "\tv[i]: " << v[i] << endl;
			//if(A>1000000) { break; }
			if(v[i] < A) {
				A = A+v[i];
				continue;
			}

			Q.push_back(v[i]);

			/*
			if(A+A-1 > v[i])
			{
				A = A+A-1;
			}
			
			ans++;
			*/
			int a = osmos(A, v, i+1, ans);
			int b = osmos(A+A-1, v, i+1, ans);
			//cout << "a: " << a << "\tb: " << b << endl;

			if(b<=a)
			{
				A = A+A-1;
				while(Q.size()>0 && Q[0] < A)
				{
					A = A+Q[0];
					Q.pop_front();
				}
			}

			ans++;
		}

		/*
		if(i == v.size())
		{
			ans = 0;
		}
		else
		{
		}
		*/

		cout << ans << endl;
	}

	//cout << "Hello!" << endl;
	in.close();
	return 0;
}

int osmos(int A, vector<int>& v, int i, int ans)
{
	//if(A>1000000) { return 0; }
	//cout << "memo: " << memo << "\ti: " << i << "\tA: " << A << endl;
	int iOrig = i;
	/*
	int m = memo[A*100 + iOrig];
	if(m!=-1)
		return m;
	*/

	mIt it = memo.find(make_pair(A,i));
	if(it != memo.end())
	{
		return it->second;
	}

	for(;i<v.size(); i++)
	{
		//cout << "A: " << A << "\tv[i]: " << v[i] << endl;
		if(v[i] < A) {
			A = A+v[i];
			continue;
		}

		int a = osmos(A, v, i+1, ans);
		int b = osmos(A+A-1, v, i+1, ans);
		//cout << "a: " << a << "\tb: " << b << endl;

		if(b<=a)
		{
			A = A+A-1;
		}
		ans++;

		/*
		if(A+A-1 > v[i])
		{
			A = A+A-1;
		}
		
		ans++;
		*/
	}

	//cout << "memoizing ans: " << ans << "\tA: " << A << "\ti: " << iOrig << endl;
	//memo[A*100 + iOrig] = ans;
	memo[make_pair(A,i)] = ans;
	return ans;
}

