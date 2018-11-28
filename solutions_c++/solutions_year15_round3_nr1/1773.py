#include <bits/stdc++.h>
using namespace std;
long long int T;
int R,C,W;
int main()
{
    //ofstream cout("respuesta.txt");
    //ifstream cin;cin.open ("A-small-attempt1.in");

    while (cin>>T){
        for(int i=1;i<=T;i++){
            cin>>R>>C>>W;
            int intentos = C/W;
            int respuesta = C/W;
            if(C%W!=0){
                respuesta++;
            }
            respuesta+= (W-1);

            cout<<"Case #"<<i<<": "<<respuesta<<endl;
        }
    }
    //cin.close();
    //cout.close();
}
