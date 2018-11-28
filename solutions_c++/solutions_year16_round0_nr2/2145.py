#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

string panc;

int lastSad(int size) {
    int lSad = -1;
    for(int i = size-1; i >= 0 && lSad == -1 ; i--)
        if(panc[i] == '-')
            lSad = i;

#ifdef _DEBUG
        cout << lSad << endl;
#endif
        
    return lSad;
}


int main()
{
    int T, cont = 0;
    
    scanf("%d\n", &T);

    while(T--)
    {
        getline(cin, panc);
#ifdef _DEBUG
        cout << panc << endl;
#endif
        
        int size = panc.length();
        
        int n;
        for(n = 0;  ; n++) {
            int lSad = lastSad(size);

            if(lSad == -1)
                break ;
            
            for(int i = 0; i <= lSad; i++) 
                panc[i] = (panc[i] == '+') ? '-' : '+';
#ifdef _DEBUG
        cout << panc << endl;
#endif
        }
        
        cout << "Case #" << ++cont << ": " << n << endl;
    }
        
return 0;
}
