#include <iostream>
using namespace std;
int arr[10]={0,1,2,3,4,5,6,7,8,9};
int func(int num)
{
  while(num>0)
	{
		arr[num%10]=-1;
		num=num/10;
	}
  for(int i=0;i<10;++i)
  {
	if(arr[i]!=-1)
	return 0;
  }
  return 1;
}
int main() {
	
	int t,j;
	long int n;
	int flag;
	cin>>t;
	for(int i=0;i<t;++i)
	{
		flag=0;
		j=1;
		cin>>n;
		while(flag!=1)
		{
			if(n==0)
			{
				cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
				flag=1;
			}
			else
			{

				flag=func(j*n);
				++j;
			}
		}
		if(n!=0)
		cout<<"Case #"<<i+1<<": "<<(j-1)*n<<endl;
		for(int k=0;k<10;++k)
		arr[k]=k;
	}
	return 0;
}
