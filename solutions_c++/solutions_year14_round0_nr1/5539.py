#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
#include<cstdlib>
using namespace std;

int A[17];

void ja_tu_tylko_sprzatam() {
    for(int i=1; i<=16; i++)
        A[i]=0;
    return;
}

int main()  {
    int T, a, b, c, d;
    cin>>T;
    for(int tt=0; tt<T; tt++)
    {
        ja_tu_tylko_sprzatam();
        cin>>a;
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
            {
                cin>>c;
                if(i==a)
                    A[c]+=1;
            }
        cin>>a;
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
            {
                cin>>c;
                if(i==a)
                    A[c]+=1;
            }
        b=0;
        for(int i=1; i<=16; i++)
        {
            if(A[i]==2)
            {
                b++;
                d=i;
            }
        }
        cout<<"Case #"<<tt+1<<": ";
        if(b>=2) cout<<"Bad magician!"<<endl;
        else
            if(b==1) cout<<d<<endl;
        else
            cout<<"Volunteer cheated!"<<endl;

    }
    return 0;
}
