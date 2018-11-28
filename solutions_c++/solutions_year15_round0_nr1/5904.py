#include<iostream>
#include<string>

using namespace std;

int main(){
    int T;
    int Smax;
    string str;
    int stoodUP=0;
    int pplwithSHY = 0;
    int pplToinvite;

    cin >> T;
    int i =1;
    while( i <= T ){
        stoodUP = 0;
        pplToinvite = 0;
        cin >> Smax >> str;
        for( int shy = 0 ; shy <= Smax ; shy++ )
        {
            pplwithSHY = str[shy] - '0';
            if( stoodUP >= shy)
            {
                stoodUP += pplwithSHY;
            }
            if( shy!=Smax && stoodUP - (shy+1) <=0){
                pplToinvite += shy-stoodUP+1;
                stoodUP += shy-stoodUP+1;
            }
        }
        cout << "Case #" <<i<<": "<<pplToinvite << endl;
        i++;
    }
}

