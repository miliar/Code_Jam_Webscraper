/*
	Author : Subhasis Dutta
*/
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

bool is_palindrome(int n)
{
	int reverse=0;
	int temp = n;
    while( temp != 0 )
 	{
      reverse = reverse * 10;
      reverse = reverse + temp%10;
      temp = temp/10;
    }
    if(reverse==n)return true;
    else return false;
}
bool is_perfectSquarePalindrome(int n)
{
	if (n < 0)
        return false;
    double d_sqrt = sqrt(n);
	int i_sqrt = d_sqrt;
	if ( d_sqrt == i_sqrt ){
		//cout<<d_sqrt<<" ";
		if(is_palindrome(i_sqrt))return true;
		else return false;
	}
	else{
		return false;
	}    
}
int main()
{
	ofstream fout ("FairandSquare.out");
	ifstream fin ("FairandSquare.in");
	int T;
	fin>>T;
	for(int i=0;i<T;i++){
		int a;
		int b;
		int count=0;
		fin>>a;
		fin>>b;
		for(int j=a;j<=b;j++){
			if(is_palindrome(j)){
				//fout<<j<<" ";
				if(is_perfectSquarePalindrome(j)){
					//fout<<j<<" ";
					count++;
				}
			}
		}
		fout<<"Case #"<<i+1<<": ";
		fout<<count<<endl;
	}
	fout<<endl;
	return 0;
}
