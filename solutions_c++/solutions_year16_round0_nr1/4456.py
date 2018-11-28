#include <iostream>
using namespace std;

void clear(bool* arr)
{
	for(int i=0;i<10;i++)
	arr[i]=0;
}
bool checkForNumbers(bool* arr)
{
	int i;
	for(i=0;i<10;i++)
	{
		if(arr[i]!=1)
		  break;
	}
	if(i==10)
	  return false;
	return true;
	
}

int main() {
	// your code goes here
	int t,n;
	bool arr[10];
	clear(arr);
	
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA\n";
			continue;
		} 
		 int k=n;
		 int j=n;
		 
		do
		{
		  while(j!=0)
		  {
		  	arr[j%10]=1;
		  	j=j/10;
		  }
		  k=k+n;
		  j=k;
		}while(checkForNumbers(arr));
		
	cout<<"Case #"<<i<<": "<<j-n<<"\n";
		  k=1;
		  clear(arr);
	}
}


