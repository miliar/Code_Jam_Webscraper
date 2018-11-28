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


int A[1009],B[1009],C[1009],D[1009];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;

	scanf("%d",&cas);

	for(int cas1=1;cas1<=cas;cas1++)
	{
		int n;
		scanf("%d",&n);

		int maxi_index = 0,temp_maxi =0;

		for(int i=0;i<n;i++)
		{
			scanf("%d",&A[i]);
			B[i]=A[i];
			C[i]=i;

			if(A[i]>temp_maxi)
			{
				temp_maxi = A[i];
				maxi_index = i;
			}
		}

		for(int i=0;i<n-1;i++)
			for(int j=0;j<n-1-i;j++)
				if(B[j]>B[j+1])
				{
					B[n]=B[j+1];
					B[j+1]=B[j];
					B[j]=B[n];

					C[n]=C[j+1];
					C[j+1]=C[j];
					C[j]=C[n];
				}

		int left = 0;
		int right = 0;
		int maxi = 0;

		for(int i=0;i<n-1;i++)
		{
			int t = C[i];
			int t1 = 0;
			int t2 = 0;

			for(int j=t-1;j>=0;j--)
				if(A[j]!=-1)
					t1++;

			for(int j=t+1;j<n;j++)
				if(A[j]!=-1)
					t2++;

			A[t] = -1;

			int leftT = left + t1;

			if(leftT>right+t1)
				leftT = right + t1;

			int rightT = right + t2;

			if(rightT > left + t2)
				rightT = left + t2;

			left = leftT;
			right = rightT;
		}
		
		maxi = left;

		if(maxi>right)
			maxi = right;

		printf("Case #%d: %d\n",cas1,maxi);
	}

	return 0;    
}
