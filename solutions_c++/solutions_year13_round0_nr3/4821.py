#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;
#define SMALL
//#define LARGE

bool is_palindrome(int num){
     int rev =0, digit;
     int n = num;
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

bool is_perfect_square_of_palindrome(int num){
     int i=1;
     bool return_val;
     do{
	int square_val = i * i;
	if(square_val == num && is_palindrome(i) == true){
		return_val = true;
		break;
	}
	else
		return_val = false;
	i++;
     }while(i <= num/2 || num == 1);
     return return_val;
}

int main(){
    FILE *fp, *fpout;
    int T,A,B;
    
#ifdef SMALL    
    freopen("C-small-0.in", "rt", stdin);
    freopen("C-small-0.out", "wt", stdout);
#endif    

#ifdef LARGE    
    freopen("C-large-0.in", "rt", stdin);
    freopen("C-large-0.out", "wt", stdout);
#endif    

    cin >> T;

    for(int cur =0;cur < T; cur ++){
    	cin >> A >> B;
	int count = 0;
	if(A == 0) 
		A++;
	for(int i = A; i <= B; i++){
		if(is_palindrome(i) == true && is_perfect_square_of_palindrome(i)){
			count++;
		}
	}
	cout << "Case #" << cur+1 << ": " << count << endl;
    }
    
    return 0;
}

