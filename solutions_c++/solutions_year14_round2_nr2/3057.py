#include <fstream>
#include <iostream>
using namespace std;

int main ()
{
	int casi;
	
	ifstream in("input.txt");
	ofstream out("output.txt");
	
	in>> casi;
	for (int c=1; c<=casi; c++)
	{
		int A, B, K, sol=0;
		in>>A >>B >>K;
		//cout<<A <<B <<K<<endl;
		for (int a=0; a<A; a++)
			for (int b=0; b<B; b++)
			{
				
				if ( (a&b) <K )
				{
					sol++;
				}
				//cout<<a<<" "<<b<<" "<<(a&b)<<" "<<sol<<endl;
			}
				
		out<<"Case #" <<c <<": " <<sol<<endl;
		//cin.get();
	}
	
	return 0;
}
