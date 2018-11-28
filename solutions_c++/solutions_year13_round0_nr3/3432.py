#include<iostream>
#include<vector>
#include<cmath>


using namespace std;

int reverseNumber(int n, int dec)
{
    int nn = 0;
    while(n != 0)
    {
        int i = n%10;
        n /= 10;
        nn += i * dec;
        dec /= 10;
    }
    return nn;
}

int main()
{
    vector<int> vec;

    int dec = 1;
    int cont = 0;
    for(int i = 1; i<=32; ++i)
    {
        if(i == dec*10)
            dec *= 10;

        if(i == reverseNumber(i,dec) && i*i == reverseNumber(i*i, (i*i < dec*10?dec:dec*10)))
        {
            vec.push_back(i*i);
        }
    }
    int t;
    cin>>t;
    for(int k=0; k<t; ++k)
    {
        int a, b;
        cin>>a>>b;
        int cont = 0;
        for(int i=0; i<vec.size(); ++i)
        {
            if(vec[i] >= a && vec[i] <= b)
                cont++;
        }
        cout<<"Case #"<<k+1<<": "<<cont<<endl;
    }
    return 0;
}
