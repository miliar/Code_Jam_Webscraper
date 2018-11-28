#include <iostream>

using namespace std;

int main()
{
	remove("output.txt");
	freopen("D-small-attempt6.in","r", stdin);
	freopen("output.txt","w", stdout);
	
	int t;
	cin>>t;
	
	int x, r, c;

	for(int i = 0; i < t; ++i)
	{
	cin>>x>>r>>c;
	if (x == 1)
		{
			cout<<"Case #"<<(i + 1)<<": "<<"GABRIEL"<<"\n";
			continue;
		}
	
	if (x == 2)
		{
			if(((r * c) % 2) == 0)
						{
							cout<<"Case #"<<(i + 1)<<": "<<"GABRIEL"<<"\n";
							continue;
						}
						
			else if(((r * c) % 2) == 1)
						{
							cout<<"Case #"<<(i + 1)<<": "<<"RICHARD"<<"\n";
							continue;
						}
						
		}
	else
	{
		if ((r == 1) || (c == 1))
				{
					cout<<"Case #"<<(i + 1)<<": "<<"RICHARD"<<"\n";
					continue;
				}
				
	if ((r * c) % x != 0)
			{
				cout<<"Case #"<<(i + 1)<<": "<<"RICHARD"<<"\n";
				continue;
			}
	else
		{
			
			switch(x)
			{
				
				case 3:
						cout<<"Case #"<<(i + 1)<<": "<<"GABRIEL"<<"\n";
						break;				
				case 4:
						if(((r == 2) && (c == 2)) || ((r == 4) && (c == 2)) || ((r == 2) && (c == 4)))
							cout<<"Case #"<<(i + 1)<<": "<<"RICHARD"<<"\n";
						else
							cout<<"Case #"<<(i + 1)<<": "<<"GABRIEL"<<"\n";
						break;
			}
		}
	}
	
	}
	
	fclose(stdout);
	fclose(stdin);
	
}
