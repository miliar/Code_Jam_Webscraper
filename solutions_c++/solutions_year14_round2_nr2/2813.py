#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,a,b,k,cnt = 0;

	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "B-small-attempt0.out", "w", stdout );
    cin>>t;
    for(int c = 0; c < t; c++)
    {
        cnt = 0;
        cin>>a>>b>>k;
        for(int i = 0; i < a; i++)
        {
            for(int j = 0; j < b; j++)
            {
                if((i&j) < k)
                    cnt++;
            }
        }
        cout<<"Case #"<<c + 1<<": "<<cnt<<"\n";

    }
    return 0;
}
