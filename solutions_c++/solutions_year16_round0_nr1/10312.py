#include<iostream>
#include<limits>

using namespace std;

int list[] = {0,1,2,3,4,5,6,7,8,9};

int mylist[] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};



void check(int product)
{
	int num;
	
	while(product > 0)		
	{
		num = product % 10	;
		mylist[num] = num;
		product = product/10;		
		cout<<"";
	}
}

int match()
{
	for(int i=0; i<10; i++)
	{
		if(mylist[i]!=list[i])	
		return 0;
	}
	
	return 1;
}

int count(long int N)
{
	int i=1;
	long int product;
	
	
	while(product <= std::numeric_limits<long>::max() && i<=1000)
	{
		product = N*i; 		
		i++;
		
		check(product);
			
		if(match() == 1)
		return product;
		
		
	}
}

int main()
{
	int T;
	long int N[100];
	int flag=1;
	
	cin>>T;
	
	for(int i=0; i<T ; i++)
	{
		cin>>N[i];	
	}
	
	for(int j=0; j<T; j++)
	{
		N[j]=count(N[j]);
		
		
		for(int y=0; y<10; y++)
		if(mylist[y]==-1)
		{flag=0;break;}
		
		if(flag==0)	
		cout<<"Case #"<<j+1<<": "<<"INSOMNIA"<<endl;
		
		else
		cout<<"Case #"<<j+1<<": "<<N[j]<<endl;
		
		for(int a=0; a<10; a++)
		mylist[a]=-1;
		flag=1;
	}
	

	
	
	return 0;
}
