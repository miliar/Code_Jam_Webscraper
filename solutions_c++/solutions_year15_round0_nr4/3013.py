#include<iostream>
#include<fstream>
using namespace std;
int main()
{
		ofstream fout ("sub1.out");
    ifstream fin ("sub1.in");
		int tes;
		fin>>tes;
		for(int u=0;u<tes;u++)
		{
				fout<<"Case #"<<u+1<<": ";
				int x,r,c;
				fin>>x>>r>>c;
				int ct=0;
				switch(x)
				{
						case 1:
								ct=1;
							break;
						case 2:
							if(r*c%2==0)
								ct=1;
							break;
						case 3:
							if(r*c%3==0&&min(r,c)>1)
								ct=1;
							break;
						case 4:
							if(r*c%4==0&&min(r,c)>2)
								ct=1;
							break;
				}
				if(ct)
					fout<<"GABRIEL\n";
				else
					fout<<"RICHARD\n";
		}
		return 0;
}
				
				
				
				
