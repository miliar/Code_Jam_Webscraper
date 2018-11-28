#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<cmath>
#include<string>
#define M 10000007;

#define input(a) scanf("%d",&a);
#define print(a) printf("%d",a);

using namespace std;

int checkpal(int n)
{
unsigned long long int num=n,digit=0;
unsigned long long int rev=0;
while(n!=0)
    {
        digit=n%10;
        rev=(rev*10)+digit;
        n=n/10;
    }
if(num==rev)
return true;
else
return false;
}

int main()
{
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);

unsigned long long int t=0;
unsigned long long int q=0;
cin>>t;
while(q++<t)
{   unsigned long long int ans=0;
	bool che=0;
	unsigned long long int a,b;
	cin>>a>>b;
unsigned long long int i=0;
for(i=a;i<=b;i++)
{
		//cout<<i<<endl;


	if((sqrt(i)*sqrt(i))==i)
{
		if((checkpal(sqrt(i))==true)&&(checkpal(i)==true))
		ans++;

		
}

}
	
cout<<"Case #"<<q<<":"<<" "<<ans<<endl;

}
}
