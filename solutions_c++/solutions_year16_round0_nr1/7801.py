#include "iostream"
#include "vector"
//#include "algorithm"
using namespace std;
vector <int>  arr;
vector <int>  reff;
int learn_digit(long int n, int m)
{
	if (arr!=reff)
	{   
		long int tempn = n*m;
		while (tempn/10)
		{
			arr[tempn % 10] = 0;
			tempn = tempn / 10;
		}
		arr[tempn] = 0;
		if (arr != reff)
			learn_digit(n, m + 1);
		else
			return m;
	}	
	else
	   return m;
}
int main(){
	int T,  out;
	long int N;
	//freopen("input.txt", "r", stdin);
	//freopen("outputAlarge.txt", "w", stdout);
	cin >> T;
	int t = 0;
	reff.assign(10,0);
	while (T--)
	{
		arr.assign(10, 1);
		cin >> N;
		t++;
		if (N != 0)
		{
			out = learn_digit(N, 1);
			cout << "Case #" << t <<": " << out*N << endl;
		}
		else
			cout << "Case #" << t <<": "<< "INSOMNIA" << endl;

	}
	return 0;
}