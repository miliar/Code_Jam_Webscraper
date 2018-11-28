#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("A-small-input0.in");
	ofstream out("out.txt");
	int t;
	in>>t;
	for(int x=1;x<=t;x++)
	{
		out<<"Case #"<<x<<": ";
		int n;
		int a;
		in>>a>>n;

		int arr[105];
		for(int i=0;i<n;i++)
			in>>arr[i];

		for(int i =0;i<n-1;i++)
		{
			for(int j=i;j<n;j++)
			{
				if(arr[i]>arr[j])
					swap(arr[i],arr[j]);
			}
		}
		//cout<<a<<endl;
		for(int i =0;i<n-1;i++)
		{
			//cout<<arr[i]<<"  ";
		}
		//cout<<endl;
		int sum=a;
		int cheats=0;
		bool cheat_possible=true;
		for(int i=0;i<n;i++)
		{
			if(sum>arr[i])
			{
				sum+=arr[i];
			}
			else 
			{
				if(sum == 1){
					cheats += n-i;
					break;
				}
				int temp1=1;
				int temp2=n-i;
				int temp3=sum;
				while(temp3 + temp3 -1 <= arr[i]){ 
					
					temp1++;
					temp3 += temp3 - 1;
				}
				
				if(temp1<temp2)
				{
					cheats+=temp1;
					sum = temp3 + temp3 - 1  + arr[i];
				}
				else
				{
					cheats+=temp2;
					break;
				}
			}
			//cout<<sum<<" " <<cheats<<endl;
		}
		out<<cheats<<endl;
		//system("pause");
	}
	system("pause");
	return 0;
}