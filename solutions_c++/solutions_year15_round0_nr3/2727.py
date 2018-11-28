#include<iostream>
#include<algorithm>
#include<string>

using namespace std;
int main()
{
	remove("output.txt");
	freopen("C-small-attempt0.in","r", stdin);
	freopen("output.txt","w", stdout);
	int t;
	cin>>t;
	
	string inp, a;
	int x, l;
	
	int eval(string);
	int check(string, int);
	int checki, checkj, checkk = 0;
	for(int i = 0; i < t; ++i)
	{
		cin>>x>>l;
		cin>>inp;
		a = "";
		
		for(int j = 0; j < l; ++j)
			a += inp;
		
		if (eval(a) != -1)
			cout<<"Case #"<<(i + 1)<<": NO"<<"\n";
		else
		{	
			checki = check(a, 2);
			if(checki >= 0)
			{
				a = a.substr(checki + 1);
				checkj = check(a, 3);
				if(checkj >= 0)
					{
						a = a.substr(checkj + 1);
						checkk = check(a, 4);
						
						if(checkk >= 0)
							cout<<"Case #"<<(i + 1)<<": YES"<<"\n";
						else
							cout<<"Case #"<<(i + 1)<<": NO"<<"\n";
					}
				else
					cout<<"Case #"<<(i + 1)<<": NO"<<"\n";
			}
			else cout<<"Case #"<<(i + 1)<<": NO"<<"\n";
			
		}
	}
	fclose(stdout);
	fclose(stdin);
}
int conv(char a)
{
	switch(a)
		{
		case 'i': return 2;
		case 'j': return 3;
		case 'k': return 4;
		}
}
int f(int a, int b)
{
	switch (a)
	{
			case 2:
			{
				switch (b)
				{
					
					case 2:
						return -1;
					case 3:
						return 4;
					case 4:
						return -3;
				}
				
			}
			case 3:
			{
				switch (b)
				{
				
					case 2:
						return -4;
					case 3:
						return -1;
					case 4: 
						return 2;
				}
				
			}
			case 4:
			{
				switch (b)
				{
					
					case 2:
						return 3;
					case 3:
						return -2;
					case 4: 
						return -1;
				}
				
			}
			case -2:
			{
				switch (b)
				{
					case 2:
						return 1;
					case 3:
						return -4;
					case 4:
						return 3;
				}
				
			}
			case -3:
			{
				switch (b)
				{
					case 2:
						return 4;
					case 3:
						return 1;
					case 4: 
						return -2;
				}
			}
			case -4:
			{
				switch (b)
				{
				
					case 2:
						return -3;
					case 3:
						return 2;
					case 4: 
						return 1;
				}
			}
			
			case -1:
					return (a*b);
			
			case 1:
					return (a*b);
	}
}
int eval(string a)
{
	int val;
	
	val = conv(a[0]);
	
	for(int i = 1; i < a.length(); ++i)
		val = f(val, conv(a[i]));
	
	return val;
}
int check(string a, int j)
{
	int val;
	
	val = conv(a[0]);
	if (val == j)
				return 0;
	
	for(int i = 1; i < a.length(); ++i)
		{
			val = f(val, conv(a[i]));
			if (val == j)
				return i;
		}
		
	return -1;
}
