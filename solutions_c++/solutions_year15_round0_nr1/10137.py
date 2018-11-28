
#include <iostream>
#include <fstream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int x , S;
    int fr = 0;
    int count = 0;
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
    in>>x;
    for(int i = 0; i < x; i++)
    {
        in>>S;
        S++;
        char* y;
        y = new char[S];
        in >> y;
        count+= y[0] - '0';
        for(int j=1; j<S; j++)
        {
            if(count >= j)
            {
                count+=y[j] - '0';
            }
            else
            {
                fr+= j-count;
                count+= y[j] - '0' + j - count;
            }
        }
        out<<"Case #"<<i+1<<": "<<fr<<endl;
        fr = 0;
        count = 0;
    }
    return 0;
}
