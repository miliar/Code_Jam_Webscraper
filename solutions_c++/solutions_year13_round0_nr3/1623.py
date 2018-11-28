#include <iostream>
#include <fstream>

using namespace std;

ifstream palinsq;

void initialize()
{

};
void solve_case(int test_case)
{
	/*int cnt;
	long long int ln;
	cin>>cnt>>ln;
	cout<<(ln*ln)<<endl;*/
	palinsq.seekg (0);
	long long int low,high;
	int ncount;
	long long int palin;
	ncount=0;
	cin>>low>>high;
	for (int i = 0; i < 100000000 ; ++i)
	{       
		palinsq>>palin;
		if (palin>=low && palin<=high)
		{
			++ncount;
		}
		if (palin>high)
		{
			break;
		}
	}
	cout<<"Case #"<<test_case<<": "<<ncount<<endl;

};

int main()
{
	freopen("Clarge.in","r",stdin);
	freopen("Clarge.out","w",stdout);
	palinsq.open("Palin_sq.txt",ios_base::in);
	initialize();
	int T; scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);
	palinsq.close();
	return 0;
}