#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("A-small-attempt0.out");
    int T,N;
    int m[1000];
    int y,z,maxz;

    infile>>T;
    for(int i=1;i<=T;i++){
        infile>>N;
        for(int j=0;j<N;j++)
            infile>>m[j];

        y = z = 0;
        maxz = m[0]-m[1];

        for(int j=0;j<N-1;j++){
            if(m[j+1]<m[j])
                y += (m[j]-m[j+1]);
        }

        for(int j=0;j<N-1;j++){
            maxz = (maxz>(m[j]-m[j+1]))?maxz:(m[j]-m[j+1]);
        }

        for(int j=0;j<N-1;j++){
            z += ((m[j]<maxz)?m[j]:maxz);
        }

        outfile<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}
