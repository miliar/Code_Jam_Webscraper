#include<iostream>
#include<string.h>
using namespace std;


int a[10];
int count1;

	unsigned long long int function1(unsigned long long int a2){
	unsigned long long int a1 = a2;
	int ctr = 1;

	while(count1 < 10){
	a1 = a2*ctr;
	ctr++;
	string s = std::to_string(a1);
	char const *chars = s.c_str();  //
	for (int i = 0; i < strlen(chars); ++i)
	{
		switch(chars[i]){

			case 48:{
				if (a[0] == 0)
				{
					a[0] = 1;
					count1++;

				}
			}
			break;
			case 49:{
				if (a[1] == 0)
				{
					a[1] = 1;
					count1++;

				}

			}
			break;
			case 50:{
				if (a[2] == 0)
				{
					a[2] = 1;
					count1++;

				}
			}
			break;
			case 51:{
				if (a[3] == 0)
				{
					a[3] = 1;
					count1++;

				}


			}
			break;
			case 52:{
				if (a[4] == 0)
				{
					a[4] = 1;
					count1++;

				}


			}
			break;
			case 53:{
				if (a[5] == 0)
				{
					a[5] = 1;
					count1++;

				}


			}
			break;
			case 54:{
				if (a[6] == 0)
				{
					a[6] = 1;
					count1++;

				}


			}
			break;
			case 55:{
				if (a[7] == 0)
				{
					a[7] = 1;
					count1++;

				}


			}
			break;
			case 56:{
				if (a[8] == 0)
				{
					a[8] = 1;
					count1++;

				}


			}
			break;
			case 57:{
				if (a[9] == 0)
				{
					a[9] = 1;
					count1++;

				}


			}
			break;

		}


		}
		if (count1 == 10)
		{
			break;
		}
	}
return a1;
}


int main(){

	unsigned long long int num;
	int t;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		count1 = 0;
		for (int i = 0; i < 10; ++i)
		{
			a[i] = 0;
		}
		cin>>num;
		if (num == 0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
			continue;
		}

		num = function1(num);
		cout<<"Case #"<<i+1<<": "<<num<<endl;
	}


}