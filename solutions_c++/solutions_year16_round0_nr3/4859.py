#include <bits/stdc++.h>
using namespace std;
typedef vector<char> vc;

int main()
{
	freopen("in.txt","r",stdin);
	//freopen("asd.txt","w",stdout);
	long long a;
	cin>>a;
	long long b,c;
	long long lol,lol2;
	for(long long iex=1;iex<=a;iex++)
	{
		cout<<"Case #"<<iex<<": "<<endl;
		long long cont=0;
		cin>>b>>c;
		bitset<64> beats;
		lol=pow(2,b-1)+1;
		lol2=pow(2,b);
		beats=lol2;
		while(lol<lol2)
		{
			beats=lol;
			
			for(long long i=2;i<=10;i++)
			{
				long long resu=0;
				for(long long j=0;j<=16;j++)
				{
					resu+=pow(i,abs(j))*beats[j];
				}
				bool aux=0;
				for(long long j=2;j<sqrt(resu);j++)
				{
					if(resu%j==0)
					{
						aux=1;
						break;
					}
				}
				if(aux==0)	
					break;
				
				if(i==10 and cont!=c)
				{
					cont++;
					for(long long asd=b-1;asd>=0;asd--)
						cout<<beats[asd];
					cout<<" ";
					//cout<<beats<<endl;
					for(long long ii=2;ii<=10;ii++)
					{
						long long lola=0;
						for(long long jj=0;jj<=16;jj++)
						{
							lola+=pow(ii,abs(jj))*beats[jj];
						}
						//cout<<lola<<" ";
						for(long long jj=2;jj<sqrt(lola);jj++)
						{
							if(lola%jj==0)
							{
								cout<<jj<<" ";
								break;
							}
						}
					}
					cout<<endl;
				}
				else if(cont==c)break;
			}
			lol+=2;
		}
		//cout<<beats<<endl;
	}
}