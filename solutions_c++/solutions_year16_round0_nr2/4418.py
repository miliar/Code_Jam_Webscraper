#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
    ifstream in("C:\\Users\\Abhi\\Downloads\\B-large.in");
    ofstream out("C:\\Users\\Abhi\\Downloads\\B-large.out");
    long long int t,i,c,j;
    in>>t;
    char a[110];
    for(i=0;i<t;++i){
        in>>a;
        c = 0;
        for(j=1;a[j];++j)
            if(a[j]!=a[j-1])
                ++c;
        if(a[j-1]=='-')
            ++c;
        out<<"Case #"<<i+1<<": "<<c<<endl;
    }
}
