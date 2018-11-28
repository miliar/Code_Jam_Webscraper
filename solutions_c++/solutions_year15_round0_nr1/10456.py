#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
    int T,Smax,need,standing;
    string audience;
    
    cin >> T;
    
    for (int i=0;i<T;i++)
    {
        cin >> Smax;
        cin >> audience;
        standing = 0;
        need = 0;
        for (int j=0;j<(Smax+1);j++){
            char c = audience[j];
            int cant =atoi(&c);
            if (j==0) standing = cant;
            else{
                if (standing >= j){
                    standing += cant; //se paran todos los del nivel pq ya cumple
                }else {
                    need += (j - standing); //los que me faltan para que se paren los de este nivel
                    standing += (j - standing) + cant;// paro a los de este nivel
                }
            }
            //cout << "Stand: " << standing << ", need: " << need << ", j: " << j << endl;
            
            
        }
        cout << "Case #" << i+1 << ": " << need <<endl;
    }
    return 0;
}
