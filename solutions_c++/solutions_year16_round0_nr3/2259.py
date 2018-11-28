#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

class Factor {
public:
	Factor(int randLoops = 20, int randSeed = 0):randLoops(randLoops) {
		srand(randSeed);
	}
	
	bool isPrime(long long n) {
		return Miller_Rabin(n);
	}
	
	long long getOneFactor(long long n) {
		if(n < 2) return n;
		if(isPrime(n)) {
	        return n;
	    }
	    long long p=n;
	    while(p>=n)p=Pollard_rho(p,rand()%(n-1)+1);
	    return getOneFactor(p);
	}
	
	vector<long long> getAllFactors(long long n) {
		if(n < 2) return {n};
		vector<long long> ans;
		findfac(n, ans);
		return ans;
	}
	
private:
	int randLoops;//����㷨�ж�������SԽ���д����ԽС

	//���� (a*b)%c.   a,b����long long������ֱ����˿��������
	//  a,b,c <2^63
	long long mult_mod(long long a,long long b,long long c)
	{
	    a%=c;b%=c;
	    long long ret=0;
	    while(b)
	    {
	        if(b&1){ret+=a;ret%=c;}
	        a<<=1;
	        if(a>=c)a%=c;
	        b>>=1;
	    }
	    return ret;
	}
	
	//����  x^n %c
	long long pow_mod(long long x,long long n,long long mod)//x^n%c
	{
	    if(n==1)return x%mod;
	    x%=mod;
	    long long tmp=x;
	    long long ret=1;
	    while(n)
	    {
	        if(n&1) ret=mult_mod(ret,tmp,mod);
	        tmp=mult_mod(tmp,tmp,mod);
	        n>>=1;
	    }
	    return ret;
	}
	
	//��aΪ��,n-1=x*2^t      a^(n-1)=1(mod n)  ��֤n�ǲ��Ǻ���
	//һ���Ǻ�������true,��һ������false
	bool check(long long a,long long n,long long x,long long t)
	{
	    long long ret=pow_mod(a,x,n);
	    long long last=ret;
	    for(int i=1;i<=t;i++)
	    {
	        ret=mult_mod(ret,ret,n);
	        if(ret==1&&last!=1&&last!=n-1) return true;//����
	        last=ret;
	    }
	    if(ret!=1) return true;
	    return false;
	}
	
	// Miller_Rabin()�㷨�����ж�
	//����������true.(������α�����������ʼ�С)
	//��������false;
	
	bool Miller_Rabin(long long n)
	{
	    if(n<2)return false;
	    if(n==2)return true;
	    if((n&1)==0) return false;//ż��
	    long long x=n-1;
	    long long t=0;
	    while((x&1)==0){x>>=1;t++;}
	    for(int i=0;i<randLoops;i++)
	    {
	        long long a=rand()%(n-1)+1;//rand()��Ҫstdlib.hͷ�ļ�
	        if(check(a,n,x,t))
	            return false;//����
	    }
	    return true;
	}
	
	
	//************************************************
	//pollard_rho �㷨�����������ֽ�
	//************************************************
	long long factor[100];//�������ֽ������շ���ʱ������ģ�
	int tol;//�������ĸ���������С���0��ʼ
	
	long long gcd(long long a,long long b)
	{
	    if(a==0)return 1;//???????
	    if(a<0) return gcd(-a,b);
	    while(b)
	    {
	        long long t=a%b;
	        a=b;
	        b=t;
	    }
	    return a;
	}
	
	long long Pollard_rho(long long x,long long c)
	{
	    long long i=1,k=2;
	    long long x0=rand()%x;
	    long long y=x0;
	    while(1)
	    {
	        i++;
	        x0=(mult_mod(x0,x0,x)+c)%x;
	        long long d=gcd(y-x0,x);
	        if(d!=1&&d!=x) return d;
	        if(y==x0) return x;
	        if(i==k){y=x0;k+=k;}
	    }
	}
	//��n���������ӷֽ�
	void findfac(long long n, vector<long long>& factors)
	{
	    if(isPrime(n))//����
	    {
	        factors.push_back(n);
	        return;
	    }
	    long long p=n;
	    while(p>=n) p=Pollard_rho(p,rand()%(n-1)+1);
	    findfac(p, factors);
	    findfac(n/p, factors);
	}
};

void testFactor(void) {
	Factor f;
	long long x;
	while(cin >> x) {
		if(f.isPrime(x)) cout << x << " is prime." << endl;
		else cout << x << " is not prime." << endl;
		cout << f.getOneFactor(x) << " is a prime factor of " << x << endl;
		auto ans = f.getAllFactors(x);
		for(auto factor : ans) cout << factor << " ";
		cout << endl << endl;
	}
}

Factor f;

long long cal(unsigned int item, long long base) {
	long long bit = 1;
	long long ans = 0;
	while(item) {
		if(item & 1) {
			ans += bit;
		}
		bit *= base;
		item >>= 1;
	}
	return ans;
}

bool check(unsigned int item, vector<long long>& numbers) {
	for(int i=0; i<=8; i++) {
		numbers[i] = cal(item, i+2);
	}
	for(auto x : numbers) {
		if(f.isPrime(x)) {
			return false;	
		}
	}
	return true;
}

string binaryString(unsigned int item) {
	if(item == 0) {
		return "0";
	}
	string ans = "";
	for(item; item>0; item = item>>1){
		if(item & 1) {
			ans = "1"+ans;
		} else {
			ans = "0"+ans;
		}
	}
	return ans;
}

void outputAns(unsigned int item, vector<long long>& numbers) {
	for(int i=0; i<numbers.size(); i++) {
		numbers[i] = f.getOneFactor(numbers[i]);
	}
	cout << binaryString(item);
	for(auto x:numbers) {
		cout << " " << x;
	}
	cout << endl;
}

int main() {
	freopen("A-small0.in", "r", stdin);
	freopen("A-small0.out", "w", stdout);
	//testFactor();
	//cout << binaryString(6) << endl;
	//cout << binaryString(0) << endl;
	int t;
	cin >> t;
	for(int cas = 1; cas <=t ; cas++) {
		int n, j;
		cin >> n >> j;
		unsigned int lbit = 1 << (n-2);
		cout << "Case #" << cas << " :" << endl;
		vector<long long> numbers(9,0);
		int count = 0;
		for(unsigned int x=0; x<lbit; x++) {
			unsigned int item = (lbit<<1) | (x<<1) | 1;

			if(check(item, numbers)) {
				outputAns(item, numbers);
				count++;
			}
			if(count >= j) break;
		}
	}
	return 0;
}
