#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t;
    int chk1;
    int chk2;
    int ar1 [16];
    int ar2 [16];
    int c1 [4];
    int c2 [4];
    
    ifstream in;
    ofstream out;

    in.open("input.txt");
    

    in >> t;
    
    for (int i=1; i<=t; i++)
    {
        int flag = 0;
        int ans=0;
        in >> chk1;
        
        for (int j=0; j<16; j++)
        in >> ar1 [j];
        
        in >> chk2;
        
        for (int j=0; j<16; j++)
        in >> ar2 [j];
        
        if (chk1==1)
        {
            for (int k=0; k<4; k++)
                c1 [k]=ar1 [k];
        }
        
        else if (chk1==2)
        {
            for (int k=0; k<4; k++)
                c1 [k]=ar1 [k+4];
        }
        
        else if (chk1==3)
        {
            for (int k=0; k<4; k++)
                c1 [k]=ar1 [k+8];
        }
        
        else
        {
            for (int k=0; k<4; k++)
                c1 [k]=ar1 [k+12];
        }
        
        
        if (chk2==1)
        {
            for (int k=0; k<4; k++)
                c2 [k]=ar2 [k];
        }
        
        else if (chk2==2)
        {
            for (int k=0; k<4; k++)
                c2 [k]=ar2 [k+4];
        }
        
        else if (chk2==3)
        {
            for (int k=0; k<4; k++)
                c2 [k]=ar2 [k+8];
        }
        
        else
        {
            for (int k=0; k<4; k++)
                c2 [k]=ar2 [k+12];
        }
        
        for (int a=0; a<4; a++)
        {
            for (int b=0; b<4; b++)
            {
                if (c1 [a]== c2[b])
                    {
                        flag ++;
                        ans=c1 [a];
                    }
            }
        }
        
        if (flag == 1)
            cout << "Case" << "#"<<i<< ":"<<" "<<ans<<endl;
            
        else if (flag > 1)
            cout << "Case" << "#"<<i<< ":"<<" "<<"Bad magician!"<<endl;
            
        else
           cout << "Case" << "#"<<i<< ":"<<" "<<"Volunteer cheated!"<<endl; 
    
    
    }
    
    //cout << "The number read is: " << one_number << endl; 
    //cout << "The number read is: " << a << endl;
   
   return 0;
}
