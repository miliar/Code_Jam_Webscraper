#include<iostream>
using namespace std;
void remove( int x , int *digit_found , int arr[10])
{
	if(arr[x] == 0)
	{
		arr[x]=1;
		*digit_found = *digit_found + 1;
	}
}
int main()
{
	int inp, counter, arr[10], no_of_test_cases, temp, digit_found,no_of_finished_cases=0;
	cin >> no_of_test_cases;
	while(no_of_test_cases>no_of_finished_cases)
	{
		no_of_finished_cases++;
		digit_found = 0;
		for(counter=0;counter<10;counter++)
			arr[counter]=0;
		cin >> inp;
		for(counter=1; counter<100 ; counter++)
		{
			temp = counter*inp;
			while(temp != 0)
			{	
				remove(temp%10 , &digit_found ,arr);
				temp = temp/10;
			}
			if(digit_found == 10)
				break;
		}
		if(digit_found == 10)
			cout<<"Case #"<<no_of_finished_cases<<": "<<counter * inp<<endl;
		else
			cout<<"Case #"<<no_of_finished_cases<<": "<<"INSOMNIA"<<endl;
	}
}