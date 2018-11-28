#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    ifstream input ("/Users/hasan/Desktop/xcode projects/war/war/D-small-attempt0.in.txt");
    ofstream output ("/Users/hasan/Desktop/xcode projects/war/war/D-small-attempt0.out.txt");
    
    int t,m,y,z;
    double n[1000], k[1000], cn[1000], ck[1000];
    input >> t;
    for (int l=0;l<t;l++)
    {
        output << "Case #" << l+1 << ": ";
        input >> m;
        
        for (int i=0;i<m;i++)
            input >> n[i];
        
        for (int i=0;i<m;i++)
            input >> k[i];
        
        for(int i=1;i<m;i++)
            for(int j=0;j<m-1;j++)
                if(n[j] > n[j+1])
                {
                    double temp = n[j];
                    n[j] = n[j+1];
                    n[j+1] = temp;
                }
        for(int i=1;i<m;i++)
            for(int j=0;j<m-1;j++)
                if(k[j] > k[j+1])
                {
                    double temp = k[j];
                    k[j] = k[j+1];
                    k[j+1] = temp;
                }
        
        for(int i=0;i<m;i++)
            cn[i] = n[i];
        for(int i=0;i<m;i++)
            ck[i] = k[i];
        
        z=0;
        for (int i=0;i<m;i++)
            for (int j=0;j<m;j++)
                if (k[j]>n[i])
                {
                    z++,k[j]=0;
                    break;
                }
        
        y=0;
        int d = m;
        for (int i=0;i<m;i++)
        {
            int j;
            for (j=0;j<d;j++)
                if (cn[i]>ck[j])
                {
                    y++;
                    ck[j]=2;
                    break;
                }
            if (j==d)
                d--;
        }
        
        output << y << " " << m-z << endl;
    }
    
    return 0;
}
