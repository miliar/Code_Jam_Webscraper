//small
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

struct ee {
	long long volume, temp;
	bool operator<(const ee &b) const {return temp<b.temp;}
};

long long read(){
	char s[110];
	scanf("%s",s);
	long long k,temp=0;
	for (k=0;k<strlen(s);k++)
	if (isdigit(s[k]))
	temp=temp*10+s[k]-'0';
	return temp;
}

int main() {
	int T,t,n,i,j;
	ee final,a[110];
	cin>>T;
	for (t=1;t<=T;t++){
		printf("Case #%d: ",t);
		cin>>n;
		final.volume=read();
		final.temp=read();
		for (i=0;i<n;i++) {
			a[i].volume=read();
			a[i].temp=read();
		}
		sort(a,a+n);
		for (i=1;i<n;)
		if (a[i].temp==a[i-1].temp) {
			a[i-1].volume+=a[i].volume;
			n--;
			for (j=i;j<n;j++)
			a[j]=a[j+1];
		}
		else i++;
		if (n==1) {
			if (a[0].temp==final.temp)
			cout<<setprecision(8)<<fixed<<1.0*final.volume/a[0].volume<<endl;
			else printf("IMPOSSIBLE\n");
		}
		else if (n==2) {
			if ((a[0].temp>final.temp && a[1].temp>final.temp) || (a[0].temp<final.temp && a[1].temp<final.temp))
			printf("IMPOSSIBLE\n");
			else if (a[0].temp==final.temp)
			cout<<setprecision(8)<<fixed<<1.0*final.volume/a[0].volume<<endl;
			else if (a[1].temp==final.temp)
			cout<<setprecision(8)<<fixed<<1.0*final.volume/a[1].volume<<endl;
			else {
				long double t1=1.0,t0=1.0;
				t1=t1*final.volume*(final.temp-a[0].temp)/a[1].volume/(a[1].temp-a[0].temp);
				t0=(t0*final.volume-a[1].volume*t1)/a[0].volume;
				t0=max((long double)0.0,max(t0,t1));
				cout<<setprecision(8)<<fixed<<t0<<endl;;
			}
		}
		else {
			printf("\n");
		}
	}
    return 0;
}
