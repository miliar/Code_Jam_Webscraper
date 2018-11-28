#include<iostream>
#include<cstring>
#include<fstream>
#include<iomanip>
#include<algorithm>

using namespace std;

bool myfunction (double i,double j) { return (i<j); }
int main()
{
	int T;
	ifstream f;
	ofstream f2;
	int i,j,k;
  	f.open ("D-large.in");
	f2.open("D-large.out");
	
	f>>T;
	double naomi[1000];
	double ken[1000];
	int N;
	int war, d_war;
	int done=0;
	double temp;
	int m,n;
	int count;
	for( i=0; i<T; i++ )
	{
		f>>N;
		for( j=0; j< N; j++ )
			f>>naomi[j];
		
		for( j=0; j<N; j++ )
			f>>ken[j];
	
		//sort naomi and ken array
		for( m=0; m<N; m++)
		{
			for( n=0; n<N-m-1; n++ )
			{
				if( naomi[n]>naomi[n+1])
				{
					temp = naomi[n+1];
					naomi[n+1] = naomi[n];
					naomi[n] = temp;
				}
				if( ken[n] > ken[n+1])
				{
					temp = ken[n+1];
					ken[n+1] = ken[n];
					ken[n] = temp;
				}
			}
		}
		//war
		count =0;
		m = 0;
		n=0;
		done= 0;
		while( n < N && done==0)
		{
			while( (naomi[n] > ken[m]) && m<N )
				m++;
			if( (naomi[n] < ken[m]) && m<N)
			{
				count++;
				m++;
			}
			if( m>N-1 )
				done =1;
			//cout<<n<<" "<<m-1<<endl;
			n++;
		}
		war=N-count;
		//d_war
		count =0;
		m = N-1;
		n=N-1;
		done= 0;
		while( n > -1 && done==0)
		{
			while( (naomi[n] < ken[m]) && m > -1 )
				m--;
			if( (naomi[n] > ken[m]) && m>-1)
			{
				count++;
				m--;
			}
			if( m < 0 )
				done =1;
			n--;
		}
		d_war=count;
		
		f2<<"Case #"<<(i+1)<<": "<<d_war<<" "<<war<<endl;
							
	}
	f.close();
	f2.close();	



	return 0;
}
