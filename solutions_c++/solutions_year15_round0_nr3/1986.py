
#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstdlib>

#pragma warning (disable:4996)
#define I 2
#define J 3
#define K 4

using namespace std;
char s[10002];
int arr[10002];
int table[5][5] = {
{ 0, 0, 0, 0, 0},
{ 0, 1, I, J, K},
{ 0, I, -1, K, -J}, 
{ 0, J, -K, -1, I}, 
{ 0, K, J, -I, -1}};

int mul(const int &a, const int &b)
{
	bool plus = (a * b) >= 0;
	int res = table[abs(a)][abs(b)];
	if (plus)
		return res;
	else
		return -res;
}

int begin_at[10002];
int end_with[10002];

void test_case()
{
	int n;
	long long x;
	long long nx;
	int onetime = 1;
	int freq = 1;
	int temp;
	bool plus = true;

	cin >> n >> x;
	nx = n * x;
	scanf("%s", s);
	/* input */
	for (int i = 0; i < n; i++)
		arr[i] = s[i] - 'i' + I;
	
	/* get one time */
	for (int i = 0; i < n; i++)
	{
		onetime = mul(onetime, arr[i]);
	}

	/* get - 1 */
	temp = 1;
	for (int i = 0; i < x; i++)
	{
		temp = mul(temp, onetime);
	}
	
	//can't
	if (temp != -1 || nx < 3)
	{
		cout << "NO" << endl;
		return; 
	}

	/*  get freq */
	temp = onetime;
	freq = 1;
	do{
		freq++;
		temp = mul(temp, onetime);
	} while (temp != onetime);
	//cout << "freq" << freq << endl;

	long long rec_len = freq * n;

	////get end with 
	//end_with[0] = arr[0];
	//for (int i = 1; i < n; i++)
	//{
	//	end_with[i] = mul(end_with[i - 1], arr[i]);
	//}

	////get start_at
	//begin_at[n - 1] = arr[n - 1];
	//for (int i = n - 2; i >= 0; i--)
	//{
	//	begin_at[i] = mul(arr[i], begin_at[i + 1]);
	//}
	//find l 
	long long l = 0;
	bool lfind = false;
	temp = 1;
	for (int i = 0; i < rec_len && l < nx; i++)
	{
		int idx = l % n;
		temp = mul(temp, arr[idx]);
		if (temp == I || temp == -I)
		{
			lfind = true;
			break;
		}
		l++;
	}

	long long r = nx - 1;
	bool rfind = false;
	temp = 1;
	for (int i = 0; i < rec_len && r>=0; i++)
	{
		int idx = r % n;
		temp = mul(arr[idx], temp);
		if (temp == K || temp == -K)
		{
			rfind = true;
			break;
		}
		r--;
	}
	if ( lfind && rfind && (r- l) > 1)
	{
		cout << "YES" << endl;
	}
	else
	{
		cout << "NO" << endl;
	}


}
int main()
{
	int t;
	cin >> t;
	for(int i=0; i<t; i++){
		printf("Case #%d: ", i + 1);
		test_case();
	}
	return 0;
}