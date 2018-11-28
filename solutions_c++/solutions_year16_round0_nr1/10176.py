#include <bits/stdc++.h>

using namespace std ;

int main(){
    long long tc , n ;
    cin >> tc;
    for(int i = 1 ; i <= tc ; i++){
        cin >> n ;
        if(n == 0){
            cout << "Case #" << i << ": " << "INSOMNIA" << endl ;
            continue ;
        }
        vector <int> Dig(10) ;
        long long t = 0 ;
        while(true){
            t++ ;
            long long n1 = t * n ;
            while(n1)
                Dig[n1 % 10] = 1 , n1 /= 10 ;

            int Cnt = 0 ;
            for(int j = 0 ; j < 10 ; j++){
                if(Dig[j])
                    Cnt++ ;
            }
            //cout << Cnt << endl ;
            if(Cnt == 10){
                cout << "Case #" << i << ": " << n * t << endl;
                break ;
            }
        }
    }

    return 0 ;
}
