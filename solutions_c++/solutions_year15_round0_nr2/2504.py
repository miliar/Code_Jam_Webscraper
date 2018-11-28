#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

struct greater
{
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};

typedef vector<int> vi;

bool print(vi a)
{
	cerr<<"[";
	for(int i=0;i<a.size();i++)
		cerr<<a[i]<<",";
	cerr<<"]";
	return false;
}
map<vi,int> mem;

int search(vi a)
{
	sort(a.begin(), a.end(), greater());
	while(a.back()==0)a.pop_back();
	
	int mv=a[0],sv=a.back();
	if(mv<4)return mv;
	
	if(mem.find(a)!=mem.end())
		return mem[a];
	
	//cerr<<"searching:"<<print(a)<<endl;
	vi b(a);
	for(int i=0;i<b.size();i++)b[i]--;
	int baseline=search(b);
	for(int j=min(3,mv/2);j<=mv/2;j++)
	{
		vi c(a);
		c[0]=j;c.push_back(mv-j);
		baseline=min(baseline,search(c));
	}
	return mem[a]=baseline+1;
	
}

int calc()
{
	int n;vi a;
	cin>>n;
	for(int i=0;i<n;i++)
	{	int t;cin>>t;
		a.push_back(t);
	}
	return search(a);
}

int main()
{
	//cerr<<calc();return 0;
	int N;cin>>N;
	for(int i=0;i<N;i++)
	{
		cerr<<"Case #"<<(i+1)<<";"<<endl;
		cout<<"Case #"<<(i+1)<<": "<<calc()<<endl;
	}
	return 0;
}