
#include<iostream>
#include<fstream>

using namespace std;


unsigned long long int find_rings(unsigned long long int radius, unsigned long long int volume_paint)
{
	int x = 1;
	int count = 0;
	unsigned long long int temp_vol = 0;
	
	while(temp_vol <= volume_paint)
	{
		++count;
		temp_vol += (2*radius) + x;
		x += 4;
	}
	
	return (count-1);
}

int main()
{
	int cases;
	int count = 0;
	unsigned long long int r, t;
	
	
	ifstream in("A-small-attempt2.in");
	
	if(!in)
	{
		cout<<"Cannot open file..."<<endl;
		return 0;
	}
	
	in >> cases;
	
	while(++count <= cases && !in.eof())
	{	
		in>>r;
		in>>t;
	
		unsigned long long int n = find_rings(r, t);
	
		cout<<"Case #"<<count<<":"<<" "<<n;
		cout<<endl;
	}
		
	return 0;
}
