#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;


int main() {
	int cases=0;
	cin >> cases;
	for(int casesIter=0;casesIter<cases;casesIter++) {
		int smax;
		std::vector<char> svector;
		char temp;

		scanf("%d ", &smax);
		for(int i=0;i<=smax;i++)
		{
			scanf("%c", &temp);
			svector.push_back(temp);
		}
		scanf("%c\n",&temp);
		svector.push_back(temp);
		
		int pos;
		int accu;
		int final;
		pos = accu = final = 0;
		for(std::vector<char>::iterator it = svector.begin(); it<svector.end(); it++)
		{
			if(accu >= pos)
			{
				accu +=	(*it - '0');
			}
			else
			{
				if((*it - '0') > 0)
				{
					final += (pos-accu);
					accu += (*it - '0') + (pos-accu);
				}
			}
			//cout<<"Accu= "<<accu<<" "<<"Pos= "<<" "<<pos<<endl;
			pos++;
		}
		
		svector.clear();	
		cout<<"Case #"<<casesIter+1<<": "<<final<<endl;
		
	}
	return 0;

}
