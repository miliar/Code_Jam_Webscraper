#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<stack>
#include <fstream>


using namespace std;

int main()
{
	int T;
	cin>>T;	
	ofstream outputFile;
	outputFile.open("data.txt");
	for(int j=0;j<T;j++)
	{
		int maxS,cur=0,cnt=0;
		cin>>maxS;
		string people;
		cin>>people;
		for(int i=0;i<=maxS;i++)
		{
			if(cur>=i && people[i]>'0')
				cur+=(people[i]-'0');
			else{
				while(cur<i)
				{
					cnt++;
					cur++;
				}
				cur+=(people[i]-'0');
			}
			
		}
		cout<<"Case #"<<j+1<<": "<<cnt<<endl;
		outputFile<<"Case #"<<j+1<<": "<<cnt<<endl;
	}
	outputFile.close();
}