#include<iostream>
#include<fstream>
#include<conio.h>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
	ifstream inp("input.in");
	ofstream out("out.txt");
	if(!inp || ! out){
	//	return 100;
	}
	
	int cases;
	inp>>cases;
	for(int z=1;z<=cases;z++)
	{
		string str1,str2;
		int n;
		inp>>n;
		inp>>str1;
		inp>>str2;
		//vector v1,v2;
		int i=0,j=0;
		int count1=0,count2=0;int flag=1,final=0;
		while(i!=str1.length() || j!=str2.length())
		{
			char a=str1[i];
			while(i<str1.length() && a==str1[i+1])
			{
				count1++;
				i++;
			}
			char b=str2[j];
			while(j<str2.length() && a==str2[j+1])
			{
				count2++;
				j++;
			}
			if(a!=b)
			{
				flag=0;
				break;
			}
			else
			{
					if(count1>count2)
					{
						final=final+count1-count2;
					}
					else
					{
						final=final+count2-count1;
					}
			}
			i++;
			j++;
			count1=count2=0;
		}
		out<<"case #"<<z<<": ";
		if(flag==0 || i!=str1.length() || j!=str2.length())
		{
			out<<"Fegla Won"<<endl;
		}
		else
		{
			out<<final<<endl;
		}
	
		
	
		
	}
	return 0;
}

