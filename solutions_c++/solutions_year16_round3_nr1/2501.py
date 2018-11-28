

#include <iostream>
#include "utility.h"


using namespace std;

bool containsMajority(int * MemberCount, int N, int Index1, int Subtract1, int Index2, int Subtract2, int PeopleCount)
{
    
    MemberCount[Index1] -= Subtract1;
    MemberCount[Index2] -= Subtract2;
    bool returnBool;
    
    int MaxI = 0;
    
    for(int i=0; i<N; i++)
        if(MemberCount[i] > MemberCount[MaxI]) MaxI = i;

    if(MemberCount[MaxI] >  (PeopleCount - Subtract1 - Subtract2 - MemberCount[MaxI]))
            returnBool = true;
    else
        returnBool = false;

    
    MemberCount[Index1] += Subtract1;
    MemberCount[Index2] += Subtract2;
    
    
    
    return returnBool;

}

int main(int argc, const char * argv[])
{
    int T;
    cin >> T;
    
    
    for (int t = 1; t <= T; ++t)
    {
        
        int N;
        int MemberCount[26];
        int PeopleCount = 0;
        cin >> N;
        
        for(int i=0; i<N; i++)
        {
            cin >> MemberCount[i];
            PeopleCount += MemberCount[i];
        }
        
        
        
        cout << "Case #" << t << ": ";

        
        while(PeopleCount > 0)
        {
            
            int MaxI = 0;
            
            for(int i=0; i<N; i++)
                if(MemberCount[i] > MemberCount[MaxI])
                    MaxI = i;
            
            int SecondMaxI = !MaxI;
            
            for(int i=0; i<N; i++)
                if(MemberCount[i] > MemberCount[SecondMaxI] && i != MaxI)
                    SecondMaxI = i;
            

            if(MemberCount[MaxI] >= 2)
            {
                if(!containsMajority(MemberCount, N, MaxI, 2, SecondMaxI, 0, PeopleCount))
                {
                    cout << (char)(MaxI + 'A') << (char)(MaxI + 'A') << " ";
                    MemberCount[MaxI] -=2;
                    PeopleCount -= 2;
                    continue;

                }
            }
            
            
            if (MemberCount[MaxI] >= 1 && MemberCount[SecondMaxI] >= 1)
            {
                
                if(!containsMajority(MemberCount, N, MaxI, 1, SecondMaxI, 1, PeopleCount))
                {
                    
                    cout << (char)(MaxI + 'A') << (char)(SecondMaxI + 'A') << " ";
                    MemberCount[MaxI] -=1;
                    MemberCount[SecondMaxI] -=1;

                    PeopleCount -= 2;
                    continue;
                }

            }
            
            if (MemberCount[MaxI] >= 1)
            {
                
                if(!containsMajority(MemberCount, N, MaxI, 1, 0, 0, PeopleCount))
                {
                    cout << (char)(MaxI + 'A') << " ";
                    MemberCount[MaxI] -=1;

                    PeopleCount -= 1;
                    continue;
                }
            }
            
            
            cout << "ERROR";
            return 0;
            
            
        }
        
        cout << endl;
        
        
        
        
     
    }
    

    

    
    
    
    
    
}

