#include<iostream>
#include<cmath>
using namespace std;


bool isPrime(uint64_t n)
{
	for(uint64_t i= 2; i<= sqrt(n);i++)
		if(n%i==0)
			return 0;
    return 1;
}

uint64_t getVal(int *num,int n, int b)
{
	uint64_t res=0;
	int k=0;
	for(int i= n-1;i>=0;i--)
	{
		res+= pow(b,k)*num[i];
		k++;
	}
	return res;
}

void getNext(int *arr, int n)
{
	uint64_t k= getVal(arr+1,n-2,2);
	k++;
	int i=2;
	while(k)
	{
		if(k&1)
			arr[n-i]=1;
		else
			arr[n-i]=0;
		i++;
		k>>=1;
	}

}

uint64_t getDiv(uint64_t num)
{
	for(uint64_t i= 2; i<= sqrt(num)+1;i++)
		if(num%i==0)
			return i;

   return 0;
}
int main()
{
	int t;
	uint64_t n;
    cin>>t;
    int cnt=1;
    while(t--)
    {
    	cout<<"Case #"<<cnt++<<":"<<endl;
    	int n,j;
    	cin>>n>>j;
    	int arr[n];
    	for(int i=0;i<n;i++)
    		arr[i]=0;
    	arr[0]=1;
    	arr[n-1]=1;

    	while(j)
    	{
    		bool pFlag=0;
    		for(int i=2;i<=10;i++)
    		{
    			if(isPrime(getVal(arr,n,i)))
    			{
    				pFlag=1;
    				break;
    			}
    		}
    		//cout<<"Chkpnt"<<endl;
    		if(!pFlag)
    		{
    			j--;
    			for(int i=0;i<n;i++)
    				cout<<arr[i];
    			for(int i=2;i<=10;i++)
    			{
    				cout<<" "<<getDiv(getVal(arr,n,i));
    			}
    			cout<<endl;
    		}
    		getNext(arr,n);

    	}


    }

}