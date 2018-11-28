#include <iostream>
#include <string>
#include <stdio.h>
#include <conio.h>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

#define i 2
#define j 3
#define k 4


int allFound=0;

signed int matrix[4][4]= {
	{1,2,3,4},
	{2,-1,4,-3},
	{3,-4,-1,2},
	{4,3,-2,-1}
};


int check_ijk(vector<int> taa)
{
	int found = 2,minus=0;
	bool condition = true;
	goto begin;
	signed int temp;
begin:
	while(condition)
	{
		if(allFound)
			{
				if(taa.size()==0)
				{ 
					condition = false;
					if((minus%2)==0)
					 return 1; 
					else
						return 0;
				}
				else if((taa.size()==1))
				{
					if(abs(taa.at(0))!=1)
					{
						condition = false;
						return 0;
					}
					else if((minus%2)!=0)
					{
						condition = false;
						return 0;
					}
					else if(abs(taa.at(0))==1)
					{
						condition = false;
						return 1;
					}
				}
				else if(taa.size()>1)
				{
				 found = 2;
				 goto second;
				 
				}
			}
		goto second;
	    	
second:
		if((found<5)&&(taa.size()>1)) // still i or j or k has to be found
		{
			while(((abs(taa.at(0)))==found)&(!allFound))
			{
				found++; //when i,j,k is found at the begining.
				taa.erase(taa.begin());
				if((!allFound)&(found==5))
				{
					allFound = 1;
					found = 2;
					goto begin;
				}
				
				
			}
			if(taa.size()>=2)
			{
				temp = 0;
			int x = abs(taa.at(0))-1;
			int y = abs(taa.at(1))-1;
			 temp = matrix[x][y];
			}
			else
				goto begin;
			if(temp<0)
					minus++;
				//check if you found any of ikj
			if((abs(temp)==found))
					{
						found++;
						//if(taa.size()>2)
					if(allFound)	
					{		taa.insert(taa.begin(),temp);
							taa.erase(taa.begin()+1);
							taa.erase(taa.begin()+1);
					}
					else
					{
						taa.erase(taa.begin());
							taa.erase(taa.begin());
					}
					}
			else
					{
						taa.insert(taa.begin(),temp);					
						taa.erase(taa.begin()+1);
						taa.erase(taa.begin()+1);
						//taa.insert(taa.begin(),temp); // if not found insert at the begining
					}

			
		} 
		else if (found ==5)
		{
			if(!allFound)
			{
				allFound = 1;
				found=2;
			}
		}
		else if((!allFound)&&(taa.size()==1))
		{
			//if(taa.at(0)!=1)
				return 0;
		}
	}


//return 1;
}
int main()
{
ifstream cin("C-small-attempt0.in");
ofstream cout("out.txt");
int T,L,X;
cin >> T;
vector<int> aa;
string S;

for(int ii=0;ii<T;ii++)
{
	cin>> L >> X;
	
	if((L*X)<3)
	{
		cout <<"Case #"<<ii+1<<": "<<"NO "<<endl;
//	cout <<"Case #"<<ii+1<<": "<<" L X  "<<L<<"   "<<X<<endl;
	string noUse;
	cin>>noUse;
	}
	else if((L*X)>=3)
		{
			cin >> S;
			int count = 0;
			for(int qq = 0;qq <X;qq++)
			{
				for(int bb = 0;bb<L;bb++)
				{
					if(S.at(bb) == 'i')
						aa.insert((aa.begin()+count),2);
					else if(S.at(bb)== 'j')
						aa.insert((aa.begin()+count),3);
					else if(S.at(bb)== 'k')
						aa.insert((aa.begin()+count),4);

					count++;
				}
			}
			int result = check_ijk(aa);
			aa.clear();
			allFound = 0;
			if(result)
				cout <<"Case #"<<ii+1<<": "<<"YES"<<endl;
			else
				cout <<"Case #"<<ii+1<<": "<<"NO"<<endl;
		}

}
}