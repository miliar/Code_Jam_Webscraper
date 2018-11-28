#define PRODUCTION
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

void run()
{
	int n, A;
	int res;
	cin>>A>>n;
	vector<long long int> a(n);
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	sort(a.begin(),a.end());

	long long int curA=A;
	int i;
	for(i=0;i<n;i++)
	{
		if(curA>a[i]){
			curA+=a[i];
		}
		else{
			break;
		}
	}
	if(i==n)
	{
		cout<<"0\n";
		return;
	}
	
	if(A==1){
		cout<<n<<endl;
		return;
	}

	curA=A;
	res=0;
	int delta;
	for(i=0;i<n;i++)
	{
		delta=0;
		while(curA<=a[i]){
			curA=2*curA-1;
			delta++;
		}

		if(i+delta>=n){
			res+=n-i;
			break;
		}
		else{
			res+=delta;
			curA+=a[i];
		}
	}
	cout<<res<<"\n";
}


int main()
{
#ifdef PRODUCTION 
	string input_name = "A-small-attempt1(1).in";
	string output_name = "output.txt";
	freopen(input_name.c_str(),"r",stdin);
	freopen(output_name.c_str(),"w",stdout);
#endif

	int test;
	cin>>test;
	for(int i = 1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
	}
	return 0;
}