#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T,n,rate;
    long long int sum;
    long long int eaten1;
    cin >> T;
    for(int i = 1;i<=T;++i){
        eaten1 = 0;
        sum = 0;
        int n,rate,max_rate=0;  
        cin >> n;
        int A[n];
        int t = n-1;
        cin >> A[0];
        for(int j= 1;j<t;++j){    
            cin >> A[j];
            rate = A[j-1] - A[j]; 
            if(rate > max_rate) max_rate = rate;     
            if(A[j]<A[j-1]){           
                eaten1+=(rate);
            }
        }
        cin >> A[t];
        if((A[t-1] - A[t]) > max_rate) max_rate = A[t-1] - A[t];        
        for(int j = 0;j<t;++j){
            if(A[j] <= max_rate) sum+=A[j];
            else             sum+=max_rate;
        }     
        if(A[t] < A[t-1]) eaten1+=(A[t-1] - A[t]);
        cout << "Case #" << i << ": " << eaten1 << " " << sum << "\n";
    }
    return 0;
}
