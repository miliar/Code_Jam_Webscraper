#include <fstream>
#include <algorithm>

using namespace std;


ifstream cin;
ofstream cout;


void solve(int k)
{
	int n;
	double a[1001];
	double b[1001];
	cin>>n;
	for(int i=0;i<n;i++)
		cin>>a[i];
	for(int i=0;i<n;i++)
		cin>>b[i];
	sort(a,a+n);
	sort(b,b+n);

	int i,j;
	int x,y;
	for(i=0,j=0;i<n;i++)
	{
		if(a[j]<b[i])
			j++;
	}
	y=n-j;

	for(i=0,j=0;i<n;i++)
	{
		if(b[j]<a[i])
			j++;
	}
	x=j;

	cout<<"Case #"<<(k+1)<<": "<<x<<" "<<y<<endl;
}

int main()
{
	cin.open("A-small-attempt1.in");
	cout.open("A-small-attempt1.out");
	int n;
	cin>>n;
	for(int i=0; i<n; ++i)
	{
		solve(i);
	}
	return 0;
}