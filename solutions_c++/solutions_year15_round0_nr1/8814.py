#include<bits/stdc++.h>
using namespace std;
int main()
{
		freopen("abc.txt","r",stdin);
		freopen("op.txt","w",stdout);
	int t,n=1;
	cin>>t;
	while(t--)
	{
	
	int s,c=0,aud=0;
	cin>>s;
	string a;
	cin>>a;
	for(int i=1;i<a.length();i++)
	{
		aud=aud+int(a[i-1])-48;
		if(aud>=i)
		c=c+0;
		else
		{
		c=c+(i-aud);
		aud=aud+(i-aud);	
	}
	}
	cout<<"Case #"<<n<<": "<<c<<endl;
	n++;
	}
	fclose(stdout);
	return 0;
}


