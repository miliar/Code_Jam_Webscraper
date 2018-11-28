#include<iostream>
#include<fstream>
#include<cmath>


using namespace std;
int J=0;
fstream fil;
int modpow(int a,int b,int mod)
{
    int product,pseq;
    product=1;
    pseq=a%mod;
    while(b>0)
    {
        if(b&1)
            product=(product*pseq)%mod;
        pseq=(pseq*pseq)%mod;
        b>>=1;
    }
    return product;
}
void checkstring(int arr[],int N)
{

	bool cont=true;
	long long int ans[9]={0},count=0;
	for(int i=2;i<=10;i++)
	{
		if(cont)
		{
			//for(long long int j=2;j<pow(i,(N+1)/2);j++)
			for(long long int j=2;j<1000;j++)
			{
				int tmp=N;
				long long int sum=0;
				while(tmp>=0)
				{
					sum+=(int)fmod(arr[N-tmp]*pow(i,tmp),j);		
					tmp--;
				}
			
				if(fmod(sum,j)==0)
				{
				  count++;
				  ans[i-2]=j;
				  break;
				}
				
				else if(j==pow(i,(N+1)/2)-1)
				cont=false;
			}
		}
			
	}
	
	if(count==9)
	{
		J--;
		for(int i=0;i<=N;i++)
		{
			cout<<arr[i];
			fil<<arr[i];
		}
		for(int i=0;i<9;i++)
		{
			cout<<" "<<ans[i];
			fil<<" "<<ans[i];
		}
		cout<<endl;
		fil<<"\n";
	}
}

void rec(int arr[],int x,int N)
{
	if(x==0)
	checkstring(arr,N);
	
	else if(J)
	{
			//case 0
		arr[x]=0;
		rec(arr,x-1,N);
		
		if(J)
		{
			//case 1
		arr[x]=1;
		rec(arr,x-1,N);
		}
			
	}
	
	
}
int main()
{
	
	fil.open("C:\\Users\\vaibhav\\Desktop\\JAM3out.txt");
	int T;
	cin>>T;
	while(T)
	{
		int N;
		cin>>N>>J;
		int num[N]={0};
		num[N-1]=num[0]=1;
		
			cout<<"Case #1:\n";
			fil<<"Case #1:\n";
			rec(num,N-2,N-1);
			
		
		T--;
	}
	fil.close();
}
