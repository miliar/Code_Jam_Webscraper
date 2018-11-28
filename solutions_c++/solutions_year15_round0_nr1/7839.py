#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int n;
    ifstream in("A-large.in");
    ofstream out("output.txt");
    in>>n;
    for(int i=0; i<n ; ++i)
    {
       int smax;
       in>>smax;
       int counter = 0;
       int audCount = 0;
       for(int j=0; j <smax + 1; j++)
       {
          char csi; 
          in>>csi;
          int si = csi - '0';
//          cout<<si;
          audCount += si;
          if(audCount <= j)
          {
              counter += j - audCount + 1;
              audCount = j + 1;
          }
       }
       out<<"Case #"<<i+1<<": "<<counter<<endl;
    }
    system("pause");
    return 0;
}
