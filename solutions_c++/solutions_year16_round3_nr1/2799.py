#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<iterator>
#include<cmath>
#include<string>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<bitset>
#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>
 
using namespace std;



int main() 
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,temp,t,total,th,index=1; ;
vector<pair<int,char>> num;
cin>>t;
while(t--)
{
total=0;
num.clear();
num.push_back(make_pair(0,('a')));
	cin>>n;
	for(int i=0; i<n; i++)
	{
		cin>>temp;
		total+=temp;
		num.push_back(make_pair(temp,(i+'A')));
	}
	sort(num.begin(),num.end());
		reverse(num.begin(),num.end());
	cout<<"Case #"<<index++<<": ";
	while(num[0].first!=0)
	{
		
		if(total>=2)
		{
			th=((total-2)/2)+1;
			if(num[0].first>=th && num[1].first>=th && num[2].first<th)
			{
				cout<<num[0].second<<num[1].second<<" ";
				num[0].first-=1;	num[1].first-=1;
				total-=2;
				sort(num.begin(),num.end());
		reverse(num.begin(),num.end());
				
			}
			else
			{
				if(num[0].first>=2)
				{
					cout<<num[0].second<<num[0].second<<" ";
					num[0].first-=2;
					total-=2;
					sort(num.begin(),num.end());
					reverse(num.begin(),num.end());
				}
				else
				{
				cout<<num[0].second<<" ";
				num[0].first-=1;
				total-=1;
				sort(num.begin(),num.end());
				reverse(num.begin(),num.end());
			
				}
			}
		}
		else
		{
			cout<<num[0].second<<" ";
				num[0].first-=1;
				total-=1;
				sort(num.begin(),num.end());
		reverse(num.begin(),num.end());
			
		}
	}
	cout<<endl;
	
}


//system("pause");
  return 0;
}
