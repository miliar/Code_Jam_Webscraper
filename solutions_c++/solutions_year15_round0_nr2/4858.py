#include <iostream>
#include <algorithm>
using namespace std ;
int a[1000] ;
int t, D, max1 = 0, min1 = 0, sum = 0;
int count_max()
{
    min1 = max1;
    for(int i = 1; i <= max1; i++) 
    {
        sum = i ;
        for(int j = 0; j < D; j++) 
        {
            if(a[j] < i)
                continue;
            if( a[j]%i == 0 )
                sum += (a[j]/i-1) ;
            else
                sum += (a[j]/i) ;
        }
        min1 = min(min1,sum) ;
    }
}
int main(int argc, char **argv) {
    int step = 0 ;
    cin >> t;
    while(t--) {
        cin >> D;
        for(int i = 0; i < D; i++) 
        {
            cin >> a[i];
            if(a[i] > max1)
            	max1 = a[i];
        }
        count_max();
        step ++;
        fill_n(a, D, 0);
        cout << "Case #"<< step << ": " << min1 << endl;
    }
    return 0 ;
}
