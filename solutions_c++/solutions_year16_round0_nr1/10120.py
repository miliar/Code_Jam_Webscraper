#include <iostream>
#include <set>
#include <fstream>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

int main()
{
    int cases;
    set<int> rep;
    in>>cases;
    for(int p=1;p<=cases;p++){
        rep.clear();
        long long j,k,n,i=1;
        in>>n;
        if(n==0){out<<"Case #"<<p<<": INSOMNIA"<<endl; continue;}
        while(rep.size()<10){
            k=n*i;
            j=k;
            while(j>9){
                rep.insert(j%10);
                j/=10;
            }
            rep.insert(j);
            i++;
        }
    out<<"Case #"<<p<<": "<<k<<endl;
    }
}
