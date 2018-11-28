#include<bits/stdc++.h>
using namespace std;

long long int pow( int base, int exp){
	long long int x = 1;
	long long int y = base;
	while (exp > 0)
	{
		if (exp % 2 == 1)
		x = (x * y) ;
		y = (y * y) ;
		exp = exp / 2;
	}
	return x ;
}
long long int convert(long long int no,  int base, int leng)
{   int rem=0;
	long long int res=0;
	long long int cnt=0;
	while(no!=0){
		// cout<<no<<" "<<leng<<" "<<(no) % 10<<endl;
		if( no% 10==1){
			res+=pow(base,cnt);
		}
		no=no/10;
		//cout<<no<<" ";
		leng--;
		cnt++;
	}
	return res;
}
bool checkvalid(long long int no,long long int len){

	if(no%10!=1)
	return false;
	return true;
}

long long  modulo(long long int base, long long int exponent, long long int mod)
{
	long long int x = 1;
	long long int y = base;
	while (exponent > 0)
	{
		if (exponent % 2 == 1)
		x = (x * y) % mod;
		y = (y * y) % mod;
		exponent = exponent / 2;
	}
	return x % mod;
}
bool Fermat(long long int p, int iterations)
{
	if (p == 1)
	{
		return false;
	}
	for (int i = 0; i < iterations; i++)
	{
		long long int a = rand() % (p - 1) + 1;
		if (modulo(a, p - 1, p) != 1)
		{
			return false;
		}
	}
	return true;
}

long long int decimal_binary(long long int n)
{
    long long int rem, i=1, binary=0;
    while (n!=0)
    {
        rem=n%2;
        n/=2;
        binary+=rem*i;
        i*=10;
    }
    return binary;
}


int main()
{
	int t;
     freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout)  ;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
	long long int n,k;

		cin>>n>>k;
		long long int  total=n-2;
		cout<<"Case #"<<tt<<": \n";

		long long int start=1<<n-1;
		{
			for(int i=start+start/101;i<start*2;i++){

			long long int temp=decimal_binary(i);
	    //	cout<<temp<<" ";

//				temp=(temp*pow(10,total-2));
//				temp+=1;//perfect no

				if(checkvalid(temp,n)){

				int cnt=0;
				for(int i=2;i<=10;i++)
				{int iteration=50;
					long long int con= convert(temp,i,n);
						//cout<<con<<endl;
					//count of total non prime no in base 2-10

					if(Fermat(con,iteration)==false)
					{
						cnt++;
					}  // not prime
				}
				if(cnt==9){ // all are right and ready to be served
					k--;
					cout<<temp<<" ";
					for(int i=2;i<=10;i++)
					{
						long long int res=convert(temp,i,n);
						for(int jj=2;jj*jj<=res;jj++)
						{
							if(res%jj==0)
							{
								cout<<jj<<" ";
								goto here1;
							}

						}
						here1:;
					}
					cout<<endl;
					if(k==0){
						goto outside;
					}
				}


			}
			}
			outside: ;
		}
	}
}



