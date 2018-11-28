#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2016/GoogleCodeJam/CountingSheep/A-large.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2016/GoogleCodeJam/CountingSheep/A-large.ou.txt");

    
    
    bool digits[10];
    
    int cases;
    
    input >> cases;
    
    cout << cases << endl;
    
    for(int j = 0; j < cases; j++)
    {
        bool stop = false;
        bool insomnia = false;
        
        for(int i = 0; i < 10; i++)
        {
            digits[i] = false;
        }
        
        int N, N_temp;
        
        input >> N;
        
       
        
        if(N == 0)
        {
            stop = true;
            insomnia = true;
        }
        
        for(int k = 1; !stop; k++)
        {
            N_temp = N * k;
            
            int n = N_temp;
            
            while(n > 0)
            {
                digits[n % 10] = true;
                n = (n - (n % 10)) / 10;
            }
            
            stop = true;
            for(int h = 0; h < 10; h++)
            {
                if(digits[h] == false)
                {
                    stop = false;
                }
            }
        }
        
        if(insomnia)
        {
            output << "Case #" << j+1 << ": INSOMNIA" << endl;
            cout << "Case #" << j+1 << ": INSOMNIA" << endl;
        }
        else
        {
            output << "Case #" << j+1 << ": " << N_temp << endl;
            cout << "Case #" << j+1 << ": " << N_temp << endl;
        }
    }
    
    return 0;
}
