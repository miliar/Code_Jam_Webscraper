#include <iostream>
#include <string.h>
#include <sstream>
#include <stdlib.h>
using namespace std;

int main()
{
    int i, t,j,todos=0,multiplicador;
    int n;
    cin>>t;
    int dig[10];

    for (i=1;i <= t;i++){
        cin>>n;
        memset(dig,0,sizeof (dig));
        todos=0;
        multiplicador=1;
        bool ten = false;

        while(todos <= 10 && !ten && n!=0){
            char nn[1000001];
            itoa(n*multiplicador, nn,10);
            for(j = 0; j < strlen(nn) && todos<=10 && !ten;j++ ){
                if( dig[(nn[j]-'0')] == 0 ){todos++;}
                dig[(nn[j]-'0')] = 1;
                if(todos==10){
                    ten = true;
                }
            }
            multiplicador++;
        }
        if(todos>=10){
            cout<<"Case #"<<i<<": "<<n*(multiplicador-1)<<endl;
        }else{
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
    }
    return 0;
}
