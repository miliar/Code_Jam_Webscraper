#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fout.open("input.txt");
	fin.open("A-large.in");
	int counter=0,a;
	fin>>counter;
	int y=1;
	while(counter>0)
	{
		fin>>a;
		if(a==0)
		{
			fout<<"Case #"<<y<<": INSOMNIA"<<endl;
		}
		else
		{
		
		int i=2;
		int aa=a,s=a;
		
	int cou=0;
	int arr[10]={0,1,2,3,4,5,6,7,8,9};
		while(cou<=9)
		{
		
		while(aa!=0)
		{
			for(int i=0;i<10;i++)
			{
				if(arr[i]==aa%10)
				{
					cou++;
					//cout<<arr[i]<<endl;
					arr[i]=-1;
					break;
				}
			}
			aa=aa/10;
		}
		aa=i*a;
	//	cout<<aa<<endl;
		s=i*a;
		i++;
	}
			fout<<"Case #"<<y<<": "<<a*(i-2)<<endl;
		;}
		counter--;
		y++;
	}
}
