#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    string orden;
    char inicio;
    int tc;
    cin>>tc;
    for(int j=0; j<tc;j++){
        cin>>orden;

        bool listo=true;
        int flip=0;
        for(int a=0; a<orden.size(); a++){
                if(orden[a]=='-'){
                    listo=false;
                    break;
                }
            }
        while(listo==false){
            int contPos =-1;
                for(int i=0; i<orden.size(); i++){
                    inicio=orden[0];
                    if(orden[i]==inicio){
                        contPos++;
                    }
                    else break;
                }

            for(int k=contPos; k>=0; k--){
                if(orden[k]=='+')orden[k]='-';
                else orden[k]='+';
            }
            flip++;
            listo=true;
            for(int a=0; a<orden.size(); a++){
                if(orden[a]=='-'){
                    listo=false;
                    break;
                }
            }

        }
        cout<<"Case #"<<j+1<<": "<<flip<<endl;


    }

    return 0;
}
