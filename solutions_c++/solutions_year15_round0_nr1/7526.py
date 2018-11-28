// Standing Ovation

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream gp1;
	ifstream gp;
	gp1.open("output.txt");
	gp.open("input.txt");
	
	int tc;
	gp >> tc;
	
	for(int t = 1; t <= tc ; t++)
	{
		int smax;
		gp >> smax;
		
		char *s = new char[smax];
		for(int i = 0; i <= smax ; i++)
		{
			gp >> s[i];
			//cout << s[i] << " " ;
		}
		
		int standing = (s[0] - '0'), invite = 0;
		for(int i = 1; i <= smax; i++) 
		{
			if(standing < i) 
			{
				invite += (i - standing);
				standing += (i - standing);
			} 
				
				standing += (s[i] - '0');
			
		}
		gp1 << "Case #" << t << ": " << invite << endl;
	}
	
	gp.close();
	gp1.close();
}