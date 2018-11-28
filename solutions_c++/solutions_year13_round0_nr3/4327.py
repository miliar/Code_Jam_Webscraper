#include <iostream>
#include <cstdio>
using namespace std;
long long V[80],VS;
bool f (long long );
void main()
{

freopen("2.in","r",stdin);
freopen("output.txt","w",stdout);

	long long a , b;
	long long t = 0;
	long long i;
	long long j = 0;
	long long qanak;
	cin >> qanak;
	for(j=1;j<10000009;j++)	if(f(j) && f(j*j)) V[VS++]=j*j;
	j=0;
	while(j < qanak){
		t=0;
		cin >> a >> b;	
		for(i = 0; i <VS; i++) if(V[i]>=a && V[i]<=b) t++;
			cout <<"Case #"<<j+1<<": "<<t<<endl;
			j++;
}
	

}

bool f(long long x)
{
	long long a = 0;
	long long k = x;
	while ( k !=0 )
		{
			a = a * 10 + k % 10;
			k = k / 10;
		 }
	if(x == a)
		return true;
	return false;
}