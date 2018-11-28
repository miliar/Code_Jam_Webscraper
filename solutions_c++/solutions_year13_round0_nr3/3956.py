#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

class LargeNumber
{
private:
	static const int N = 100;
	static const int BASE = 1000000000;
	int data[N];
public:
	LargeNumber(const string &str);
	const LargeNumber& operator-=(const int B);
	string LargeNumber::toString()const;
};

LargeNumber::LargeNumber(const string &str)
{
	memset(data, 0, sizeof(data));
	int len = str.size();
	for(int i=0; i<len; i+=9)
	{
		int curnum = 0;
		for(int j=i+9; j>i; j--)
		{
			int pos = len-j;
			if(pos>=0)
			{
				int num = str[pos]-'0';
				curnum *= 10;
				curnum += num;
			}
		}
		data[i/9] = curnum;
	}
}

const LargeNumber& LargeNumber::operator-=(const int B)
{
	int i=0;
	data[0] -= B%BASE;
	data[1] -= B/BASE;
	while(data[i] < 0)
	{
		data[i] += BASE;
		data[++i]--;
	}
	return *this;
}

string LargeNumber::toString()const
{
	char buffer[N * 9];
	char str[10];
	int i;
	for(i=N-1; data[i]==0&&i>0; i--);
	sprintf(str, "%d", data[i--]);
	strcpy(buffer, str);
	for(; i>=0; i--)
	{
		sprintf(str, "%09d", data[i]);
		strcat(buffer, str);
	}
	return buffer;
}

const int N = 100;
static int sum[N+1];

void initComb(int *x, int k)
{
	for (int i = 0; i < k; i++)
		x [i] = i;
}

bool next_combination(int *x, int n, int k)
{
	int e = k-1;
	while(x[e] >= e+n-k)
		e--;
	if (e >= 0) {
		x[e]++;
		for (int i = e+1; i < k; i++)
			x[i] = x[i-1]+1;
		return true;
	} else {
		return false;
	}
}

string getSquare(const vector<ii> &num)
{
	int len = 2 * num[num.size()-1].first + 1;
	string result(len, '0');
	for (size_t i = 0; i <num.size(); i++) {
		for(size_t j = 0; j < i; j++) {
			result[num[i].first+num[j].first] += 2*num[i].second*num[j].second;
		}
		result[2*num[i].first] += num[i].second*num[i].second;
	}
	string number(num[num.size()-1].first + 1, '0');
	for (size_t i = 0; i <num.size(); i++)
		number[num[i].first] += num[i].second;
	number = number;
	return result;
}

int countWithLimit(int len, const string &limit)
{
	len = (len + 1) / 2;
	int count = 0;
	vector<ii> num;
	int *x = new int[100];

	// 2, 2
	if (len >= 2) {
		num.clear();
		num.push_back(ii(0, 2));
		num.push_back(ii(len-1, 2));
		count += getSquare(num) <= limit;
	}

	// 1, 1
	if (len >= 2) {
		num.clear();
		num.push_back(ii(0, 1));
		num.push_back(ii(len-1, 1));
		count += getSquare(num) <= limit;
	}

	// 1, 1, 1, 1
	if (len >= 4) {
		int n = len / 2 - 1;
		int k = 1;
		initComb(x, k);
		do {
			num.clear();
			num.push_back(ii(0, 1));
			num.push_back(ii(x[0]+1, 1));
			num.push_back(ii(len-x[0]-2, 1));
			num.push_back(ii(len-1, 1));
			count += getSquare(num) <= limit;
		} while (next_combination(x, n, k));
	}

	// 1, 1, 1, 1, 1, 1
	if (len >= 6) {
		int n = len / 2 - 1;
		int k = 2;
		initComb(x, k);
		do {
			num.clear();
			num.push_back(ii(0, 1));
			num.push_back(ii(x[0]+1, 1));
			num.push_back(ii(x[1]+1, 1));
			num.push_back(ii(len-x[1]-2, 1));
			num.push_back(ii(len-x[0]-2, 1));
			num.push_back(ii(len-1, 1));
			count += getSquare(num) <= limit;
		} while (next_combination(x, n, k));
	}

	// 1, 1, 1, 1, 1, 1, 1, 1
	if (len >= 8) {
		int n = len / 2 - 1;
		int k = 3;
		initComb(x, k);
		do {
			num.clear();
			num.push_back(ii(0, 1));
			num.push_back(ii(x[0]+1, 1));
			num.push_back(ii(x[1]+1, 1));
			num.push_back(ii(x[2]+1, 1));
			num.push_back(ii(len-x[2]-2, 1));
			num.push_back(ii(len-x[1]-2, 1));
			num.push_back(ii(len-x[0]-2, 1));
			num.push_back(ii(len-1, 1));
			count += getSquare(num) <= limit;
		} while (next_combination(x, n, k));
	}

	if (len % 2 == 1) {
		// 2, 1, 1
		if (len >= 3) {
			num.clear();
			num.push_back(ii(0, 1));
			num.push_back(ii((len-1)/2, 2));
			num.push_back(ii(len-1, 1));
			count += getSquare(num) <= limit;
		}

		// 2, 1, 1, 1, 1
		if (len >= 5) {
			int n = len / 2 - 1;
			int k = 1;
			initComb(x, k);
			do {
				num.clear();
				num.push_back(ii(0, 1));
				num.push_back(ii(x[0]+1, 1));
				num.push_back(ii((len-1)/2, 2));
				num.push_back(ii(len-x[0]-2, 1));
				num.push_back(ii(len-1, 1));
				count += getSquare(num) <= limit;
			} while (next_combination(x, n, k));
		}

		// 1, 1, 1
		if (len >= 3) {
			num.clear();
			num.push_back(ii(0, 1));
			num.push_back(ii((len-1)/2, 1));
			num.push_back(ii(len-1, 1));
			count += getSquare(num) <= limit;
		}

		// 1, 1, 1, 1, 1
		if (len >= 5) {
			int n = len / 2 - 1;
			int k = 1;
			initComb(x, k);
			do {
				num.clear();
				num.push_back(ii(0, 1));
				num.push_back(ii(x[0]+1, 1));
				num.push_back(ii((len-1)/2, 1));
				num.push_back(ii(len-x[0]-2, 1));
				num.push_back(ii(len-1, 1));
				count += getSquare(num) <= limit;
			} while (next_combination(x, n, k));
		}

		// 1, 1, 1, 1, 1, 1, 1
		if (len >= 7) {
			int n = len / 2 - 1;
			int k = 2;
			initComb(x, k);
			do {
				num.clear();
				num.push_back(ii(0, 1));
				num.push_back(ii(x[0]+1, 1));
				num.push_back(ii(x[1]+1, 1));
				num.push_back(ii((len-1)/2, 1));
				num.push_back(ii(len-x[1]-2, 1));
				num.push_back(ii(len-x[0]-2, 1));
				num.push_back(ii(len-1, 1));
				count += getSquare(num) <= limit;
			} while (next_combination(x, n, k));
		}

		// 1, 1, 1, 1, 1, 1, 1, 1, 1
		if (len >= 9) {
			int n = len / 2 - 1;
			int k = 3;
			initComb(x, k);
			do {
				num.clear();
				num.push_back(ii(0, 1));
				num.push_back(ii(x[0]+1, 1));
				num.push_back(ii(x[1]+1, 1));
				num.push_back(ii(x[2]+1, 1));
				num.push_back(ii((len-1)/2, 1));
				num.push_back(ii(len-x[2]-2, 1));
				num.push_back(ii(len-x[1]-2, 1));
				num.push_back(ii(len-x[0]-2, 1));
				num.push_back(ii(len-1, 1));
				count += getSquare(num) <= limit;
			} while (next_combination(x, n, k));
		}
	}

	delete []x;
	return count;
}

int f(const string &num)
{
	int len = num.size();
	if (len == 1) {
		int count = 0;
		if (num >= "1") count++;
		if (num >= "4") count++;
		if (num >= "9") count++;
		return count;
	}
	else if (len % 2 == 0) {
		return sum[len-1];
	} else {
		return sum[len-1] + countWithLimit(len, num);
	}
}

string solve(const string &A, const string &B)
{
	LargeNumber largeA(A);
	largeA -= 1;
	int countA = f(largeA.toString());
	int countB = f(B);
	char answer[11];
	sprintf(answer, "%d", countB - countA);
	return answer;
}

void preprocess()
{
	int wei[N+1];

	// even is 0;
	for (int i = 0; i <= N; i+=2)
		wei[i] = 0;

	// odd count
	wei[1] = 3;
	for (int i = 3; i <= N; i+=2) {
		string maxNum(i, '9');
		wei[i] = countWithLimit(i, maxNum);
	}

	// cumulate
	for (int i = 1; i <= N; i++)
		sum[i] = sum[i-1] + wei[i];
}

void readinput(string &A, string &B)
{
	cin>>A>>B;
}

vs getoutput()
{
	string A, B;
	readinput(A, B);
	string answer = solve(A, B);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
	freopen("test\\C-small-attempt0.in", "r", stdin);freopen("test\\C-small-attempt0.out", "w", stdout);
//	freopen("test\\C-large.in", "r", stdin);freopen("test\\C-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for(int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}