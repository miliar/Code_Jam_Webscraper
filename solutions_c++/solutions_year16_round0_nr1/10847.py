#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
int main()
{
	freopen("ques.in","r",stdin);
    freopen("answer.txt","w",stdout);
	int t;
	long long int n;
	cin>>t;
	int tmp = t;
	while(t--)
	{
		set<int> s;
		int i=1;
		long long int tmp1;
		cin>>n;
		long long int k = n;
		if (n==0)
		{
			cout<<"Case #"<<tmp-t<<": "<<"INSOMNIA"<<endl;
		}
		else
		{	
			s.clear();
			do{
			 	n=k*i; 
			 	tmp1 = n;
				while(n!=0)
				{                  

					s.insert(n%10);
					n = n/10;

				}
  				
  				i++;                        
				
				}while(s.size()!=10);

				
			
			cout<<"Case #"<<tmp-t<<": "<<tmp1<<endl;
		}
	}
}