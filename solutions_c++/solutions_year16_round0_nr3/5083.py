#include<iostream>
#include<vector> 
#include<cmath>
#include<cstring>
#include<algorithm>
#include<time.h>
using namespace std;
const int MAXN=70001;
bool isp[MAXN];
vector<int> primes;
void genp(){
	memset(isp,true,sizeof(isp));
	isp[0]=false; isp[1]=false;
	for (int i=2;i<sqrt(MAXN)+1;i++){
		for (int j=2*i;j<MAXN;j+=i)
			isp[j]=false;
	}
	for (int i=0;i<MAXN;i++)
		if (isp[i])
			primes.push_back(i);
}
string binary(int x){
	if (x==0) return "0";
	string s="";
	while (x>0){
		if (x&1) s+="1";
		else s+="0";
		x>>=1;
	}
	reverse(s.begin(),s.end());
	return s;
}
vector<long long > check(int x,int n){
	vector<long long > a;
	for (int i=2;i<=10;i++){
		long long y=0;
		for (int j=n-1;j>=0;j--){
			y*=i;
			if (x&(1<<j))
				y+=1;
		}
		bool flag=false;
		int cnt=0;
		for (long long j=2;j<y;j++){
			if (y%j==0){
				a.push_back(j);
				flag=true;
				break;
			}
			cnt++;
			if (cnt>10000000) break;
		}
		if (!flag) break;
	}
	return a;
}
int main(){
	//genp();
	int t,n,j;
	cin >> t >> n >> j;
	int cnt=0;
	srand(time(0));
	cout << "Case #1:" << endl;
	while (true){
		int i=rand()%(1<<(n-2));
		int x=(1<<(n-1))+(i<<1)+1;
		//cout << x << " " << binary(x) << endl; 
		vector<long long> a=check(x,n);
		if (a.size()<10-2+1) continue;
		cout << binary(x);
		for (int k=0;k<a.size();k++)
			cout << " " << a[k];
		cout << endl;
		cnt++;
		if (cnt>=j) break;
	}
	return 0;
}

