#include <fstream>
#include <iostream>
#include <cmath>

using namespace std;

int isPalindrome(int);

int main()
{
	int N;
	ifstream fi("C-small-attempt0.in");
	ofstream fo("output.txt");
	
	if(!fo || !fi)
		cout<<"File did not open!";

	fi>>N;
	double n = 1, i, j, A, B, count;
	float isFloat;
	
	while(n<=N)
	{
		fi>>A>>B;    
		count = 0;
		      
		for(i=A ; i<=B ; i++)
			if(isPalindrome(i))
			{
				isFloat = sqrt(i) - (int)sqrt(i);
				if(!isFloat)
					if(isPalindrome(sqrt(i)))
						count ++;

			}

		fo<<"Case #"<<n<<": "<<count<<endl;
		
		n++;	

	}
		
	fi.close();
	fo.close();	

	return 0;

}

int isPalindrome(int num)
{
	int rev = 0,temp = num;
		
	while(temp) 
	{ 

		rev *= 10;
		rev += temp%10;
		temp /= 10;
		
	}

	if(rev == num)
		return 1;
	else
		return 0;
	
}
