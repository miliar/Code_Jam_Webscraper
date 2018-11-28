#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <sstream>
#include <fstream>

using namespace std; 

int main()
{
    int cases;
    ifstream input;
    ofstream output ("out.txt");
    input.open("in.txt");
    string s;
    input>>s;
    istringstream buffer(s);
    buffer  >>cases; 

//    int i;
//    while (input >> i) {
//        cout << i << endl;
//    }

    for(int c=0;c<cases;c++)
    {
        int m,n;
        input>>m;
        input>>n;
        int field[m][n];
        for (int j=0;j<m;j++)
        {
            for (int k=0;k<n;k++)
            {
                input>>field[j][k];
                
            }
        }
      
        bool access=true;
        
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                //horiz
                bool horiz_acc=true;
                for(int h=0;h<n;h++)
                {
                    if (h==j) continue;
                    if (field[i][h]>field[i][j]) horiz_acc=false;
                }
                
                bool vert_acc=true;
                for(int v=0;v<m;v++)
                {
                    if (v==i) continue;
                    if (field[v][j]>field[i][j]) vert_acc=false;
                }
                if (!horiz_acc && !vert_acc) {access=false;j=n;i=m;output<<"Case #"<<c+1<<": "<<"NO\n";cout<<"NO"<<"\n";} 
            }
        }
        if (access==true) {output<<"Case #"<<c+1<<": "<<"YES\n";cout<<"YES"<<"\n";}
        
    }
    return 0;
}