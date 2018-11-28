#include<iostream>
#include<cstdlib>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

int main () 
{
    int T;
    cin>>T;
    for(int Barti=0; Barti<T; Barti++)
    {
        int a, b, k;
        cin>>a>>b>>k;

        int c=0;
        for(int i=0; i<a; i++)
            for(int j=0; j<b; j++)
            {
                if( (i&j) < k) c++;
            }
        cout<<"Case #"<<Barti+1<<": "<<c<<endl;
    }
    return 0;
}
