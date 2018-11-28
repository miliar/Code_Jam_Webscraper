#include <iostream>

using namespace std;

bool tab[10];

int main()
{
	int T;
	cin>>T;
	for(int ti = 1; ti <= T; ti++)
	{
		int N;
		cin>>N;
		
		if(N == 0)
		{
			cout<<"Case #"<<ti<<": INSOMNIA"<<endl;
			continue;
		}
		
		int w = 1;
		int counter = 0;
		while(true)
		{
			int n = N * w;
			while(n != 0)
			{
				int d = n % 10;
				n /=10;
				
				if(tab[d]==false){ counter++; tab[d] = true;}
			}
			if(counter==10)break;
			w++;
		}
		cout<<"Case #"<<ti<<": "<<N*w<<endl;
		
		for(int i = 0; i <=9;i++)tab[i]=false;
	}
	
}