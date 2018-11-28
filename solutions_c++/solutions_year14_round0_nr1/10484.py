#include<stdio.h>
//#include<fstream>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int main()
{
	//fstream f("C:/Users/Shweta/Desktop", ifstream::in);
	int T ;
	
	cin>>T;
	
	int j=0;
	vector<int> v1;
	vector<int> v2;
	while(j<T)
	{
		v1.clear();
		v2.clear();
		int row1;
		cin>>row1;
		//cout<<"row1 "<<row1<<endl;
		int temp;
		for(int k=1;k<row1;k++)
		{
			for(int l=0;l<4;l++)
			{
				cin>>temp;
			}
			
		}
		for(int k=0;k<4;k++)
		{
			cin>>temp;
			v1.push_back(temp);
		}
		for(int k=row1;k<4;k++)
		{
			for(int l=0;l<4;l++)
			{
				cin>>temp;
			}
			
		}
		int row2;
		cin>>row2;
		//cout<<"row2 "<<row2<<endl;
		
		for(int k=1;k<row2;k++)
		{
			for(int l=0;l<4;l++)
			{
				cin>>temp;
			}
			
		}
		for(int k=0;k<4;k++)
		{
			cin>>temp;
			v2.push_back(temp);
		}
		for(int k=row2;k<4;k++)
		{
			for(int l=0;l<4;l++)
			{
				cin>>temp;
			}
			
		}
		for(int l=0;l<v1.size();l++)
		{
			//cout<<"Element in v1 "<<v1.at(l)<<" ";
		}
		//cout<<endl;
		for(int l=0;l<v1.size();l++)
		{
			//cout<<"Element in v2 "<<v2.at(l)<<" ";
		}
		//cout<<endl;
		std::vector<int> v(10);   
		std::sort (v1.begin(),v1.end());     
		std::sort (v2.begin(),v2.end());   
		std::vector<int>::iterator it;
		it=std::set_intersection (v1.begin(),v1.end(), v2.begin(),v2.end(),v.begin());
      
		v.resize(it-v.begin());                

		//std::cout << "The intersection has " << (v.size()) << " elements:\n";
		if(v.size()==1)
		{
			cout<<"Case #"<<j+1<<": "<<v.at(0)<<endl;
		}
		else if(v.size()>1)
		{
			cout<<"Case #"<<j+1<<": "<<"Bad magician!"<<endl;
		}
		else
		{
			cout<<"Case #"<<j+1<<": "<<"Volunteer cheated!"<<endl;
		}

		
		j++;
	}
}