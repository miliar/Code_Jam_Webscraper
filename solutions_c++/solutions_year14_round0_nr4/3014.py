#include<bits/stdc++.h>
using namespace std;
int war ( float n[], float k[], int num )
{	
	int kt=0 , kb =num-1 ,ns =0;
	for(int i=num-1; i>=0 ; i-- )
	{
		if( n[i] > k[kb] )
		{
			ns++;
			kt++;
		}
		else
		{
			kb--;
		}
	}
	return ns;
}

int dwar ( float n[], float k[], int num )
{
	
	int kt =0, kb= num-1, nt=0, nb = num-1 ,ns=0;
	while ( nb !=nt  ) 
	{
		if( n[nt] > k[kt] )
		{
			ns++;
			nt++;
			kt++;
		}
		else
		{
			nt++;
			kb--;
		}
	}
	if( n[nb] > k[kb] )
	{
		ns++;
		nb--;
		kt++;
	}
	else
	{
		nt++;
		kb--;
	}
	return ns;
	
}
int main()
{
	freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
	float n[1000] ={0} ,k[1000] ={0} ;
	int test =0 ,num=0; 
	cin>>test;
	for(int t=1 ; t<=test ; t++ )
	{
		cin>>num;
		for( int i =0 ;i < num ;i++ )
		{
			cin>> n[i];
		}
		for( int i = 0; i< num ;i++ )
		{
			cin >> k[i];
		}
		sort ( n, n+num) ;
		sort ( k, k+num) ;
		/*
		//------outputs--------
		for( int i =0 ;i < num ;i++ )
		{
			cout<< n[i] << " ";
		}
		cout<< endl;
		for( int i = 0; i< num ;i++ )
		{
			cout<< k[i] << " ";
		}
		cout<<endl;
		//--outputs end ---------
		 */
		int wars = war( n, k, num);
		int dwars = dwar ( n, k, num);
		cout<<"Case #"<<t<<": "<< dwars<<" " << wars <<endl; 
	}
}
