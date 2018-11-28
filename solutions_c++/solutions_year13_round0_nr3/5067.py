#include <iostream>
#include <math.h>
using namespace std;
int isPalindrome(long);

int main()
{
  int noOfTestCases;
  
 
  cin>>noOfTestCases;
  for(int k=1; k<=noOfTestCases; k++)
  {
    int low;
    int high;
    cin>>low>>high;
    float j,m;
    m=sqrt(low);
    j=ceil(m);
    int i=(int)j;
    int count=0;
    
    	while((i*i)<=high)
        {
          int chek=isPalindrome(i);
          	if(chek==1)
            {
              int j=i*i;
              int chek1=isPalindrome(j);
              if(chek1==1)
                count++;
            }
          i++;
        }
    
    cout<<"Case #"<<k<<": "<<count<<"\n";
     
    
  }//end of outermost for loop
  
  
  
  
  
   return 0;
}

int isPalindrome(long number) {
		long palindrome = number; 
		long reverse = (long)0;
		if(number ==0)
			return false;
		while (palindrome != 0) {
			long remainder = palindrome % 10;
			reverse = reverse * 10 + remainder;
			palindrome = palindrome / 10;
		}

		
		if (number == reverse) {
			return 1;
		}
		return 0;
	}

   