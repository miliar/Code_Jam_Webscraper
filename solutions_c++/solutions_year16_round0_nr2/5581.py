#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		string pancake;
		cin >> pancake;
		bool isHappyside;
		int flip = 0;
		string checker1;
		string checker2;
		for(int c=0;c<pancake.size();c++)
		{
			checker2 = checker2+'-';
			checker1 = checker1+'+';
		}

		while(pancake != checker1 && pancake != checker2)
		{
			if(pancake[0] == '+')
				isHappyside = true;
			else
				isHappyside = false;
			for(int m=1; m<pancake.size(); m++)
			{
				
				if(pancake[m] == '+' && !isHappyside)
				{
					for(int y=0;y<=m-1;y++)
						pancake[y] = '+';
					flip++;
					break;
				}
				if(pancake[m] == '-' && isHappyside)
				{
					for(int y=0;y<=m-1;y++)
						pancake[y] = '-';
					flip++;
					break;
				}
			}
		}
		if(pancake == checker1)
					cout << "Case #" << i << ": " << flip << "\n";
		else
			cout << "Case #" << i << ": " << flip+1 << "\n";
	}

	return 0;
}