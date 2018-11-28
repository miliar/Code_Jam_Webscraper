#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T;
    
    fin >> T;
    for (int t=0;t<T;t++ )
    {
        double C,F,X;
        double tmpTime,Time;
        int n;
        fin >> C >> F >> X;

        Time = X /2.0;
        n = 0;
        while(1)
        {
            n = n+1;
            tmpTime = 0;
            for (int i=0;i<n;i++){
                tmpTime = tmpTime + C/(2.0+ i*F);
            }
            tmpTime = tmpTime + X/(2.0+ n*F);
            if (tmpTime< Time)
            {
                Time = tmpTime;
            }
            else
            {
                break;
            }           
        }
        fout << "Case #" << t+1 << ": " << setiosflags(ios::fixed) << setprecision(10) << Time << endl;
        
    }     
    fin.close();
    fout.close();
    
    return 0;
}
