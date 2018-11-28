#include <iostream>
#include <list>
#include <string>

using namespace std;

long long CheckPrime(long long num)
{
	if(num<2) return 0;
	for(long long i=2;i*i<=num;i++) {
		if(num%i==0)
			return i;
	}
	return 1;
}

int main()
{
	long long T, N, J, counter=0;
	list<long long> result[100][100];
	cin>>T;
	for(int i=0;i<T;i++) {
		long long range, max_range=1, t;
		cin>>N>>J;
		max_range=1LL<<(N-2);
		t=1LL<<(N-1);
		for(range=0;range<max_range;range++) {
			long long pr[9]={}, j;
			for(j=2;j<=10;j++) {
				for(long long temp=t+(range<<1LL)+1LL, k=1LL;temp;temp>>=1LL,k*=j) {
					pr[j-2]+=(temp&1)*k;
				}
				if((pr[j-2]=CheckPrime(pr[j-2LL]))==1LL)
					break;
			}
			if(j==11) {
				result[i][counter].push_back(t+(range<<1LL)+1LL);
				for(int k=0;k<9;k++)
					result[i][counter].push_back(pr[k]);
				if(++counter==J)
					break;
			}
		}
	}
	for(int i=0;i<T;i++) {
		cout<<"Case #"<<i+1<<":"<<endl;
		for(int j=0;result[i][j].size()!=0;j++) {
			list<long long>::iterator it=result[i][j].begin();
			string r;
			for(;*it;*it>>=1) {
				r+='0'+(*it&1);
			}
			reverse(r.begin(),r.end());
			cout<<r<<' ';
			for(it++;it!=result[i][j].end();it++) {
				cout<<*it<<' ';
			}
			cout<<endl;
		}
	}
	system("PAUSE");
    return 0;
}