#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
	ifstream in("A-large.in");
    ofstream out("A-large.out");
    
	long int xxx , SSS;
    long int count = 0;
    long int frrr = 0;
    in>>xxx;
    
	for(long int i = 0; i < xxx; i++)
    {
        in>>SSS;
        SSS++;
        char y[SSS];
        in >> y;
        count= count + y[0] - 48;
        for(long int j=1; j<SSS; j++)
        {
            if(count >= j)
            {
                count+=y[j] - 48;
            }
            else
            {
                frrr+= j-count;
                count+= y[j] - 48 + j - count;
            }
        }
        out<<"Case #"<<i+1<<": "<<frrr<<endl;
        frrr = 0;
        count = 0;
	}
    
    return 0;
}
