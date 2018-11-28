#include<iostream>
#include<fstream>
using namespace std;

int arr[26];


void d0(int* arr)
{
	arr['Z']--;
	arr['E']--;
	arr['R']--;
	arr['O']--;
}

void d1(int* arr)
{
	arr['O']--;
	arr['N']--;
	arr['E']--;
}

void d2(int* arr)
{
	arr['T']--;
	arr['W']--;
	arr['O']--;
}

void d3(int* arr)
{
	arr['T']--;
	arr['H']--;
	arr['R']--;
	arr['E']--;
	arr['E']--;
}

void d4(int* arr)
{
	arr['F']--;
	arr['O']--;
	arr['U']--;
	arr['R']--;
}

void d5(int* arr)
{
	arr['F']--;
	arr['I']--;
	arr['V']--;
	arr['E']--;
}

void d6(int* arr)
{
	arr['S']--;
	arr['I']--;
	arr['X']--;
}

void d7(int* arr)
{
	arr['S']--;
	arr['E']--;
	arr['V']--;
	arr['E']--;
	arr['N']--;
}

void d8(int* arr)
{
	arr['E']--;
	arr['I']--;
	arr['G']--;
	arr['H']--;
	arr['T']--;
}

void d9(int* arr)
{
	arr['N']--;
	arr['I']--;
	arr['N']--;
	arr['E']--;
}



int main()
{
	
	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);

	int i,t;
	fin>>t;
	for(i=1;i<=t;i++)
	{
		int j;
		string str,ans="";
		fin>>str;


		for(j=65;j<65+26;j++)
		{
			arr[j]=0;
		}



		for(j=0;j<str.length();j++)
		{
			arr[str[j]]++;
			
		}
		
		
		
		for(j=0;j<arr['Z'];)
		{
			ans=ans+'0';
			d0(arr);
		}

		for(j=0;j<arr['W'];)
		{
			ans=ans+'2';
			d2(arr);
		}

		for(j=0;j<arr['U'];)
		{
			ans=ans+'4';
			d4(arr);
		}

		for(j=0;j<arr['X'];)
		{
			ans=ans+'6';
			d6(arr);
		}

		for(j=0;j<arr['O'];)
		{
			ans=ans+'1';
			d1(arr);
		}

		for(j=0;j<arr['R'];)
		{
			ans=ans+'3';
			d3(arr);
		}

		for(j=0;j<arr['F'];)
		{
			ans=ans+'5';
			d5(arr);
		}

		for(j=0;j<arr['S'];)
		{
			ans=ans+'7';
			d7(arr);
		}

		for(j=0;j<arr['T'];)
		{
			ans=ans+'8';
			d8(arr);
		}

		for(j=0;j<arr['I'];)
		{
			ans=ans+'9';
			d9(arr);
		}



cout<<ans<<"@";

		int temp[10],l;
		l=ans.length();
		for(j=0;j<10;j++)
		{
			temp[j]=0;
		}
		for(j=0;j<l;j++)
		{
			temp[ans[j]-48]++;
		}
		ans="";
		for(j=0;j<10;j++)
		{
			if(temp[j]!=0)
			{
				for(int k=0;k<temp[j];k++)
				ans+=j+48;
			}
		}

cout<<ans<<endl;


			fout<<"Case #"<<i<<": "<<ans<<endl;		
	}








	
	cout<<"done";
	return 0;
}
