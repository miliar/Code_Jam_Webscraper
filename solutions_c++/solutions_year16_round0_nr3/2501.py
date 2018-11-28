#include <iostream>
#include <string>
using namespace std;

long long w[11][20];
long long now[11],divs[11];
long long n,J,T,maxb,nowans;
string s;

long long d(int k) {
	long long p=now[k];
	for (long long i=2; i*i<=p; i++)
		if (p%i==0)
			return i;
	return 0;
}

bool check() {
	//cout<<endl;
	for (int i=2; i<=10; i++) {
		long long ansd=d(i);
		//cout<<i<<"  "<<ansd;
		if (ansd) {
			divs[i]=ansd;
		} else {
			return false;
		}
	}
	return true;
}

int main() {
	//freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
	ios::sync_with_stdio(false);
	cin>>T;
	//T=1;
	for (int ii=1; ii<=T; ii++) {
		cout<<"Case #"<<ii<<":\n";
		cin>>n>>J;
		//n=16;J=50;
		for (int i=2; i<=10; i++) {
			w[i][1]=1;
			for (int j=2; j<=n; j++)
				w[i][j]=w[i][j-1]*i;
		}
		maxb=w[2][n-1]-1;
		nowans=0;
		for (int i=0; nowans<J && i<=maxb; i++) {
			s="1";
			for (int j=2; j<=10; j++) now[j]=w[j][n]+1;
			int k=i,bit=2;
			while (k>0) {
				if (k%2==1)
					for (int j=2; j<=10; j++) now[j]+=w[j][bit];
				s=char(k%2+'0')+s;
				k/=2;
				bit++;
			}
			
			if (check()) {
				for (int j=bit; j<n; j++) s="0"+s;
				s="1"+s;
				cout<<s<<" ";
				for (int j=2; j<=10; j++) cout<<divs[j]<<" ";
				cout<<endl;
				nowans++;
			}
			/*
			for (int j=bit; j<n; j++) s="0"+s;
			s="1"+s;
			cout<<s<<" ";
			for (int j=2; j<=10; j++) cout<<now[j]<<" ";
			cout<<endl;
			*/
		}
	}
}
