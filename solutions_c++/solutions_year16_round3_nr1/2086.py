#include <bits/stdc++.h>
using namespace std;
typedef pair<int,char> ii;
int main()
{
	freopen("A-large (2).in","r",stdin);
	freopen("lol.txt","w",stdout);
	int a;
	cin>>a;
	int lol=0;
	while(a--)
	{
		lol++;
		int b;
		cin>>b;
		ii ar[b];
		int x;
		for(int i=0;i<b;i++)
		{
			cin>>x;
			ar[i]=ii(x,'A'+i);
		}
		sort(ar,ar+b);
		/*
		for(int i=0;i<b;i++)
		{
			cout<<ar[i].first<<" "<<ar[i].second<<endl;
		}*/
			int cont=0;
			for(int i=0;i<b;i++)
			{
				cont+=ar[i].first;
			}
			cout<<"Case #"<<lol<<": ";
			while(cont!=0)
			{
				
				if(b-2>=0 and ar[b-1].first==ar[b-2].first and cont>=2 )
				{
					ar[b-1].first--;
					ar[b-2].first--;
					for(int i=0;i<b;i++)
					{
						if(ar[i].first*2>cont-2)
						{
							ar[b-1].first++;
							ar[b-2].first++;
							goto gnu;
						}
					}

					cout<<ar[b-1].second<<ar[b-2].second;
				}
				else
				{
					gnu:;
					ar[b-1].first--;
					cout<<ar[b-1].second;
				}
				if(1==0)
				{
					gnu2:;
					ar[b-1].first-=2;
					cout<<ar[b-1].second;
				}
				sort(ar,ar+b);
				cont=0;
				for(int i=0;i<b;i++)
				{
					cont+=ar[i].first;
				}
				if(cont==0)cout<<endl;
				else cout<<" "; 
				//cout<<cont<<endl;

			}

		}
	}