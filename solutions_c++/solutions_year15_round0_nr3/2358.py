#include <iostream>
using namespace std;


struct RES
{
	int r;
	int sign;
	RES(char a)
	{
		sign = 1;
		if(a == 'i') r = 2;
		else if(a == 'j') r = 3;
		else if(a == 'k') r = 4;
		else if(a == '1') r = 1;
	}
	RES()
	{
	sign = r = 1;
	}
	RES(int a, int b): r(a), sign(b) {}
	bool operator == (const RES& b)
	{
		return (r == b.r && sign == b.sign);
	}
};

RES res[4][4] = {
	{{1,1}, {2,1}, {3,1}, {4,1}},
	{{2,1}, {1,-1}, {4,1}, {3,-1}},
	{{3,1}, {4,-1}, {1,-1}, {2,1}},
	{{4,1}, {3,1}, {2,-1}, {1,-1}}
};
 
 void mult(RES& a, const RES& b)
 {
	RES c = res[a.r-1][b.r-1];
	c.sign *= (a.sign * b.sign);
	a = c;
 }
 
int main()
{
	int i,j,k,t;
	cin>>t;
	for(i=1;i<=t;i++)
	{
	bool ans = false;
	typedef long long int ll;
	int l;
	ll x;
	cin>>l>>x;
	cin.ignore();
	string s;
	cin>>s; //l char
	
	int c = 0;
	k=0;
	RES a('1');
	RES ri('i');
	for(j=0;j<4*l;j++)
	{
		RES b(s[k]);
		mult(a,b);
		k = (k+1)%l;
		c++;
		if(a == ri)
		{
			ans = true; break;
		}
	
	}
	
	if(ans)
	{
		ans = false;
	RES a('1');
	RES rj('j');
	for(j=0;j<4*l;j++)
	{
		RES b(s[k]);
		mult(a,b);
		k = (k+1)%l;
		c++;
		if(a == rj)
		{
			ans = true; break;
		}	
	}
	}
	
	if(ans)
	{
		ans = false;
	RES a('1');
	RES rk('k');
	for(j=0;j<4*l;j++)
	{
		RES b(s[k]);
		mult(a,b);
		k = (k+1)%l;
		c++;
		if(a == rk)
		{
			ans = true; break;
		}	
	}
	}
	
	if(ans)
	do
	{
		if((ll)c == l*x)
			break;
		ans = false;
		if((ll)c > l*x)
			break;
		//check that mult of whole is -1
		int tt = x%4;
		RES a('1');
	k=0;
	for(j=0;j<l*tt;j++)
	{
		RES b(s[k]);
		mult(a,b);
		k = (k+1)%l;
		}
		if(a.sign == -1 && a.r == 1)
			ans = true;
		
		
		
	}while(0);
	
	cout<<"Case #"<<i<<": ";
	cout<<(ans ? "YES" : "NO");
	cout<<'\n';
	}
	return 0;
}
