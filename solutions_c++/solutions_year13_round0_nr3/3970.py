#include <iostream>
#include <cmath>
using namespace std;
int checkpalindrome(int );
int main()
{

	int i,j,test_cases, test_cases1,start,end;
    cin>>test_cases;
    test_cases1 = test_cases;
    while(test_cases--){
	j=0;
	cin>>start>>end;
    for(i=start;i<=end;i++)
    {
    	if((int)sqrt(i)*(int)sqrt(i)==i && checkpalindrome(i) && checkpalindrome((int)sqrt(i)))
    	 {
    	 	j++;
    	 }
    }
    cout<<"Case #"<<test_cases1 - test_cases<<": "<<j<<"\n";
	}

}

int checkpalindrome(int n)
{
	int  rev = 0, temp;

   temp = n;
 
   while( temp != 0 )
   {
      rev *= 10;
      rev += temp%10;
      temp = temp/10;
   }
	
	if(n==rev)
		return 1;
	else return 0;
   
}

