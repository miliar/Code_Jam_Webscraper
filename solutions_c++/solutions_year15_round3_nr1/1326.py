#include<bits/stdc++.h>


#define ffi first
#define ssi second
#define lli long long int
#define mod 1000000007


using namespace std;


int gcd(int a ,int b)
{
	if(a%b==0)
	return a;
	else
	return gcd(b,a%b);
}


lli read_int(){
	char r;
	bool start=false,neg=false;
	long long int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}

int main()

{
	freopen("abc.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	lli t, rw, cl, wd;
	cin >> t;
	for (int cse = 0; cse<t; cse++)
	{
		   lli res = 0;
           rw=read_int();
           cl=read_int();
           wd=read_int();
		res = cl / wd *rw;
		res += wd - 1;
		if (cl%wd != 0)
			res++;
		cout << "Case #" << cse + 1 << ": " << res << endl;
	}
	return 0;
}
