# include<iostream>
# include<fstream>
# include<cmath>
using namespace std;
 
bool check(int a)
{
	int i,j,k = 0;
	for(int i = a; i > 0; i /= 10)
	{
		j = i % 10; 
		k = (k * 10) + j;
	}
	if(k == a)
	{
		return true;
	}
	return false;
}
int main()
{
	int i, count = 0, k1 = 1;
	fstream file1("OUTPUT.TXT",ios::in | ios::out);
	fstream file("C-small-attempt0.in",ios::in | ios::out);		
	file >> i;
	while(i > 0)
	{
		int a, b;
		file >> a >> b; 
		for(double j = a; j <= b; j++)
		{
			if(check(j))
			{
				double z = sqrt(j);
				if(floor(z)== z)
				{
					if(check(z))
					{
						count++;
					}
				}
			}
		}
		i--;
		file1 << "Case #" << k1 << ": " << count << endl;
		count = 0;
		k1++;
	}
	return 0;
}
