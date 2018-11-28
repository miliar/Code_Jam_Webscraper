#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
int main()
{
	int testcases;
	ifstream in("B-large.in");
	ofstream out("out.txt");
	out.precision(7);
    out.setf(std::ios::fixed, std::ios::floatfield);
	//enter number of test cases
	in>>testcases;
	for(int i=0;i<testcases;i++)
	{
		string a;
		double start_cookie=2,c,f,x;
		in>>c;
		in>>f;
		in>>x;
		
		getline(in,a);
		double second=0,new_second=0.0,second_for_win=-1,second_for_farm;
		int cc;
		if(x<c)//if cookies for win less than cookies to by a farm
			{
			second=x/start_cookie*1.0;
			out<<"case #"<<i+1<<":"<<" "<<second<<"\n";
			}
		else//if cookies for win larger than cookies to by a farm
				{
					while(second_for_win<second)
					{cc=0;
					second_for_win=new_second+x/start_cookie*1.0;
						second_for_farm=c/start_cookie*1.0;
						start_cookie+=f;
						new_second+=second_for_farm;
						second=new_second+x/start_cookie*1.0;
						if(second_for_win<second)
						{
								out<<"case #"<<i+1<<":"<<" "<<second_for_win<<endl;
								cc=1;
								break;
						}
						second_for_farm=c/start_cookie*1.0;
						start_cookie+=f;
						new_second+=second_for_farm;
						second_for_win=new_second+x/start_cookie*1.0;
					}
					if(cc==0)
					out<<"case #"<<i+1<<":"<<" "<<second<<endl;
					
				}
		
		
		
	}
}
