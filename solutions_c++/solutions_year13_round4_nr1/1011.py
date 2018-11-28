#include <iostream>
#include <algorithm>
#include <math.h>
#include <set>
#include <iomanip>
#include <vector>
using namespace std;

//long long N;
static int cc = 1000002013;

int cost(int o, int e, int p, int N)
{
	if (o==e)
		return 0;
	
	int d = e-o;

	return ((2*N+1-d)*d/2)*p%cc;
}

class A
{
public:
	int o;
	int e;
	int p;
};

bool comp_o(const A& a, const A& b)
{
	return a.o < b.o;
}
bool comp_e(const A& a, const A& b)
{
	return a.e < b.e;
}

class pass
{
	int s;
	int total;
	int out;
};

void tst()
{
	int N;
	int M;

	cin >> N;
	cin >> M;

	A data[1000];
	int in[101];
	int out[101];
	int pass[101];

	for (int i=1; i<=N; i++) {
		in[i]=out[i]=pass[i] = 0;
	}

	for (int i=0; i<M; i++) {
		cin >> data[i].o >> data[i].e >> data[i].p;
	}
	std::vector<A> m_v (data, data+M);
	
	int orig = 0;

	for (int i=0; i<M; i++) {
		orig += cost(data[i].o, data[i].e, data[i].p, N);
	}
//	cout << orig << endl;

	std:sort(m_v.begin(), m_v.end(), comp_o);

	
	for (std::vector<A>::iterator it=m_v.begin(); it!=m_v.end(); ++it) {
	//	cout << (*it).o << (*it).e << endl;
		in[(*it).o] += (*it).p;
		out[(*it).e] += (*it).p;
		pass[(*it).o] += (*it).p;
	}

	int sum = 0;

	for (int i=1; i<=N; i++) {
		if (out[i] > 0) {
			for (int j=i; j>=1; j--) {
				if (pass[j] >= out[i]) {
					sum += cost(j, i, out[i], N);
					pass[j] -= out[i];
					break;
				} else if (pass[j] > 0) {
					sum  += cost(j, i, pass[j], N);
					out[i] -= pass[j];
					pass[j] = 0;
				}
			}
		}
	}

//	cout << sum << endl;

	int x = (1000002013-sum + orig)%1000002013;	
	cout << x << endl;

	return;
}

int main()
{
    int t;
    cin >> t;
    for(int i=0;i<t;i++) {
		cout << "Case #" << i+1 << ": ";
		tst();
		cout << endl;
	}
}



