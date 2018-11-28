#include <iostream>

using namespace std;

void initialize()
{

};
void solve_case(int test_case)
{
	int radius,rings;
	int area,paint;
	rings=0;
	cin>>radius>>paint;
	while(true)
	{
		area=2*radius+1;
		if (paint < area)
		{
			break;
		}
		else
		{
			++rings;
			radius+=2;
			paint-=area;
		}
	}
	if (rings<1)
	{
		cout<<"Case #"<<test_case<<": "<<1<<endl;
	} 
	else
	{
		cout<<"Case #"<<test_case<<": "<<rings<<endl;
	}

};

int main()
{
	freopen("Asmall.in","r",stdin);
	freopen("Asmall.out","w",stdout);
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}