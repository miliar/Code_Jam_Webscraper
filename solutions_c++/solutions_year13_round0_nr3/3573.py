#include <iostream>
#include <fstream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>  

#define MAX 100
using namespace std;

bool isPalindrome(long long x)
{
	int length=0;
	short ar[101];
	long long temp=x;
	while(temp)
	{
		ar[length]=temp%10;
		length++;
		temp/=10;
	}
	for(int i=0;i<length;i++)
		if(ar[i]!=ar[length-i-1])
			return 0;
	return 1;
}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

//	FILE * input;
//	input = fopen("input.txt","r");
//	 srand (time(NULL));
	int t;

	unsigned long long a,b;
//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input>>t;// cout<<n<<endl;
	
	unsigned long long left,right;
	int ans=0;

//	 cout<<--l;
//	input>>a>>b;
	 for(int k=0;k<t;k++)
	 {
		 ans=0;
		 input>>a>>b;
		 left=sqrt(a);
		 if(left*left<a)
			 left++;
		 right=sqrt(b);
		 
//		 cout<<"left = "<<left<<" right = "<<right<<endl; 
//		 cout<<k<<endl;

		 for(unsigned long long i=left;i<=right;i++)
			 if(isPalindrome(i))
				 if(isPalindrome(i*i))
				 {
					 ans++;
//					 cout<<i<<' '<<i*i<<endl;
				 }
	//			 cout<<endl;


		output<<"Case #"<<k+1<<": "; 
		output<<ans;
		
		output<<endl;
	 }
	
//	fclose(input);
	input.close();
	output.close();
//	system("pause");
	return 0;
}
