# include <iostream>
# include <iomanip>
using namespace std;

int main()
{
	int num,j;
	cin >> num;
	double list[num];
	for (j=1;j<=num;j++)
	{
	double c,f,x;
	int i;	
	
	cin >> c >> f >> x;
	int k = 0;
	while ((x-c)/(2+f*k) > x/(2+f*(k+1)))
		k++;
	double d = 0;
	for (i=0;i<k;i++)
		{double temp = 2+f*i;double temp1 = 1;double temp2 = temp1/temp;double flag = temp2*c;d = d+flag;}
	double flag = x/(2+f*k);
	d = d + flag;
	list[j] = d;
	}
	for (j=1;j<=num;j++)
		cout << std::setprecision(14) << "Case #" << j << ":  " << list[j] << endl;
}
