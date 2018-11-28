#include <iostream>
#include <fstream>
int arr[1000001];
 
bool isPalindrome(int n)
{
    int t = n;
        int c = 0;
        
        while( n > 0 )
        {
                c *= 10;
                c += n % 10;
                n /= 10;
        }
        
        return c == t;
}
 
using namespace std;
 
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
   	freopen("out.out","w",stdout);
        for(int i = 1; i <= 1000; ++i)
                if( isPalindrome(i) && isPalindrome( i * i ) )
                        arr[ i * i ] = 1;
                        
        int TC;
        cin >> TC;
        
        for(int j = 0; j < TC; ++j)
        {
                int A, B;
                cin >> A >> B;
                
                int res = 0;
                
                for(int i = A; i <= B; ++i)
                        res += arr[i];
                        
                cout << "Case #" << j + 1 << ": " << res << endl;
        }
        
        return 0;
}
 
