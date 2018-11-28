#include <iostream>
#include <fstream>
#include<iomanip>
using namespace std;

int main()
{

    // insert code here...
    
    ifstream fin ("B-large.in");
    if(!fin)
    {
        return 1;
    }
    ofstream fout ("BL.out");
    if(!fout)
        return 1;
    
    double C,F,X;
    int T;
    fin>>T;
    if(T<1 || T>100)
        return 1;
    
    for( int i=0; i<T; i++)
    {
        fin>>C;
        fin>>F;
        fin>>X;
        if(C<1 || C>10000 || F<1 || F>100 || X<1 || X>100000)
            return 1;
        
        double cookies = 0;
        double time = 0.0;
        double timer=2;
        if(X<C)
        {
            time = X/2.0;
        }
        else
        {
            cookies = C;
            time = C/2.0;
            while(cookies != X)
            {
                if( time+(X/(timer+F)) < time+((X-C)/timer))
                {
                    timer = timer+F;
                    time = time + C/timer;
                    cookies = C;
                }
                else
                {
                    time = time + (X-C)/timer;
                    cookies = X;
                }
                
            }
        }
		int a = time;
		int len = 0;
		while(a!= 0)
		{
			len++;
			a /= 10;
		}
		fout<<showpoint<<setprecision(7+len)<<"Case #"<<i+1<<": "<<time<<endl;
    }
    return 0;
}