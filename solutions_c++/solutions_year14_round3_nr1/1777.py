# include <iostream>
# include <stdio.h>
# include <math.h>
using namespace std;
float f(int p,int q)
{
	int temp = log (q)/log (2);
	float flag = log (q)/log (2);
	if (temp == flag)
	{float r = p/q;
	if (r >= 1)
		return 0;
	else
		return (1+f(p,q/2));
	}
	else
	return 9999;
}
int main()
{
	int t,i;
	cin >> t;
	int a[t];
	for (i=1;i<=t;i++)
	{
	int p,q;
	scanf("%d/%d",&p,&q);
	float r = f(p,q);
	a[i] = r;
	}
	for (i=1;i<=t;i++)
	{
		if (a[i] != 9999)
		cout << "Case #" << i << ": " << a[i] << endl;	
		else
		cout << "Case #" << i << ": impossible" << endl;	
	}
	return 0;
}
