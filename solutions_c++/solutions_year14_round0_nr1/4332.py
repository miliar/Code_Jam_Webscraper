#include <iostream>
#include <vector>
#include <algorithm> 
#include <set>
#include <fstream>

using namespace std;
typedef set<int> si;

ifstream in("a.in"); ofstream out("a.out");
int T, tmp, l=1;

int main()
{
	in>>T;
	while(T--)
	{
		int a,b,tmp;
		si  s1 , s2,inter;

		in>>a;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				in>>tmp;
				if(i==a) s1.insert(tmp);				
			}
		}

		in>>b;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				in>>tmp;
				if(i==b) s2.insert(tmp);				
			}			
		}
		
		set_intersection(s1.begin(),s1.end(),s2.begin(),s2.end(),inserter(inter,inter.begin()));
		
		if(inter.size()==0) out<<"Case #"<<l<<": "<<"Volunteer cheated!"<<endl;
		else if(inter.size()==1) out<<"Case #"<<l<<": "<<*inter.begin()<<endl;
		else out<<"Case #"<<l<<": "<<"Bad magician!"<<endl;
		
		l++;
		
		}
    }




