#include <iostream>

using namespace std;

int main()
{
    int k;
    cin>>k;
    for(int i = 0; i < k; i++)
    {
        int r, t;
        cin>>r>>t;
        int rr = r;
        int cont = 0;
        int c = (((rr+1)*(rr+1)) - (rr*rr));
        while(t >= c)
        {
            t -= c;
            rr+=2;
            cont++;
            c = (((rr+1)*(rr+1)) - (rr*rr));
        }
        cout<<"Case #"<<i+1<<": "<<cont<<endl;
    }
    return 0;
}
