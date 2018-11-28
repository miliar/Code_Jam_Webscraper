#include<iostream>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<vector>
using namespace std;
int find(long int );
bool isPrime(long int);
void divisor(long int arr[]);
int main()
{
	int n,j,t;
	std::cin>>t>>n>>j;
	int count=0;
	int count1=count;
	int flag=pow(2,n-2);
	cout<<"Case #1:";
	while(j--)
	{
		flag--;
		int row=pow(2,n-2);
		char str_dec[n];
	 	//string::size_type sz;   // alias of size_t
		str_dec[0]='1';
		str_dec[n-1]='1';
		for(int i=1;i<n-1;i++)
		{
			row=row/2;
			//cout<<"ROW : "<<row<<endl;
			if((count%(row*2))<row)
			{
				str_dec[i]='0';
			}
			else
			{
				str_dec[i]='1';
			}
			
			
		}
		count=count+1;
		//std::cout<<str_dec<<endl;
		long int i_dec = atol (str_dec);
		//cout<<i_dec;
		if(flag==0)
		{
			break;
		}
		if(find(i_dec)==1)
		{
			j++;
		}
	}
	return 0;
}
int find(long int i_dec)
{
	long int arr[9]={0};
	for(int i=2;i<11;i++)
	{
		long int sum=0,num=i_dec,rem=0;
		int count=0;
		while(num!=0)
		{
			
			rem=num%10;
			num=num/10;
			if(rem!=0)
			{
				sum=sum+rem*pow(i,count);
			}
			count++;
		}
		if(isPrime(sum)==true)
		{
			//cout<<"NUMBER IS PRIME"<<endl;
			return 1;
		}
		arr[i-2]=sum;
		//cout<<"sum : "<<sum<<endl;
	}
	//cout<<i_dec<<endl;
	cout<<endl<<i_dec;
	divisor(arr); 
	/*for(int i=0;i<9;i++)
	{
		cout<<"sUM : "<<arr[i]<<endl;
	}*/
	return 0;
}
bool isPrime(long int number){

    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(long int i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) return false;
    }
    return true;

}
void divisor(long int arr[])
{
	for(int j=0;j<9;j++)
	{
		for(int i=2;i<arr[j];i++)
		{
			if(arr[j]%i==0)
			{
				cout<<" "<<i;
				break;
			}
		}
	}
}
