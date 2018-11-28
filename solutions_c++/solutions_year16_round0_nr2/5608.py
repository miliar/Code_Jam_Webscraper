#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

int main(){
	int i,j,k,l;
	int T, nFlips;
	string str;
	cin>>T;
	for(l = 0 ; l < T ; l++)
	{	
		cout<<"Case #"<<l + 1<<": ";
		cin>>str;
		nFlips = 0;
		int N = str.length();
		while(true){
			for(i = 0 ; i < N ; i++)
				if(str[i] == '-')
					break;
			if(i == N)
				break;
			if(i != 0)
				nFlips++;
			for(j = 0 ; j < i ; j++)
				str[j] = '-';
			int pos = i;
			for(j = i ; j < N ; j++)
				if(str[j] == '-')
					pos = j;
			string substring = str.substr(0, pos+1);
			for(i = 0 ; i <= pos ; i++)
				if(substring[i] == '-')
					substring[i] = '+';
				else
					substring[i] = '-';
			nFlips++;
			for(i = pos ; i >= 0 ; i--)
				str[pos - i] = substring[i];			
		}
		cout<<nFlips<<"\n";
	}
	return 0;
}
