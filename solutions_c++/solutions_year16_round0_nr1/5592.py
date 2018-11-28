#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdbool.h>
#define ll long long int
#define li long int

using namespace std;

int main()
{
	ifstream fin("input.in");
    ofstream fout("output.out");
	
	ll t;
	fin >> t;
	for(ll l = 1; l <= t ; l++)
	{
		bool hsh[10] = {0}, flag = 0;
		ll n, num, j = 1, i, disp ;
		fin >> n ;
		
		if(n == 0)
			fout << "Case #" << l << ": " << "INSOMNIA\n" ;
		else
		{
			while(!flag){
				
				num = j*n ;
				disp = num ;
				while(num!=0){
					hsh[num%10] = 1;
					num /= 10;
				}
				for(i = 0 ; i < 10 ;)
				{
					if(hsh[i] == 1)
						i++ ;
					else
						break;
				}	
				
				if(i == 10)	flag = 1 ;
				else j++ ;
			}
			fout << "Case #" << l << ": " << disp << endl;
		}
	}
}

