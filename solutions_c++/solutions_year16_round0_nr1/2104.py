#include <iostream>

using namespace std;

bool digs[10];

int fill(int sum) {
    int ndigs = 0;
    
#ifdef _DEBUG
    cout << sum << ": ";
#endif
    
    while(sum > 0){
        int dig = sum%10;
#ifdef _DEBUG
      if(digs[dig] == false)
        cout << " " << dig;
#endif
        digs[dig] = true;
        sum /= 10;
    }
    
    for(int i=0; i < 10; i++)
        ndigs += (digs[i]) ? 1 : 0;

#ifdef _DEBUG
    cout << endl;
#endif

    
    return ndigs;
}

int main()
{
    int T, cont = 0;
    
    cin >> T;

    while(T--)
    {
        int n;
        
        cin >> n;
//     for(int n = 0; n <= 100000; n++) {
        
        for(int i = 0; i < 10; i++)
            digs[i] = false;
        
        if(n == 0) {
            cout << "Case #" << ++cont << ": " << "INSOMNIA" << endl;
            continue ;
        }

        int sum = n, ndigs = 0;
        for( ;  ; ) {
            ndigs = fill(sum);
            if(ndigs == 10)
                break ;
            
            sum += n;
        }
        
        cout << "Case #" << ++cont << ": " << sum << endl;
    }
        
return 0;
}
