#include<iostream>

using namespace std;

int main()
{
	int i , j , A[4][4] , B[4][4] , N , N1 , N2 ,flag=0 , val ;
	int ans[100];

	cin>>N; //Number of test cases

   for(int n=1;n<=N;n++)
   {
	//cout<<"1. Which Row? :";

	cin>>N1;N1--;

	//cout<<"\nFirst Arrangement : \n";

	for( i=0;i<4;i++ )

	{
		for( j=0;j<4;j++ )
		cin>>A[i][j];
	}

	/* Displaying
	for( i=0;i<4;i++ )

	{
		cout<<"\n";
		for( j=0;j<4;j++ )
		cout<<A[i][j]<<" ";
	} */

	// cout<<"\n2. Which row? :" ;

	cin>>N2;N2--;

	//cout<<"\nSecond Arrangement : \n";

	for( i=0;i<4;i++ )

	{
		for( j=0;j<4;j++ )
		cin>>B[i][j];
	}

	for( i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		  {
			if(A[N1][i]==B[N2][j])
			{
				val=B[N2][j];
				flag++;
			}
		  }
	}

	if(flag==1)
	cout<<"Case #"<<n<<": "<<val;

	else if(flag>1)
	cout<<"Case #"<<n<<": "<<"Bad magician!";

	else if(flag==0)
	cout<<"Case #"<<n<<": "<<"Volunteer cheated!";
    cout<<"\n";
    flag=0;
   }
return 0;
}