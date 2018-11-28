



#include <iostream>
//#include <iomanip>


using namespace std;

int main ()
{
    //cout << std::setprecision(7) << std::fixed;
    
    int T;
    
    cin >> T;
    
    int cards[4][4];
    
    for(int i = 1; i <= T; i++)
    {
        int a1, a2, dummy;
        
        int r1[4];
        int r2[4];
        
        cin >> a1;
        
        a1--;
        
        for(int r =0; r < 4; r++)
        {
            for(int k=0; k < 4; k++)
            {
                cin >> dummy;
                
                if(a1 == r)
                {
                    r1[k] = dummy;
                }
            }
        }
        
        
        cin >> a2;
        
        a2--;
        
        for(int r =0; r < 4; r++)
        {
            for(int k=0; k < 4; k++)
            {
                cin >> dummy;
                
                if(a2 == r)
                {
                    r2[k] = dummy;
                }
            }
        }
        
        
        int card, num_possible_matches=0;
        
        for(int k=0; k < 4; k++)
        {
            for(int j=0; j<4; j++)
            {
                if(r1[k] == r2[j])
                {
                    card = r1[k];
                    num_possible_matches++;
                }
            }
            
        }
        
        
        cout << "Case #" << i << ": ";
        
        
        if(num_possible_matches > 1)
            cout << "Bad magician!\n";
        
        else if(num_possible_matches == 0)
            cout << "Volunteer cheated!\n";
        
        else
            cout << card << "\n";
        
        
    }
    
    return 0;
}


