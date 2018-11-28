#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;
typedef long long int int64;
#define MOD 1000000007


//int main(int argc, char* argv[])
int length;
int binsearch(int arr[], int key)
{
	int low = 0, mid,high = length - 1;
	while (low<=high)
	{
		mid = (low + high) / 2;
		if (arr[mid]>=key) high=mid-1;
		else low=mid+1;
	}
	if (arr[low] == key) return low;
	else return -1;
}

void reverse_string(char str[])
{
	char c;
	char *p, *q;

	p = str;
	if (!p)
		return;

	q = p + 1;
	if (*q == '\0')
		return;

	c = *p;
	reverse_string(q);

	while (*q != '\0') {
		*p = *q;
		p++;
		q++;
	}
	*p = c;

	return;
}
double Naomi[10], Ken[10];
int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	//code here
	int t,n;
	cin >> t;
	for (int testcase = 1; testcase <= t; testcase++)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> Naomi[i];
		for (int i = 0; i < n; i++)
			cin >> Ken[i];

		sort(Naomi, Naomi + n);
		sort(Ken, Ken + n);
		vector<double> Ken1(Ken,Ken+n);

		int score = 0;
		for (int i = n - 1; i >= 0; i--)
		{
			int j;
			if (Naomi[i]>Ken[i]) { j = 0; score++; }
			else
			{
				for (j = i; j >= 0; j--)
				if (Naomi[i] > Ken[j]) break;
				j++;
			}

			//array deletion
			for (int k = j; k <= i - 1; k++)
			{
				Ken[k] = Ken[k + 1];
			}
		}
		
		

		int cheat_score = 0;
		for (int i = 0; i <= n - 1; i++)
		{

			if (Naomi[i] < Ken1[0]) ;
			else
			{
				cheat_score++;
				//array deletion	
				for (int k = 0; k <= n - 2 - i; k++)
				{
					Ken1[k] = Ken1[k + 1];
				}

				//for (int mm = 0; mm <= n - 1 - i; mm++)
				//	cout << Ken1[mm] << " ";
				//cout << endl;
			}
		}
		cout <<"Case #"<<testcase<<": "<<cheat_score<<" "<<score<< endl;
	}
	//debug
	//for (vector<i64>::iterator it = sqr.begin(); it != sqr.end(); ++it)
	//cout << ' ' << *it;1
	//cout << '\n';
	//
	fclose(stdout);
	fclose(stdin);

	return 0;

}