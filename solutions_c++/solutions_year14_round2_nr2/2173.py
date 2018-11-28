#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>
#include <bitset>
#include <sstream>


#define forf(a,b) for(a=0;a<b;a++)
#define forb(a,b) for(a=b;a>0;a--)
#define count(a) for (int zzz=0;zzz<a;zzz++)
#define PI 3.14159265358979
#define MILLION 1000000
#define BILLION 1000000000
#define oo 999999999

using namespace std;




int main()
{
    int T,ANS;
    int A,B,K;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin>>T;

    for (int i=1; i<T+1;i++){
        cin>>A>>B>>K;
        ANS=0;
        for (int j=0;j<A;j++){
            for (int k=0;k<B;k++){
                if ( (j & k)  < K ){
                    ANS++;
                }
            }
        }
        printf( "Case #%d: %d\n",i, ANS);
        /*if (K>max(A,B)){
            printf( "Case #%d: %d\n",i, A*B);
        }
        else if( K )
        //for (int first=0;first<)
*/

    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}
