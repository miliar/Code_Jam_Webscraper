#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
                           
    int T;
    
    cin >> T;
    
    for(int i = 1; i <= T; i++)
    {
            cout << "Case #" << i << ": ";
            
            int N, fair = 0, unfair = 0;
            
            cin >> N;
            
            double *ken = new double[N];
            double *naomi = new double[N];
            
            for(int j = 0; j < N; j++) cin >> naomi[j];
            for(int j = 0; j < N; j++) cin >> ken[j];
            
            sort(naomi, naomi+N);
            sort(ken, ken+N);
            
            int kens = N-1, naomis = N-1;
            
            while(naomis >= 0)
            {
            	         if(naomi[naomis] > ken[kens]) fair++;
                         else kens--;
                         naomis--;
            }
            
            kens = 0, naomis = N-1;
            
            for(int j = 0; j < N; j++)
            {
            	if(naomi[j] > ken[kens])
                   {
                        unfair++; 
                        kens++;
                   }
            }
            
            cout << unfair << " " << fair << endl;
            
            delete[] ken;
            delete[] naomi;
            
    }
    
    return 0;
}
