#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
#include<cstring>
#include<cmath>

using namespace std;

int palindrome(long long int n)
{
	char arr[101];
	sprintf(arr,"%lld",n);
	int i,len;
	len = strlen(arr);
	for(int i=0;i<len/2;i++)
	{
		if(arr[i] != arr[len-1-i])
			return 0;
	}
	return 1;
}

// A utility function to check if num has all 9s
int AreAll9s( int* num, int n )
{
    int i;
    for( i = 0; i < n; ++i )
        if( num[i] != 9 )
            return 0;
    return 1;
}

void generateNextPalindromeUtil (int num[], int n )
{
    // find the index of mid digit
    int mid = n/2;
 
    // A int variable to check if copy of left side to right is sufficient or not
    int leftsmaller = 0;
 
    // end of left side is always 'mid -1'
    int i = mid - 1;
 
    // Begining of right side depends if n is odd or even
    int j = (n % 2)? mid + 1 : mid;
 
   // Initially, ignore the middle same digits 
    while (i >= 0 && num[i] == num[j])
        i--,j++;
 
    // Find if the middle digit(s) need to be incremented or not (or copying left 
    // side is not sufficient)
    if ( i < 0 || num[i] < num[j])
        leftsmaller = 1;
 
    // Copy the mirror of left to tight
    while (i >= 0)
    {
        num[j] = num[i];
        j++;
        i--;
    }
 
    // Handle the case where middle digit(s) must be incremented. 
    // This part of code is for CASE 1 and CASE 2.2
    if (leftsmaller == 1)
    {
        int carry = 1;
        i = mid - 1;
 
        // If there are odd digits, then increment
        // the middle digit and store the carry
        if (n%2 == 1)
        {
            num[mid] += carry;
            carry = num[mid] / 10;
            num[mid] %= 10;
            j = mid + 1;
        }
        else
            j = mid;
 
        // Add 1 to the rightmost digit of the left side, propagate the carry 
        // towards MSB digit and simultaneously copying mirror of the left side 
        // to the right side.
        while (i >= 0)
        {
            num[i] += carry;
            carry = num[i] / 10;
            num[i] %= 10;
            num[j++] = num[i--]; // copy mirror to right
        }
    }
}
 
// The function that prints next palindrome of a given number num[]
// with n digits.
long long int generateNextPalindrome( long long int number )
{
    int i;
    
    char cnumber[101];
    sprintf(cnumber,"%lld",number);
    int n = strlen(cnumber);
    int num[n];
    
    for(i=0;i<n;i++)
    	num[i] = int(cnumber[i]-48);
    
    char numarr[n+1];
 
    // Input type 1: All the digits are 9, simply o/p 1
    // followed by n-1 0's followed by 1.
    if( AreAll9s( num, n ) )
    {
        numarr[0] = '1';
        for( i = 1; i < n; i++ )
            numarr[i] = '0';
        numarr[n] = '1';
        numarr[n+1] = '\0';
    }
 
    // Input type 2 and 3
    else
    {
        generateNextPalindromeUtil ( num, n );
 
        // print the result
    	for(i=0;i<n;i++)
    		numarr[i] = char(num[i]+48);
    	numarr[i] = '\0';
    }
    return atoll(numarr);
}

int main()
{
	int T,count,digits;
	char str[101],newj[101];
	long long int A,B,i,j,k,root,square;
	long double rootd;
	
	//ifstream fin("C-small-attempt0.in");
	//ofstream fout("C-small-attempt0.out");
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C-small-attempt1.out");
	
	fin>>T;
	
	for(i=0;i<T;i++)
	{
		count = 0;
		fin>>A>>B;
		
		if(palindrome(A))
			j = A;
		else
			j = generateNextPalindrome(A);
		do
		{
			rootd = sqrtl(j);
			root = (long long int)rootd;
			if(rootd-root == 0 && palindrome(root))
			{
				cout<<j<<" "<<root<<endl;
				count++;
			}
			j = generateNextPalindrome(j);
		}
		while(j <= B);
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
