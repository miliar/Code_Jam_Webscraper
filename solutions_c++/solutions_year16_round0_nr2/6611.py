#include "iostream"
using namespace std;
int counter()
{
	string a;
	cin >> a;
	int count = 0;
	for (int i = 0; i < a.size(); ++i)
	{
		if (a[i]!=a[i+1]&&a[i+1]!='\0')
		{
			// for (int j = 0; j < i+1; ++j)
			// {
			// 	a[j]=a[i+1];
			// }
			count ++;
			//cout << a << endl;
		}
		if (a[i+1]=='\0'&&a[i]=='-')
		{
			count++;
		}
	}
	cout << count;
	return 0;
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