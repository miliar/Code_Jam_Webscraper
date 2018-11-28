#include <bits/stdc++.h>

using namespace std;

int respuesta;
char s[10];
int ss[10];

void cambiar(int max){
    for(int i = 0; i < max; i++)
        if(ss[i] == 0)ss[i] = 1;
        else ss[i] = 0;
}

int main()
{
    
    int t, q;
    cin >> t;
    
    q = t;
    
    while(t--){
        
        respuesta = 0;
        
        for(int i = 0; i < 10; i++){
            s[i] = '\0';
            ss[i] = -1;
        }
        
        cin >> s;
        
        for(int i = 0; i < strlen(s); i++)
            if(s[i] == '+')ss[i] = 1;
            else ss[i] = 0;
            
        for(int j = strlen(s)-1; j > -1; j--){
            if(ss[j] == 1);
            else {
                respuesta++;
                ss[j] = 1;
                cambiar(j);
            }
        }
        
        
        
        cout << "Case #" << q-t << ": " << respuesta << endl;
    }
    
    return 0;
}
