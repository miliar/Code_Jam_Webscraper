#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1001;
int main()
{
    int turn, T, N, war, d_war;
    double naomi[MAX], ken[MAX];
    cin >> T;
    for( turn =1; turn<=T; turn++){
        cin >> N;
        for( int i=0; i< N; i++)
            cin >> naomi[i];
        for( int i=0; i< N; i++)
            cin >> ken[i];
        sort( naomi, naomi + N );
        sort( ken, ken + N );

/*        ////////////////////////////
        for( int i=0; i< N; i++)
            cout << naomi[i] <<"  ";
        cout << endl;
        for( int i=0; i< N; i++)
            cout << ken[i] << "  ";
        cout << endl;
*/        ///////////////////////////

        // war
        war = 0;
        bool out = false;
        int j = N-1, i = N-1;
        for(; i>=0 and j>=0; j--){
            while( i>=0 and j>=0 and ken[i] > naomi[j])
            {
                if(j>0)    j--;
                else    {
                    war++;
                    out = true;
                    break;
                }
                i--;
                war++;
            }
            if (out)    break;
        }
        // d_war
        d_war = 0;
        int comp = N;
        int temp_n=N-1, temp_k=N-1;
        while( comp > 0){
            while( temp_n >=0 and temp_k >=0 and naomi[temp_n] > ken[temp_k] ){
                temp_n--;
                temp_k--;
                d_war++;
                comp--;
            }
            comp--;
            temp_k--;
        }
        cout <<"Case #" << turn << ": " << d_war << ' ' << N - war << '\n';
    }
}
