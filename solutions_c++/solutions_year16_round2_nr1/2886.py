#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("q1_s.out","w",stdout);
	int t;
	cin>>t;
	int kk=0;
	while(t--)
	{
		kk++;
		string s;
		cin>>s;
		int l=s.length();
		int a[26];
		cout<<"Case #"<<kk<<": ";
		for(int i=0;i<26;i++)
		{
			a[i]=0;
		}
		for(int i=0;i<l;i++)
		{
			a[(int)s[i]-65]++;
		}
		int n[10];
		for(int i=0;i<10;i++)
		{
			n[i]=0;
		}
		int zero = a[25];
		n[0]=zero;
		a[4] = a[4]-zero;
		a[17] = a[17]-zero;
		a[14] = a[14]-zero;
		int two=a[22];
		n[2]=two;
		a[14] = a[14]-two;
		a[19] = a[19]-two;
		int four=a[20];
		n[4] = four;
		a[14] = a[14]-four;
		int six = a[23];
		n[6] = six;
		a[18] = a[18]-six;
		int eight = a[6];
		n[8] = eight;
		a[4] = a[4] - eight;
		a[19] = a[19]-eight;
		int one=a[14];
		n[1]=one;
		a[4]=a[4]-one;
		int three=a[19];
		n[3]=three;
		a[4]=a[4]-three;
		a[4]=a[4]-three;
		int seven=a[18];
		n[7]=seven;
		a[4]=a[4]-seven;
		a[4]=a[4]-seven;
		a[21]=a[21]-seven;
		int five=a[21];
		n[5]=five;
		a[4]=a[4]-five;
		int nine=a[4];
		n[9]=nine;
		for(int i=0;i<10;i++)
		{
			int k=n[i];
			while(k--)
			{
				cout<<i;
			}
		}
		cout<<endl;
	}
	return 0;
}
