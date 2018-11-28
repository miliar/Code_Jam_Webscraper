#include <iostream>
using namespace std;
 
int main() {
int N, T, i, j, temp, flag, arr[10];
	float k;
	cin>>T;
	for(i=0; i<T; i++)
	{
		for(j=0; j<10; j++)arr[j]=0;
		cin>>N;
		for(k=0; k<1000000; k++)
		{
			temp=N*(k+1);
			flag=1;
			while(temp!=0)
			{
				arr[temp%10]=1;
				temp/=10;
			}
			for(j=0; j<10; j++)
			{
				if(arr[j]==0)flag=0;
			}
			if(flag==1)break;
		}
		if(flag==1)
			cout<<"Case #"<<i+1<<": "<<N*(k+1)<<endl;
		else
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
	}
	return 0;
}