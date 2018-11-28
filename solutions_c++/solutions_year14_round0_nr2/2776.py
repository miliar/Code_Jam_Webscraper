#include <fstream>

using namespace std;


ifstream cin;
ofstream cout;


void solve(int k)
{
	double x,f,c;
	cin>>c>>f>>x;

	double result=x/2;
	double per=2;
	double wasted_time=0;
	while(1)
	{
		double temp_result= wasted_time+ c/per +x/(per+f);
		if(temp_result<result)
		{
			result=temp_result;
			wasted_time+=c/per;
			per=per+f;
			
		}
		else
			break;
	}

	cout<<"Case #"<<(k+1)<<": "<<result<<endl;
}

int main()
{
	cin.open("A-small-attempt1.in");
	cout.open("A-small-attempt1.out");
	int n;
	cin>>n;
	cout << fixed << showpoint;
	cout.precision(7);
	for(int i=0; i<n; ++i)
	{
		solve(i);
	}
	return 0;
}