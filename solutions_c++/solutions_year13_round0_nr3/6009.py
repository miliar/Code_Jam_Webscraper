#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
#include<list>
#include<algorithm>

using namespace std;


bool is_palindrome(long long int i)
{
	list<int> l1;
	list<int> l2;
		
	while(i>0)
	{
		l1.push_back(i%10);
		l2.push_front(i%10);
		i /= 10;
	}

	list<int>::iterator first = l1.begin();
	list<int>::iterator second = l2.begin();
		
	while(first != l1.end())
	{	
		if(*first != *second)
			return false;

		first++;
		second++;
	}
	
	return true;
}


void fair_and_square(long long int x, long long int y, int case_number)
{
	int fair_and_square_count = 0;

	long long int lower_root = pow(x, 0.5);
	long long int upper_root = pow(y, 0.5);
	
	if(pow(lower_root, 2) < x)
		lower_root++;
		
	for(long long int i = lower_root ; i <= upper_root ; i++)
	{
		if(is_palindrome(i))
		{
			if(is_palindrome(pow(i, 2)))
				fair_and_square_count++;
		}
	}
	
	cout<<"Case #"<<case_number<<":"<<" "<<fair_and_square_count;
	return;
}


int main()
{
	int cases;
	int count = 0;
	
	long long int x, y;

	ifstream in("C-small-attempt0.in");
	
	if(!in)
	{
		cout<<"Cannot open file..."<<endl;
		return 0;
	}
	
	in >> cases;
	
	while(++count <= cases && !in.eof())
	{	
		in>>x;
		in>>y;
		
		fair_and_square(x, y, count);
		
		cout<<endl;
	}
	
	in.close();

	return 0;
}		
		

