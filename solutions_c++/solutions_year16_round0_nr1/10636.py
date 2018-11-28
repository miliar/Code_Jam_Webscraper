#include<iostream>
using namespace std;
#include<vector>
#include<fstream>

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin>>t;
	int count=1;
	while(t--)
	{
		int n;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<count++<<": INSOMNIA"<<endl;
		}
		else{
			int flag=0,a=1,x;
			vector<bool> arr(10);
			while(flag==0){
				x=n*a;
				int z=x; 
				
				while(z!=0)
				{
					arr[z%10]=1;
					z/=10;
				}
				for(int i=0;i<10;i++)
				{
					if(arr[i]==false)
						break;
					else if(arr[i]==true && i==9)	
						flag=1;
				}
				if(flag==0)
					a++;
			}
			cout<<"Case #"<<count++<<": "<<x<<endl;
		}
	}
	return 0;
}
