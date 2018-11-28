#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
bool isPalin(int n)
{
	int digit,rev,num;
	rev=0;	
	num=n;
	do
     	{
         	digit = num%10;
         	rev = (rev*10) + digit;
         	num = num/10;
     	}while (num!=0);
     
     if (n == rev)
       return true;
     else
       return false;
                  
}
bool isSq(int n)
{
	float p;
	int m;
	p = sqrt(n) ;   
 	m = p ;   
 	if (p == m)  
		return true;
	return false;
}
int main()
{
	ofstream fout;
	fout.open("output1.txt");
	int T;
	int A,B;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int count =0;
		cin >> A >> B;
		for(int j = A; j <=B; j++)
		{
			if(isPalin(j)&&isSq(j)&&isPalin(sqrt(j)))
			{
				count++;
				//cout << "No is : " << j << endl;
			}
		}
		fout << "Case #" << i+1 << ": " << count << endl;
	}
}
