#include <queue>
#include <iostream>
#include <string>
#include <algorithm>


using namespace std;

class party
{
	public:
	int num;
	char symbol;
	party(int n,int i)
	{
		num=n;
		symbol='A'+i;
	}
};

struct comparator {
	bool operator()(party& p1, party& p2) 
	{
		return p1.num < p2.num;
	}
};

void solve(int case_no)
{
	priority_queue<party, std::vector<party>, comparator> maxHeap;
	int n,num;
	cin>>n;
	std::vector<string> ans(600);
	int l=0;
	for (int i = 0; i < n; ++i)
	{
		/* code */
		cin>>num;
		maxHeap.push(party(num,i));
	}
	bool alt=false;
	while(!maxHeap.empty())
	{
		party k1=maxHeap.top();
		maxHeap.pop();
		char k1c=k1.symbol;
		k1.num--;
		if(k1.num>0) maxHeap.push(k1);
		ans[l]=ans[l]+k1c;
		//cout<<ans[l]<<" dfd "<<l<<endl;
		if(alt) l++;
		alt=!alt;
	}
	if(alt) l++;
	//cout<<l;
	cout<<"Case #"<<case_no<<": ";
	if(ans[l-1].length()==1) swap(ans[l-1],ans[l-2]);
	for (int i = 0; i < l; ++i)
	{
		cout<<ans[i]<<" ";
	}
	cout<<endl;

	return;
}

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		solve(i+1);
	}
	return 0;
}