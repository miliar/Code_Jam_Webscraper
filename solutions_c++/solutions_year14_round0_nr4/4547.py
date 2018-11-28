#include <iostream>
#include <vector>

using namespace std;

int T, N;

bool cmp(double a, double b) { return a > b; }

int dwar(vector<double> &nd, vector<double> &kd)
{
    int cnt = 0;
    int len = nd.size();
    for (int i=0; i<len; ++i) {
	double k = kd[0];
	kd.erase(kd.begin());
	if (nd[0] > k) {
	    nd.erase(nd.begin());
	    cnt += 1;
	    continue;
	} else {
	    nd.pop_back();
	}
    }

    return cnt;
}

int war(vector<double> &nd, vector<double> &kd)
{
    int cnt = 0;
    int len = kd.size();
    for (int m=0; m<len; ++m) {
	double n = nd[0];
	nd.erase(nd.begin());

	int index = -1;
	double k = -1;
	int kl = kd.size();
	for (int i=kl-1; i>=0; --i) {
	    if (kd[i] > n) {
		index = i;
		break;
	    }
	}
	if (index == -1) index = kl-1;
	k = kd[index];
	kd.erase(kd.begin()+index);

	if (k>n) cnt += 1;
    }

    return len - cnt;
}

int main()
{
    cin >> T;
    for (int k=1; k<=T; ++k) {
	cin >> N;
	double num;
	vector<double> nao;
	vector<double> ken;

	for (int i=0; i<N; ++i) {
	    cin >> num;
	    nao.push_back(num);
	}
	sort(nao.begin(), nao.end(), cmp);
	for (int i=0; i<N; ++i) {
	    cin >> num;
	    ken.push_back(num);
	}
	sort(ken.begin(), ken.end(), cmp);

	vector<double> nao1 = nao;
	vector<double> ken1 = ken;
	
	int rst1 = dwar(nao, ken);
	/*
	for (int i=0; i<N; ++i) cout << nao[i] << " ";
	cout << endl;
	for (int i=0; i<N; ++i) cout << ken[i] << " ";
	cout << endl;
	*/
	int rst2 = war(nao1, ken1);

	printf("Case #%d: %d %d\n", k, rst1, rst2);
    }
}
