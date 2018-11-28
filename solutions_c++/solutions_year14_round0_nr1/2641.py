#include<iostream>
#include<fstream>
int main()
{
	std::ifstream in;
	in.open("A-small-attempt0.in");
	std::ofstream out;
	out.open("A-small-attempt0.out");
	int T, a1, a2, x[4][4], y[4][4], i, j, count, c=0, num;
	in>>T;
	while(T--)
	{
		c++;
		count = 0;
		in>>a1;
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				in>>x[i][j];

		in>>a2;
		for(i=0; i<4; i++)
			for(j=0; j<4; j++)
				in>>y[i][j];

		for(i = 0; i<4; i++)
			for(j=0; j<4; j++)
			{
				if(x[a1-1][i] == y[a2-1][j])
				{
					num = x[a1-1][i];	
					count++;
				}
			}
		
			if(count == 0)
				out<<"Case #"<<c<<": Volunteer cheated!\n";
			else if(count == 1)
				out<<"Case #"<<c<<": "<<num<<"\n";
			else
				out<<"Case #"<<c<<": Bad magician!\n";

	}
}