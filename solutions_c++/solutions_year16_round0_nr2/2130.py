
#include <cstdio> 
#include <iostream>
#include <string>

using namespace std;


int main()
{
    int T;
    cin >> T;
  
    int count = 1;
    while(T--)
    {
        string in;
        cin >> in;
        in += "+";
        char s = in[0];
        int flips = 0;
        for(int i = 1; i < in.length(); i++)
        {
            if (in[i] != s) flips++;
            s = in[i];
        }
        cout << "Case #" << count++ << ": " << flips << endl;
            
    }
    
}
   
