#include<iostream>
using namespace std;
long long int ans = 1 , k ,c, s,printa;
long long int po(long long int x,long long int y)
{
	long long int temp;
	if(y == 0)
	return 1;
	temp = po(x,y/2);
	if(y%2 == 0)
	return temp*temp;
	else
	return x*temp*temp;
}
int main()
{
	int t   ,coun =0 ;
	cin>>t;
	while(t--)
	{
		coun++;
		cin>>k>>c>>s;
		//cout<<k<<c;
		ans = po(k ,c-1);
		cout<<"Case #"<<coun<<": ";
		printa = 1;
		for(int i=1;i<=s;i++)
		{
			cout<<printa<<" ";
			printa = printa + ans;
		}
		cout<<endl;
	}
}
