#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<cstring>
#include<string>
#include<map>
using namespace std;

/*
void Vec()
{
	vector<int> A;  
	A.push_back(10);
	int n = A.size();
	A.clear();
	if(!A.empty())
	{
		int sum = 0;
		for(vector<int>::iterator it = A.begin();it != A.end();it++)
		{
			sum += *it;
		}

		vector<int>::iterator it = A.begin();
		A.erase(it);
		sort(A.begin(),A.end());
		it = max_element(A.begin(),A.end());
		it = min_element(A.begin(),A.end());
		A.insert(it,10);
		A.pop_back();
		int a = A.front();
		int b = A.back();
	}
}

void Pairs()
{
	pair<int,int> A;
	A.first = 10;
	A.second = 15;
}

void STRING()
{
	string a = "Hello";
	a = a + a;
	string b = a.substr(0,3);
	int t = a.find_first_of('a');
	cout<< a;
}

void SET()
{
	set<int> A;
	A.insert(10);
	A.erase(10);
	int t = A.count(10);
	set<int>::iterator it = A.find(10);
	it = A.upper_bound(10);//>10
	it = A.lower_bound(10);//<=10

	A.clear();
	if(!A.empty())
	{
		int sum = 0;
		for(set<int>::iterator it = A.begin();it != A.end();it++)
		{
			sum += *it;
		}
	}
}

void MAP()
{
	map<int,int> A;
	A[10]=20;
	A.erase(10);
	A.clear();
	A.size();
	map<int,int>::iterator it = A.find(10);

	if(!A.empty())
	{
		int sum = 0;
		for(map<int,int>::iterator it = A.begin();it != A.end();it++)
		{
			sum += it->second;
		}
	}
}

struct fun{
  int  xnode, weight;
  fun() {}
  fun(int t, int w) : xnode(t), weight(w) {}
  bool operator < (const fun &that) const {
    return weight > that.weight;
  }
};

void Priority_Queue()
{
	priority_queue<fun> q;
	q.top().weight;
	q.pop();
	q.push(fun(1,2));
	int i = q.size();
	if(!q.empty())
	{}
}
*/

int A[100009],B[100009];
char temp[20];
int N = 0;

int findV(__int64 x)
{
	if(x==0)
		return 0;

	int st = 0, ed = N-1;
	int mid = (st+ed)/2;

	while(st<=ed)
	{
		__int64 t = A[mid];
		t = t * t;
		if(t == x)
			break;
		else if(t>x)
			ed = mid - 1;
		else
			st = mid + 1;

		mid = (st+ed)/2;
	}

	while(mid-1>=0)
	{
		__int64 t = A[mid];
		t = t * t;
		if(t <= x)
			break;
		else
			mid--;	
	}

	while(mid+1<N)
	{
		__int64 t = A[mid+1];
		t = t * t;
		if(t > x)
			break;
		else
			mid++;
	}

	return B[mid];
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	for(int i=1;i<10000000;i++)
	{
		temp[0]=0;
		sprintf(temp,"%d",i);
		bool flag = 1;
		int t = strlen(temp);
		for(int j=0;j<t;j++)
			if(temp[j]!=temp[t-j-1])
			{
				flag = 0;
				break;
			}

			if(flag)
			{
				A[N]=i;
				N++;
			}
	}

	B[0]=1;

	for(int i=1;i<N;i++)
	{
		B[i]=B[i-1];

		__int64 mul = A[i];
		mul = mul * mul;

		temp[0]=0;
		sprintf(temp,"%I64d",mul);
		bool flag = 1;
		int t = strlen(temp);
		for(int j=0;j<t;j++)
			if(temp[j]!=temp[t-j-1])
			{
				flag = 0;
				break;
			}

			if(flag==1)
				B[i]++;
	}

	int cas;

	scanf("%d",&cas);

	for(int cas1=1;cas1<=cas;cas1++)
	{
		__int64 x,y;
		scanf("%I64d %I64d",&x,&y);
		printf("Case #%d: %d\n",cas1,findV(y)-findV(x-1));
	}

	return 0;    
}
