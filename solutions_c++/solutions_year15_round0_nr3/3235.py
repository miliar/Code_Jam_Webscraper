#include <iostream>
#include <map>
#include <cstdio>
using namespace std;

map<char,int> q2i;
char i2q[] = {'0', '1', 'i', 'j', 'k'};

int mul[5][5] = {
	{0},
	{0, 1, 2, 3, 4},
	{0, 2, -1, 4, -3},
	{0, 3, -4, -1, 2},
	{0, 4, 3, -2, -1},
};

struct Q {
	int sign;
	int value;

	Q() {}
	Q(int value) {
		if (value > 0) {
			this->sign = 1;
			this->value = value;
		} else {
			this->sign = -1;
			this->value = value * -1;
		}
	}
	Q operator*(const Q& q) {
		Q ret = Q(1);
		ret.value = mul[this->value][q.value];
		ret.sign = this->sign * q.sign;
		if (ret.value < 0) {
			ret.sign *= -1;
			ret.value *= -1;
		}
		return ret;
	}
	friend ostream &operator<<(ostream& out, const Q& q) {
		if (q.sign < 0) out << "-";
		out << i2q[q.value];
		return out;
	}
};

Q num[10010];
Q prefix[10010];
char str[10010];
int n, l, x;

Q mul_range(int start, int end)
{
	Q ret = prefix[start] * prefix[end];
	if (prefix[start].value != 1)
		ret.sign *= -1;
	return ret;
}

bool check(Q& a, Q& b, Q& c)
{
	if (a.value == 2 && b.value == 3 && c.value == 4 && a.sign == 1 && b.sign == 1 && c.sign == 1)
		return true;
	return false;
}

int main()
{
	q2i['1'] = 1;
	q2i['i'] = 2;
	q2i['j'] = 3;
	q2i['k'] = 4;

	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		cin >> l >> x >> str;
		n = l * x;
		if (l == 1 || l*x < 3) {
			printf("Case #%d: NO\n", kase);
			continue;
		}
		for (int i = 0; i < x; i++)
			for (int j = 0; j < l; j++)
				num[i*l+j] = Q(q2i[str[j]]);

		prefix[0] = Q(1);
		for (int i = 0; i < n; i++)
			prefix[i+1] = prefix[i] * num[i];

		bool ok = false;
		for (int i = 1; i < n-1 && !ok; i++)
			for (int j = i+1; j < n && !ok; j++) {
				Q a = mul_range(0, i);
				Q b = mul_range(i, j);
				Q c = mul_range(j, n);
				ok = check(a, b, c);
			}
		printf("Case #%d: %s\n", kase, ((ok) ? "YES" : "NO"));
	}
	return 0;
}
