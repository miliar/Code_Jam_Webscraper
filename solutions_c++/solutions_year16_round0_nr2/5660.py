#include <iostream>
#include <fstream>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#define ll long long int
#define li long int

using namespace std;

int main()
{
	ifstream fin("B-large.in");
    ofstream fout("large-output.out");
	
	ll t, l;
	fin >> t;
	for(l = 1; l <= t ; l++)
	{
		char s[105] = {'\0'}, set, cur ;
		bool flag = 0 ;
		fin >> s ;
		ll i, len, j, count = 0;
		len = strlen(s) ;
		while(!flag){
			
			if(s[0] == '+'){
				cur = '+'  ;
				set = '-' ;
			}	
			else{
				cur = '-'  ;
				set = '+' ;	
			}
			
			if(len == 1){
				flag = 1;
				break ;
			}
			for(i = 1 ; i < len ; i++){
				
				if(s[i] != cur)
				{
					flag = 0;
					count++;
					for(j = 0 ; j < i ; j++)
					{
						s[j] = set ;
					}					
					break ;
				}
				else flag = 1 ;
			}
		}
		
		if(flag && cur =='+')	fout << "Case #" << l << ": " << count << endl ;
		else	fout << "Case #" << l << ": " << count+1 << endl ;
	}
}

