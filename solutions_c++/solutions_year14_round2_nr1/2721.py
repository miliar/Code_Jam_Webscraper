#include <iostream>
#include <string>
#include <math.h>
#include <stdlib.h>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		bool correct=true;
		int N;
		cin>>N;
		int index[N];
		int count[N];
		int countmax=0;
		int min1=0;
		string array1[N];
		for(int j=0;j<N;j++)
		{
			string a;
			cin>>a;
			array1[j]=a;
			index[j]=0;
			count[j]=0;
		}
		char start=array1[0][0];
		int end=0;
		bool check1=false;
		bool print=false;
		while(end<N)
		{
			/*int check=0;
			bool check1[N];
			for(int q=0;q<N;q++)
			{
				check1[q]=false;
			}*/
			bool check=check1;
			for(int k=0;k<N;k++)
			{
				int l=index[k];
				if(check && index[k]!=array1[k].length())
				{
					correct=false;
					break;
				}
				/*if(k>ch && check2 && index[k]!=array1[k].length())
				{
					correct=false;
					break;
				}*/
				if(index[k]==array1[k].length())
				{
					end++;
					break;
				}
				if(array1[k][l]!=start)
				{
					correct=false;
					break;
				}	
				while(array1[k][l]==start && l<array1[k].length())
				{
					/*if(!check1[k])
					{
						check++;
						check1[k]=true;
					}*/
					if(end!=0)
					{
						correct=false;
					}
					count[k]++;
					index[k]++;
					/*if(index[k]=array1[k].length())
					{
						check1=true;
					}*/
					if(countmax<count[k])
					{
						countmax=count[k];
					}
					l++;
				}
				if(l==array1[k].length())
				{
					check1=true;
					//check2=true;
					//ch=k;
				}
				//cout<<index[k]<<" "<<count[k]<<endl;	
			}
			if(!correct)
			{
				cout<<"Case #"<<i<<": Fegla Won"<<endl;
				print=true;
				break;
			}
			
			start=array1[0][index[0]];
			int min=1000;
			int minin=0;
			for(int m=1;m<=countmax;m++)
			{
				int steps=0;
				for(int p=0;p<N;p++)
				{
					steps+=abs(m-count[p]);
				}
				if(min>steps)
				{
					min=steps;
					minin=m;
				}
				//cout<<steps<<endl;
			}
			//cout<<min<<endl;
			if(min<105)
			{
				min1+=min;
			}
			for(int m=0;m<N;m++)
			{
				count[m]=0;
				countmax=0;
			}
				
		}
		string c=array1[0];
		int correct1=0;
		if(min1==0)
		{
			for(int q=0;q<N;q++)
			{
				if(array1[q]!=c)
				{
					correct=false;
					correct1=1;
					break;
				}
			}
		}
		if(!correct && !print)
		{
			cout<<"Case #"<<i<<": Fegla Won"<<endl;
		}			
		if(correct)
		{
			cout<<"Case #"<<i<<": "<<min1<<endl;
		}
	}
}
