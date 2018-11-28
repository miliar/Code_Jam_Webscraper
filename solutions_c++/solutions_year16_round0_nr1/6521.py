#include "iostream"
using namespace std;
int counter()
{
	int N,ans;
	int temp=0,sum=0;
	int b[10]={0};
	cin >> N;
	int count =0;
	for (int i = 0; i < 10000000; ++i)
	{
		temp = (i+1)*N;
		while (temp/1)
		{
			b[temp%10]=1;
			temp/=10;
		}
		count=0;
		if ((b[1]==1&&b[2]==1&&b[3]==1&&b[4]==1&&b[5]==1&&b[6]==1&&b[7]==1&&b[8]==1&&b[9]==1&&b[0]==1))
		{
			ans = (i+1)*N;
			break;
		}
		else if (i+1==10)
		{
			ans = -1;
		}
		// cout << endl;
	}
	//cout << count;
	if (ans ==-1)
	{
		cout << "INSOMNIA";
	}
	else cout << ans;

	return ans;
}
int main(int argc, char const *argv[])
{
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cout << "Case #"<< i+1 <<": ";
		counter();
		cout << endl;
	}
	return 0;
}