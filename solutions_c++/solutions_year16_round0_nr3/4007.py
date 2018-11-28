#include <bits/stdc++.h>

using namespace std;

typedef long long td;

td primeFactors(td n)
{
	if (n%2 == 0)
	{
		return 2;
	}

	for (td i = 3; i <= sqrt(n); i = i+2)
	{
		if (n%i == 0)
		{
			return i;
		}
	}
}

long long mul(long long a,long long b,long long c);
long long mod(long long a,long long b,long long c){
	long long x=1,y=a; 
	while(b > 0){
		if(b%2 == 1){
			x=mul(x,y,c);
		}
		y = mul(y,y,c); 
		b /= 2;
	}
	return x%c;
}

long long mul(long long a,long long b,long long c){
	long long x = 0,y=a%c;
	while(b > 0){
		if(b%2 == 1){
			x = (x+y)%c;
		}
		y = (y*2)%c;
		b /= 2;
	}
	return x%c;
}

int Miller(long long p,long long it){
	if(p<2){
		return 0;
	}
	if(p!=2 && p%2==0){
		return 0;
	}
	long long s=p-1;
	while(s%2==0){
		s/=2;
	}
	long long i;
	for(i=0;i<it;i++){
		long long a=rand()%(p-1)+1,tt=s;
		long long md=mod(a,tt,p);
		while(tt!=p-1 && md!=1 && md!=p-1){
			md=mul(md,md,p);
			tt *= 2;
		}
		if(md!=p-1 && tt%2==0){
			return 0;
		}
	}
	return 1;
}

void set_bits (int bit[], td n, td i)
{
	bit[0] = bit[15] = 1;

	int mask[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192};

	for (i = 0; i <= 13; i++) {
		if (n & mask[i]) {
			bit[i+1] = 1;
		}
	}

	return ;
}


int main()
{
	td i, t, num, re, j, n, k, l, cnt, flag;
	//		t = pow(10,16);
	//		cout<<t<<endl;

	int bit[16];

	cin>>t>>n>>re;

	cnt = 0;
	vector <td> v[50];
	vector <td> number[50];
	vector <td> tmp;
	for (i = 0; i < 8192; i++) {
		memset (bit, 0, sizeof(bit));
		set_bits(bit, i, 16);
		tmp.clear();
		flag = 0;
		for (j = 2; j <= 10; j++) {
			num = 0;
			for (k = 0; k < 16; k++) {
				l = pow(j,k);
				if(bit[k])
					num += l;
			}
/*			if (num < 0) {
				cout<<"negative\n";
			}
*/			if (Miller(num, 20)) {
				flag = 1;
				break;
			}
			else {
				tmp.push_back(num);
			}
		}
		if (flag == 0) {
			for (j = 15; j >= 0; j--) {
				v[cnt].push_back(bit[j]);
			}
//			cout<<"sizei " <<tmp.size()<<" "<<cnt<<endl;
			for (l = 0; l < tmp.size(); l++) {
/*				if (tmp[l] < 0) {
					cout<<"neagtive number going in\n";
				}
	*/			k = primeFactors(tmp[l]);
	//			if (k < 0) {
	//				cout<<"retrun\n";
	//			}
				number[cnt].push_back(k);
			}
			cnt++;
			if (cnt == re)
				break;
		}
	}
	//	cout<<cnt<<endl;	
	cout<<"Case #1:\n";
	for (i = 0; i < cnt; i++) {
		for (j = 0; j < v[i].size(); j++) {
			cout<<v[i][j];
		}
		cout<<" ";
	//	cout<<" "<<number[i].size()<<endl;
		for (j = 0; j < number[i].size(); j++) {
			cout<<number[i][j]<<" ";
		}
		cout<<endl;
	}

	return 0;
}
