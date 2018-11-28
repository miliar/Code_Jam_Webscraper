# include<iostream>
# include<fstream>
# include<cmath>
using namespace std;
int main()
{
	int i, j = 1;
	fstream file1("A-small-attempt0(1).in",ios::in|ios::out);
	fstream file2("OUTPUT.TXT",ios::in|ios::out);
	long r = 0, t = 0, area = 0;
	long count = 0;
	file1 >> i;
	while(i > 0)
	{
		file1 >> r >> t;
		while (t >= 0)
		{
			area = ((r+1)*(r+1)) - ((r)*(r));
			t -= area;
			r += 2;
			if(t >= 0)
			{
				count++;
			}
		};
		i--;
		file2 << "Case #"<<j << ": "<< count<< endl;
		count = 0;
		j++;
	}
	return 0;
}
