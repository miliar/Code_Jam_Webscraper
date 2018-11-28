#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T ;
    cin >> T ;
    for(int n(1); n <= T ; n++){ // Nombre de cas

        long int N ; // L'Entier N
        cin >> N ;
        vector<int> tabEntier ; // Ce tableau reçoit les chiffres
        tabEntier.push_back(10); // Juste pour initialiser le vector

        if(N==0)
            cout << "Case #" << n << ":" << " INSOMNIA" << endl ;
        else{

            int i(1) ;
            long int Z ;
            Z = N ;
        while(tabEntier.size() < 11 ) {
           long int A ;
            Z = i*N ;
            A = Z ;
             int mod ;
            while(A!=0){
                mod = A%10 ;
                A = (A-mod)/10;
                bool s(false) ;
                unsigned int z(1);
                while(z < tabEntier.size()){
                    if(mod==tabEntier[z])
                        s=true ;
                    z=z+1 ;
                }
            if(s==false){
                tabEntier.push_back(mod);
            }
        }
        i=i+1 ;
        }
        cout << "Case #" << n << ": " << Z << endl ;
        }
    }
    return 0;
}
