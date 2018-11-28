#include <iostream>
#include <math.h>
#include <fstream>
#define ll long long int
using namespace std ;

void increment(int array[] , int len)
{
    for (int i = len - 2 ; i >= 1 ; i --)
    {
        if (array[i] == 0)
        {
            array[i] = 1;
            return;
        }
        array[i] = 0 ;
    }
}

int is_prime(int div[] , ll n , int base)
{	
	if(n == 2) {
 		return 1 ;
	} else {
		if(n % 2 == 0) {
			div[base - 2] = 2 ;
			return 0 ;
		}
		else {
			for(ll i = 3 ; i * i <= n ; i += 2) {
				if(n % i == 0) {
					div[base - 2] = i ;
					return 0 ;
				}
			}
			return 1 ;
		}
	}
}

ll convert(int arr[] , int n , int base) {
	ll num = 0 ;
	for(int i = n - 1 ; i >= 0 ; i --) {
		num += arr[i] * pow(base , n - 1 - i) ;
	}
	return num ;
}

int main() {
	ifstream din("C-small-attempt0.in") ;
	ofstream dout("o3.txt") ;
	int t ;
	din >> t ;
	for(int i = 1 ; i <= t ; i ++) {
		int n , j ;
		din >> n >> j ;
		dout << "Case #" << i <<":\n" ;
		int arr[n] = {} ;
		arr[0] = 1 ;
		arr[n - 1] = 1 ;
		int count = 0 , check ;
		while(count != j) {
			check = 0 ;
			int div[9] = {} ;
			if(is_prime(div , convert(arr , n , 2) , 2) == 0) {
				check ++ ;
				for(int k = 3 ; k <= 10 ; k ++) {
					if(is_prime(div , convert(arr , n , k) , k) == 0)
						check ++ ;
					else 
						break ;
				}
				if(check == 9) {
					count ++ ;
					dout << convert(arr , n , 10) ;
					for(int m = 0 ; m < 9 ; m ++)
						dout << " " << div[m] ;
					dout << endl ;
				}
			} 
			increment(arr , n) ;	
		}
	}
	return 0 ;
}
