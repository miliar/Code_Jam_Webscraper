#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int ki=0;ki<T;ki++)
	{
		int n1,n2;
		cin>>n1;
		int arr1[16],arr2[16];
		for(int i=0;i<16;i++)
		cin>>arr1[i];
		cin>>n2;
		for(int i=0;i<16;i++)
		cin>>arr2[i];
		int co=0;
		int cur=17;
		for(int i=4*n1-4;i<4*n1;i++)
		{
			for(int j=4*n2-4;j<4*n2;j++)
			{
				if(arr1[i]==arr2[j])
				{
					cur=arr1[i];
					co++;
				}
				if(co>1)
				break;
			}
			if(co>1)
			break;
		}
		if(co==0)
		cout<<"Case #"<<ki+1<<": Volunteer cheated!"<<endl;
		else if(co==1)
		cout<<"Case #"<<ki+1<<": "<<cur<<endl;
		else
		cout<<"Case #"<<ki+1<<": Bad magician!"<<endl;
	}
	return 0;
}
