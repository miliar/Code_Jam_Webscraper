#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream f2("f2.out");
    int nn;
    cin>>nn;
    int n;
    char a[10000];
    int b[10000],count=0,min=0;
    for(int i=0;i<nn;++i)
    {
        count=0;
        min=0;
        cin>>n;
        cin>>a;
        for(int j=0;j<n+1;++j)
        {
            b[j]=a[j]-'0';
            if(count>j||count==j)
            {
                count+=b[j];
            }
            else
            {
                min+=j-count;
                count=j;
                count+=b[j];
            }
        }
        f2<<"Case #"<<i+1<<":"<<" "<<min<<endl;
    }
    return 0;
}
