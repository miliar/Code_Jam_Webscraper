#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;

int main()
{
	fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\JAM21out.txt");
	int T, s=1;
	cin>>T;
	char list[][10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	while(T)
	{
		char num[2000];
		cin>>num;
		char copy[2000];
		for(int k=0;k<strlen(num);k++)
				{
					copy[k]=num[k];
				}
		
		vector<int> ans;
		//int count=0;
		int itr=0;
		bool fin=true;
		int neg=-1;
	while(fin && neg<10)
	{
		
		for(int i=0;i<10;i++)
		{
			bool flag=true;
			int j=0;
			if(i==neg)
			continue;
			char tmp[2000];
			for(int k=0;k<strlen(num);k++)
				{
					tmp[k]=num[k];
				}
				
			while(list[i][j]!='\0')
			{
				bool found=false;
				
				
				for(int z=0;z<strlen(num);z++)
				{
					if(list[i][j]==num[z] && tmp[z]!='-')
					{
						found=true;
						tmp[z]='-';
						break;
					}
				}
				if(found)
				{
					j++;
				}
				else
				{
					flag=false;
					break;	
				}
				
			}
			
			if(flag)
			{
				for(int k=0;k<strlen(num);k++)
				{
					num[k]=tmp[k];
				}
				//cout<<num<<endl;
				ans.push_back(i);
			}
			
		}
		int count=0;
		for(int l=0;l<strlen(num);l++)
		{
			if(num[l]=='-')
			{
				count++;
			}
		}
		if(count==strlen(num))
		{
			fin=false;
		}
		if(itr>strlen(num))
			{
				neg++;
				cout<<neg<<endl;
				ans.clear();
				for(int k=0;k<strlen(num);k++)
				{
					num[k]=copy[k];
				}
				itr=0;
			}
			itr++;
	}
		sort(ans.begin(),ans.end());
		long int res=0;
		cout<<"Case #"<<s<<": ";
		fil<<"Case #"<<s<<": ";
		for(int i=0;i<ans.size();i++)
		{
			cout<<ans[i];
			fil<<ans[i];
		}
		cout<<endl;
		fil<<"\n";
		s++;
		T--;
		
	}
	
	fil.close();
}
