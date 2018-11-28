#include<cstdio>
#include<string>
#include<cmath>
using namespace std;


#define ll long long int

string convertInt1( long long int number )
{
    if (number == 0)
        return "0";
    string temp="";
    string returnvalue="";
    while (number>0)
    {
        temp+=number%10+48;
        number/=10;
    }
    for (int i=0;i<temp.length();i++)
        returnvalue+=temp[temp.length()-i-1];
    return returnvalue;
}

bool ispal(long long int n)
{
	string s=convertInt1(n);
	int k=s.size();
	for(int i=0;i<k/2;i++)
	{
		if(s[i]!=s[k-1-i])
		return false;
	}
	return true;
}
		
int main()
{
	int t;scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		ll  a,b,count=0;
		
		scanf("%lld%lld",&a,&b);
		
		for(ll i=sqrt(a);i<=sqrt(b);i++)
		{
			if(ispal(i))
			{
				if(ispal(i*i) && (i*i)<=b && (i*i)>=a)
				count++;
			}
		}
		
		printf("Case #%d: %lld\n",k,count);
	}
}
				
