#include<iostream>
#include<fstream>
using namespace std;

unsigned long long arr[200];
int length=0, counter;

int operate ( int i, int l )
{
	//cout<<"Entered func at val "<<i<<endl; getchar();
	int diff=l-i-1;
	int store=diff;
	//cout<<"diff="<<diff<<endl; getchar();
	unsigned long long num=arr[i];
	while ( diff-- )
	{
		num+=(num-1);
	//	cout<<"num="<<num<<endl; getchar();
		if ( num>arr[i+1] ) break;
	}
	
	//cout<<"diff="<<diff<<endl; getchar();

	int j, k;
	if ( diff>0 )
	{
		diff=store-diff;
		for ( j=l-1; j>i; j-- )
		{
			arr[j+diff]=arr[j];
		}
		
		num=arr[i];
		for ( k=i+1; k<=i+diff; k++ )
		{
			//cout<<"h";
			num+=(num-1);
			arr[k]=num;
		}
		//cout<<"hellO";	
		length+=diff;
		counter+=(diff-1);

		//cout<<"New array"<<endl; for ( j=0; j<length; j++ ) cout<<arr[j]<<" "; cout<<endl; getchar();
		return diff;
	}
	else
	{
		length-=(l-i-1);

		return (l-i-1);
	}
}

void sort ()
{
	for ( int i=length-1; i>1; i-- )
	{
		for ( int j=1; j<i; j++ )
		{
			if ( arr[j]>arr[j+1] )
			{
				arr[j]+=arr[j+1];
				arr[j+1]=arr[j]-arr[j+1];
				arr[j]-=arr[j+1];
			}
		}
	}
}


int main()
{
	ofstream out ("A.text");
	int tcases, i, j, k;
	cin>>tcases;
	unsigned long long A;
	int N, casenum=1;
	while ( tcases-- )
	{
		cout<<"Case "<<casenum<<endl;
		cin>>A>>N;
		length=N+1;
		arr[0]=A;
		for ( i=1; i<=N; i++ )
			cin>>arr[i];
		sort();
		//cout<<"Array "<<endl; for ( i=0; i<length; i++ ) cout<<arr[i]<<" "; cout<<endl; getchar();

		int total=0;
		for ( counter=0; counter<length; counter++ )
		{
			if ( arr[counter]>arr[counter+1] )
			{
				arr[counter+1]+=arr[counter];
				continue;
			}
			else total+=operate(counter,length);
		}
		out<<"Case #"<<casenum<<": "<<total<<endl;
		casenum++;
	}



	return 0;
}