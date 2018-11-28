/* sourabh1024  */
#include<bits/stdc++.h>

#define si(n)		(scanf("%d",&n))
#define pi(n)		(printf("%d",n))
#define sl(n)		(scanf("%I64d",&n))
#define pl(n)		(printf("%I64d",n))

#define lli long long int
#define ii pair<int,int>
#define vii pair< ii ,int>
#define pb(a) push_back(a)
using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	lli t,x,y;
	in>>t;
	lli ca =1;
	while(t--)
	{
		in>>x;
		string ip;
		in>>ip;
		lli ans =0, curr=0;
		for(int i=0;i<=x;i++)
		{
			if(ip[i]-'0' >0)
			{
				if(curr < i)
				{
					ans+=(i-curr);
					curr+=(i-curr);
				}
				
				curr+=(ip[i]-'0');
			}
		}
		out<<"Case #"<<ca<<": "<<ans<<endl;
		ca++;
	}
	in.close();
	out.close();
	return 0;
}

