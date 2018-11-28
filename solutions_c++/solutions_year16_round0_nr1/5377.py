#include <iostream>
#include <fstream>

using namespace std;
bool checkdig(bool arr[]);
int main()
{
	fstream myfile;
	ofstream codejam;
	codejam.open("OutPut.txt");

	myfile.open("Problem.txt");
	char a[1000];
	myfile.getline(a,1000);
	int T = atoi(a);
	int t = 0;
	cout<<T<<endl;
	int N = 200;
	
	bool digits[10];
	
	int sleep_it = 1;
	while(T!=0 && T<=100)
	{
		myfile.getline(a,1000);
		T--;
		t++;
		sleep_it = 1;
		long int check = atoi(a);
		long int check1 = check;
		bool m = false;
		for(int i=0; i<10; i++)
		{
			digits[i] = false;
		}
		while(m == false)
		{
			int index = 0;
						
			while(a[index]!='\0')
			{
			
				int curr_num = a[index] - '0';
				if(digits[curr_num] == false)
				{
					digits[curr_num] = true;
				}
				
				index++;
			}
		
			if(checkdig(digits) == true)
			{
					//we done	
					if(T!=0)
					{
					codejam << "Case #" <<t<<": "<<check<<endl;
					}
					else
					{
						codejam << "Case #" <<t<<": "<<check;
					}
					m = true;
			}
			else if(check1 == (check1*(sleep_it+1)))
			{
				sleep_it++;
				codejam << "Case #" <<t<<": "<<"INSOMNIA"<<endl;
				m = true;
			}
			sleep_it++;
			check = check1 * sleep_it;
			itoa(check,a,10);
		}	
		
	}
	
}
bool checkdig(bool arr[])
{
	for(int i=0; i<10; i++)
	{
		if(arr[i] == false)
		{
			return false;
		}
	}
	return true;
}
