#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
typedef long long ll ;
//const int maxx =  ;
const int inf = 1<<30 ;
char ch[2100] , s[2100];
using namespace std;
int main()
{
    int cas = 1 , T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin >> T ;
    while(T--){
        memset(ch,0,sizeof(ch)) ;
        cin >> s;
        int len = strlen(s) ;
        int left = len, right = len ;
        ch[left] = s[0] ;
//    cout << ch[left] <<" " <<left <<endl ;
   // cout << s  <<endl ;
        for(int i = 1 ; i < len ; ++i){
              //  cout << "ch letf " << ch[left] << " " << " s[i] " << s[i] <<endl;
            if(s[i] >= ch[left]){
                --left;
                ch[left] = s[i] ;
               // cout << ch[left] << " * " <<endl;;
            }
            else {
                ++right ;
                ch[right] = s[i] ;
               // cout << ch[right] << " xxxx " <<endl ;
            }
        }
        printf("Case #%d: ",cas++) ;
        for(int i = left ; i <= right ; ++i){
            cout << ch[i] ;
        }
        cout << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
