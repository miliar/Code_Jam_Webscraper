// deceitful war
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<float> vecf;

vecf Naomi(1000);
vecf Ken(1000);

int main()
{
    unsigned int i, j, k;
    unsigned int T;
    
    cin>>T;
    
    for (i = 0; i < T; i++)
    {
        unsigned int N;
        unsigned int dw_score = 0;
        unsigned int w_score = 0;
        
        cin>>N;
        for (j = 0; j < N; j++)
        {
            cin>>Naomi[j];
        }
        for (j = 0; j < N; j++)
        {
            cin>>Ken[j];
        }
        
        sort(Naomi.begin(), Naomi.begin() + N);
        sort(Ken.begin(), Ken.begin() + N);
        
        for (j = 0, k = 0; j < N; j++)
        {
            if (Ken[j] > Naomi[k])
            {
                w_score++;
                k++;
            }
        }
        
        w_score = N - w_score;
        
        for (j = 0, k = 0; j < N; j++)
        {
            if (Naomi[j] > Ken[k])
            {
                dw_score++;
                k++;
            }
        }
        
        cout<<"Case #"<<i+1<<": "<<dw_score<<" "<<w_score<<endl;
    }
    
    return 0;
}
