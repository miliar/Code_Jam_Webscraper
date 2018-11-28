#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int mark(int num, int *flag)
{
	int r,i;
	
	while(num != 0)
	{
		r = num%10;
		flag[r] = 1;
		num /= 10;
	}
	
	return 0;
}

bool check(int *flag)
{
	int i;
	for(i=0;i<10;i++)
	{
		if(flag[i] == 0) return false;
	}
	return true;
}

int main()
{
	int t, i;
	
	cin >> t;	
	for (i=0;i<t;i++)
	{
		int n;
		cin >> n;
		if (n==0)
		{
			cout << "Case #"<< i+1 <<": INSOMNIA\n";
			continue;
		}
		int flag[10],j = 1,num;
		memset(flag,0,sizeof(flag));
		while( !check(&flag[0]) )
		{
			num = n * j;
			j++;
			mark(num,&flag[0]);
		}
		cout << "Case #" << i+1 << ": " << num << endl;
	}
}
