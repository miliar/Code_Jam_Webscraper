#include <cstdio>
#include <cmath>
using namespace std;



long long get_number(int num[], int n){
    long long out = 0;
    for(int i=0; i<n; ++i){
        out *= 10;
        out += num[i];
    }
    return out;
}

void num_to_Array(int num[], long long n, int * size_n){
    int s = 0 , n_copy = n;
    while(n_copy){
        n_copy /= 10;
        ++s;
    }
    *size_n = s;
    for(int i = s-1; i >= 0; --i){
        num[i] = n % 10;
        n /= 10;
    }
}

bool check_palindrome(int num[], int n){
    int mid = n/2;
    for(int i=0; i<= mid; ++i){
        if(num[i] == num[n-1-i])
            continue;
        else
            return false;
    }
    return true;
}

bool check_palindrome_and_square(int num[], int n, long long lower, long long upper){
    long long sqrt_a = get_number(num,n), a;
    a = sqrt_a * sqrt_a;
    if(a >= lower && a<= upper){
        int num_sqare[16] , size_square;
        num_to_Array(num_sqare, a, &size_square);
        return ( check_palindrome(num,n) && check_palindrome(num_sqare, size_square) );
    }
    return false;
}



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
    int mid = n/2;
    bool leftsmaller = false;

    int i = mid - 1;
    int j = (n % 2)? mid + 1 : mid;

    while (i >= 0 && num[i] == num[j])
        i--,j++;

    // Find if the middle digit(s) need to be incremented or not (or copying left
    // side is not sufficient)
    if ( i < 0 || num[i] < num[j])
        leftsmaller = true;

    // Copy the mirror of left to tight
    while (i >= 0)
    {
        num[j] = num[i];
        j++;
        i--;
    }

    // Handle the case where middle digit(s) must be incremented.
    // This part of code is for CASE 1 and CASE 2.2
    if (leftsmaller == true)
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
int generateNextPalindrome( int num[], int n )
{
    int i;
    if( AreAll9s( num, n ) ) {
        num[0] = 1;
        for( i = 1; i < n; i++ )
            num[i] = 0;
        num[n] = 1;
        return 1; // meaning array size increased;
    }
    else {
        generateNextPalindromeUtil ( num, n );
        return 0;
    }

}





int main(){
    int t;
    long long a,b;
    scanf("%d",&t);
    for(int i=0; i<t; ++i){
        int num_a[16], num_b[16], len_a, len_b;
        scanf("%lld %lld",&a, &b);
        long long sqrt_a =sqrt(a);
        long long sqrt_b =sqrt(b)+1;

        num_to_Array(num_a, sqrt_a, &len_a);
        num_to_Array(num_b, sqrt_b, &len_b);

        long long total = 0;
        while( get_number(num_a, len_a) <= sqrt_b ){

            if ( check_palindrome_and_square(num_a, len_a, a, b) ){
                //printf("Sqrt Numbers found = %lld\n", get_number(num_a, len_a) );
                total++;
            }
            len_a += generateNextPalindrome(num_a, len_a);
        }
        printf("Case #%d: %lld\n",i+1,total);


    }

}
