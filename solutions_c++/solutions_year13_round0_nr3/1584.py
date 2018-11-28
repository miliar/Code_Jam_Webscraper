#include<iostream>
#include<string>
using namespace std;

bool isPalin(long long n){

	char str[1000];
	sprintf(str,"%lld",n);
	int l=strlen(str);
	for(int i=0;i<l/2;i++)
		if(str[i]!=str[l-i-1]) return false;
	return true;
}

void process1(){
	long long t;
	cout<<"{";
	for(int  i=1;i<10000001;i++){
		t=i;
		t=t*t;
		
		if(isPalin(i)&& isPalin(t)){
			cout<<i<<","<<endl;
		}
		
	}
	cout<<"}";
}
int ar[]={1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002};
int howMany(int n){

	int cnt=0;
	for(int i=0;i<39;i++)
	if(ar[i]<=n) cnt++;

	return cnt;
}
int main(){
	freopen("C-large-1.in","rt",stdin);
	freopen("C-large-1.out","wt",stdout);
	//freopen("save.out","wt",stdout);
	long long A,B;
	int T,cas=1;
	int a,b;
	cin>>T;
	while(T--){
	
		cin>>A>>B;
		a=(int)sqrt((long double)(A-1));
		b=(int)sqrt((long double)B);
		printf("Case #%d: %d\n",cas++,howMany(b)-howMany(a));
	}

	
	

	return 0;
}