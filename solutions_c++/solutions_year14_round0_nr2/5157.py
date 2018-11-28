#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <sstream>
#include <fstream>//for writing in files
#include <cctype>
#include <stdlib.h>
#include <iomanip>

using namespace std;


string NumberToString (int Number)
{
	stringstream ss;
	ss << Number;
	return ss.str();
}
int StringToNumber (string Text)
{                              
	stringstream ss(Text);
	int result;
	return ss >> result ? result : 0;
}
bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}
bool isPalindrom(unsigned long long n)
{
	string number=NumberToString(n);
	int lenght=number.size();
	bool check=true;
	for(int i=0;i<lenght;i++)
	{
		if(number[i]==number[lenght-i-1] && check==true)
		{
			check=true;
		}
		else
		{
			check=false;
		}
	}
	return check;
}
int main()
{
	freopen("B-large.in","r",stdin); // For reading input
    freopen("solution.out","w",stdout);
	int n;
	double F;double c,f,x,t1,t2,time,cookies;bool finish=false;
	time=0;t2=0;t1=0;cookies=0;F=2.00000;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		finish=false;
		time=0.00000;t2=0.00000;t1=0.00000;cookies=0;F=2.00000;
		cin>>c>>f>>x;
	//	cout<<c<<" "<<f<<" "<<x<<endl;
		while(!finish)
		{
			t1=x/F;
			t2=(c/F)+(x/(F+f));
			if(t1>t2)
			{
				time+=c/F;
				F+=f;
			}
			else
			{
				time+=t1;
				finish=true;
			}
		}
		cout<<"Case #"<<i+1<<": "<< std::fixed << std::setprecision(7)<<time<<endl;
		//std::cout << std::fixed << std::setprecision(7) << a;
	}
	
	return 0;
}
