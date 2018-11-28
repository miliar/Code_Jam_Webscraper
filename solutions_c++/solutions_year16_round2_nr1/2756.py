#include<iostream>

using namespace std;
main()
{
	
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int test,T=1;
	cin>>test;
	while(T<=test)
	{
		int a[27],b[11];
		string s;
		cin>>s;
		int l=s.length(),i,j;
		for(i=0;i<26;++i)
		{
			a[i]=0;
		}
		for(i=0;i<10;++i)
		{
			b[i]=0;
		}
		for(i=0;i<l;++i)
		{
			a[s[i]-'A']++;
		}
		cout<<"Case #"<<T<<": ";
		j=a[25];  //Z
		b[0]=j;
		a[4]-=j;  //E
		a[14]-=j;//O
		j=a[22];//W
		b[2]=j;
		a[14]-=j;
		j=a[20];//U
		b[4]=j;
		a[5]-=j;//F
		a[14]-=j;
		j=a[6];//G
		b[6]=a[23];//X
		b[8]=j;
		a[4]-=j;
		a[7]-=j;//H
		j=a[5];
		b[5]=j;
		a[21]-=j;//V
		a[4]-=j;
		j=a[21];
		b[7]=j;
		a[4]-=j;a[4]-=j;
		j=a[7];
		b[3]=j;
		a[4]-=j;a[4]-=j;
		j=a[14];
		b[1]=j;
		a[4]-=j;
		b[9]=a[4];
		for(i=0;i<10;++i)
		{
			while(b[i])
			{
				cout<<i;
				b[i]--;
			}
		}
		
		
		cout<<endl;
		T++;
	}
}
