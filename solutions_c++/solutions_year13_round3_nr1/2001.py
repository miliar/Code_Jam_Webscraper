#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;


#include <stdio.h>

int solution(string name, int n);
int main() {


	ifstream fin("input.in");
	ofstream fout("output.out");


	int T;

	fin >> T;
	
	while( T-- > 0 ) {


		string name;
		int k;
		fin >> name >> k;

		



		int sol = solution(name, k);





		static int cs = 1;

		fout << "Case #"<< cs++<< ": "<<  sol << endl;

	}
	

	fin.close();
	fout.close();


	return 0;
}


int solution(string name, int n)
{
			
	int count = 0;
	int sol = 0;

	for(int i =0 ; i< name.size(); i++)
	{
		if(name[i] !='a' && name[i] !='u' && name[i] !='o' && name[i] !='i' && name[i] !='e')
			count++;
		else
			count=0;
		if(count ==n)
		{
			sol = (i-n+2)*(name.size() -i);
			name.erase(0,i-n+2);
			break;

		}


	}
	if(count<n) return 0;
	return sol += solution(name, n);

	


}