#include <iostream>
#include <cmath>
using namespace std;


int check_square(int n)
{
	int n2=sqrt(n);
	return (n2*n2)==n;

}

int palindrome(int n){
	int length=0;int temp=n;
	while(n!=0){n/=10;length++;}
	int rev=0;n=temp;
	while(n!=0){
	rev *= 10; rev+= n%10; n/=10;
	}
	n=temp;
	return rev==n;
}

int main ()
{
	int T;int casenum=1, tempans,temp;
	cin>>T; 
	int Pm[1002], Pc[1002];

	for (int i = 1; i < 1002; i += 1)
	{
		Pm[i]=1;Pc[i]=1;
	}

//	for (int i = 1; i < 5; i += 1)
//	{
//			cout<<Pm[i];
//	}

	for (int i = 1; i < 1002; i += 1)
	{
		if(!palindrome(i)){Pm[i]=0;Pc[i]=0;}
	}

//	for (int i = 1; i < 5; i += 1)
//	{
//			cout<<Pm[i];
//	}	

	for (int i = 1; i < 1002; i += 1)
	{
		if(Pm[i]==1 && !check_square(i)){Pm[i]=0;}
	}

//	for (int i = 1; i < 5; i += 1)
//	{
//			cout<<Pm[i];
//	}

	for (int i = 1; i < 1002; i += 1)
	{
		if(Pm[i]==1 && Pc[(int)sqrt(i)]==0){Pm[i]=0;}
	}	

//	for (int i = 1; i < 5; i += 1)
//	{
//			cout<<Pm[i];
//	}

	for (int i = 2; i < 1002; i += 1)
	{
		Pm[i]+=Pm[i-1];
	}

	Pm[0]=0;
	int A,B;

	while(T!=0){

	cin>>A>>B;
//	int a=0;
//	for(int i=A;i<=B;i++){
//	a+=Pm[i];
//	}
	cout<<"Case #"<<casenum<<": "<<Pm[B]-Pm[A-1]<<"\n";
	//cout<<palindrome(T);
		
	T--;casenum++;
	}
	return 0;
}

