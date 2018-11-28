#include <iostream> 
#include <string>
#include <list>

using namespace std;
void main(){
	int N, modulus, count;
	unsigned long int number, tmp_number;
	list<int> lst_digits;
	cin >> N;
	for(int i = 0; i < N; i++)
	{
		lst_digits.clear();
		for(int i = 0; i < 10; i++)
		{
			lst_digits.push_back(i);
		}
		cin >> number;
		if(number == 0)
		{
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		tmp_number = number;		
		while(tmp_number != 0)
		{
			modulus = tmp_number % 10;
			lst_digits.remove(modulus);
			tmp_number = tmp_number / 10;
		}
		//cout<<"list size "<<lst_digits.size()<<endl;
		if(lst_digits.empty())
		{
			cout<<"Case #"<<i+1<<": "<<number<<endl;
			continue;
		}
		count = 2;
		while(!lst_digits.empty())
		{
			tmp_number = count * number;
			while(tmp_number != 0)
			{
				modulus = tmp_number % 10;
				lst_digits.remove(modulus);
				tmp_number = tmp_number / 10;
			}
			if(lst_digits.empty())
			{
				cout<<"Case #"<<i+1<<": "<<count * number<<endl;
				continue;
			}
			count++;
		}
	}
}