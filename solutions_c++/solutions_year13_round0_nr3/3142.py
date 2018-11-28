#include<iostream>
#include<fstream>
#include<vector>
#define PR(X) //cout << (X) << endl
using namespace std;
ifstream in("3.in");
ofstream out("3.out");
vector<long long> ans;
long long sqr(long long x){return x*x;}
long long reverse(long long x, int k){
	long long ans = 0;
	for (int i = 1; i<=k; i++){
		ans = ans * 10 + x % 10;
		x /= 10;
	}
	return ans;
}
bool check(long long x){

	int a[100], len = 0;
	while (x != 0){
		len++;
		a[len] = x % 10;
		x /= 10;
	}
	bool isok = true;

	for (int i = 1; i<=len; i++)
		if (a[i] != a[len+1-i]) isok = false;
	return isok;
}
long long polin2(long long x, int k){
	long long tmp = 1, now = x;
	for (int i = 1; i<=k; i++){
		tmp *= 10;
		now /= 10;
	}
	return reverse(x, k) * tmp + x;
}
long long polin1(long long x, int k){
	long long tmp = 1, now = x;
	for (int i = 1; i<=k; i++){
		tmp *= 10;
		now /= 10;
	}
	return reverse(x, k)/10 * tmp + x;
}
long long getans(long long x){
	int i;
	for (i = 0; i<=ans.size(); i++)
		if (sqr(ans[i])>x) {PR(ans[i]);break;}
	return i;
}
long long (*polin[2]) (long long x, int k) = {polin1, polin2};

int main(){
	//PR(reverse(1234));

	int bas = 1;
	for (int i = 1; i <= 4; i++){
		//PR(i);
		int l = bas, r = bas*10-1;
		for (int k = 0; k <= 1; k++)
			for (int j = 1; j <= r; j++)
				if (j % 10 != 0){
					long long rev = polin[k](j,i);
					//if (rev == 10000000001) PR(rev);
					if (check(sqr(rev))){
						cout << sqr(rev) << endl;
						ans.push_back(rev);
					}
				}
		bas *= 10;
	}
	PR(ans[ans.size()-1]);
	//polinf polin[2];
	int iTestSum;
	in >> iTestSum;
	for (int iTest = 1; iTest <= iTestSum; iTest++){
		out << "Case #" << iTest << ": ";
		long long x, y;
		in >> x >> y;
		out << getans(y) - getans(x-1);
		out << endl;
	}
}
