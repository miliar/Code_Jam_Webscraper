#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin>>T;

    for(int t=1; t<=T; t++)
    {
        int Smax;
        cin>>Smax;
        int standing=0, count=0;

        char* ar= new char[Smax+1];

        for(int i=0; i<=Smax; i++)
        {
            cin>>ar[i];
        }

        for(int i=0; i<=Smax; i++)
        {
            int temp=0;
            if(i>standing)
            {
                count+= (i-standing);
                temp=i-standing;
            }
            standing += (ar[i]-'0'+temp);
        }
        cout<<"Case #"<<t<<": "<<count<<endl;
        delete[] ar;
    }
    return 0;
}
