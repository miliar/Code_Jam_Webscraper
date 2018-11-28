#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	char XX[1000000];
	char X;
	string S;
	int L;
	int N;

	int y;
    for (int T_i=0; T_i<T;T_i++){
        X = '*';
        L=0;
        cin >> S;
        cin >> N;    
        
        int S_start = -1; 
        int S_count = 0;
        int Result = 0;
        int Last_k;
        
        for (int i=0; i < S.length();i++){
            if ((S[i]=='a') || (S[i]=='i') || (S[i] =='u') || (S[i]=='e') || (S[i] =='o'))
            XX[L] = 'O'; else XX[L]='X';
            if ((S_start == -1) && (XX[L]=='X')) S_start = i;
            if ((S_start != -1) && (XX[L]=='O')) {
                          if (i-S_start< N) for (int j = S_start;j <i; j++) XX[j]='O';
                          S_start = -1;
                          }
            L++; 
        }
        for (int i=0;i <L-N+1;i++){
            S_count = 0;
            for (int k=i;k<L;k++) {
               if (XX[k] =='X') S_count++; 
               if (XX[k] =='O') S_count =0;
               if (S_count >= N) { Last_k = k; k=L;}
            }
            if (S_count >=N) {
               Result += L - Last_k;
            }
        }
        

        cout << "Case #" << T_i+1 << ": " << Result << endl;
    }
    return EXIT_SUCCESS;
}
