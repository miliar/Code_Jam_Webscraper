#include <iostream>
#include <fstream>

using namespace std;
typedef long long ll;


int main()
{
    
    ifstream in("/Users/vlad8/Downloads/D-small-attempt1.in.txt");
    ofstream out("/Users/vlad8/Downloads/D-small-attempt1.out.txt");
    int T;
    in>>T;
    for(int i=0;i<T;i++)
    {
    ll k,c,s;
    in>>k>>c>>s;
    
        out<<"case #"+to_string(i+1)+": ";
        
        for(int u=1;u<=k;u++)
            out<<u<<' ';
        
        out<<endl;
    }
    
    
   
}