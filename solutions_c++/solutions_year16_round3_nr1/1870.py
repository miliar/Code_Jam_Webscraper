#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Node{
	int count;
	char key;
};
struct more_func
{
	inline bool operator()(const Node& node1,const Node& node2){
		return (node1.count>node2.count);
	}
};

int getSum(vector<Node> v)
{
	int sum=0;
	for(size_t i=0;i<v.size();i++){
		sum+=v[i].count;
	}
	return sum;
}

void solve()
{
	int N;cin>>N;	
	vector<Node> v;
	Node temp;char tempChar='A';
	for(int j=0;j<N;j++)
	{
		cin>>temp.count;
		temp.key=tempChar;
		v.push_back(temp);
		tempChar++;
	}
	int sum=getSum(v);
	while(sum>0){
		sort(v.begin(),v.end(),more_func());
		if(v[1].count>(sum-1)/2)
		{
			cout<<v[0].key<<v[1].key<<" ";
			v[0].count--;
			v[1].count--;
		}
		else{
		cout<<v[0].key<<" ";
		v[0].count--;
		}
		sum=getSum(v);		
	}
	cout<<endl;

}
int main()
{
	int T;cin>>T;
	for(int test_case=0;test_case<T;test_case++){
		cout<<"Case #"<<test_case+1<<": ";
		solve();
	}
	return 0;
}