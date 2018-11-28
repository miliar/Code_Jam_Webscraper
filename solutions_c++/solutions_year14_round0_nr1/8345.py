#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream a;
	ofstream q;
	int A[34];
	int B[4];
	a.open("A-small-attempt2.in");
	q.open("A-small-out.txt");
	int t,c = 0,b = 0, i = 0,x = 0,y;
	a>>t;
	for(c = 0; c < t;c++)
	{while (b < 34)
		{a>>A[b];b++;}
	for(b = 0;b < 4;b++)
		{B[b] = A[4*A[0] - 3 + b]; b++;}
	for(b = 0; b < 4; b++)
		{for(i = 0; i < 4; i++)
			{if (A[4*A[0] - 3 + i] == A[4*A[17] + 14 + b])
				{y = A[4*A[17] + 14 + b];x++;}
            }
		}
	if (x == 1)
		{q<<"Case #"<<c+1<<": "<<y<<endl;}
	else if (x == 0)
		{q<<"Case #"<<c+1<<": Volunteer cheated!"<<endl;}
	else
		{q<<"Case #"<<c+1<<": Bad magician!"<<endl;}
    x = 0;b = 0;i = 0;
	}
};

