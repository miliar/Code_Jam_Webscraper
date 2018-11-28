#include <iostream>

using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    int tdb,kidb,K,j,h,l;
    bool b;
    cin>>tdb;
    int i;
    string S;
    int T[1000];
    for (i=0; i!=tdb; i++)
    {
        cin>>S>>K;
        h=S.length();
        for (j=0; j!=h; j++)
        {
            if (S[j]=='+') {T[j]=1;} else {T[j]=-1;}
        }
        kidb=0;
        for (j=0; j+K<=h; j++)
        {
            if (T[j]==-1)
            {
                kidb++;
                for (l=0; l!=K; l++)
                {
                    T[l+j]*=-1;
                }
            }
        }
        b=false;
        cout<<"Case #"<<i+1<<": ";
        for (j=j; j!=h; j++)
        {
            if (T[j]==-1)
            {
                b=true;
                cout<<"IMPOSSIBLE"<<endl; break;
            }
        }
        if (!b)
        {
            cout<<kidb<<endl;
        }
    }

    return 0;
}
