#include <iostream>
#include <fstream>
#include <stdlib.h> 
#include <string>

using namespace std;


int atoichar(char a)
{
	if(a=='0') return 0;
	if(a=='1') return 1;
	if(a=='2') return 2;
	if(a=='3') return 3;
	if(a=='4') return 4;
	if(a=='5') return 5;
	if(a=='6') return 6;
	if(a=='7') return 7;
	if(a=='8') return 8;
	if(a=='9') return 9;
	
}

int main()
{
	int tests;
	cin>>tests;
	ofstream fout;
  	fout.open("datalarge.txt");
	for(int count = 1;count <=tests;count++)
	{
		int Smax;
		cin>>Smax;
		char* shyness;
		cin>>shyness;
		int max = 0;
		int need = 0;
		for(int count1 = 0;count1<=Smax;count1++)
		{
			need += (1-atoichar(shyness[count1]));
			//cout<<count1<<" "<<need<<endl;  
			if (need >max) max = need;
		}
		fout<<"Case #"<<count<<": "<<max<<endl;
		
	}
	
}

