#include <iostream>
#include <cstring>
using namespace std;

int proc(int x)
{
    int s = 0, z;
    for (int i=1; i<=4;i++)
        for (int j = 1; j<=4; j++)
        {
            cin >> z;
            if (i == x)
                s += (1 << z);
        }
    return s;
}

int main()
{
    int T; cin>>T;
    int s1, s2;
    for (int i=1; i<=T; i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>s1; int a = proc(s1);
        cin>>s2; int b = proc(s2);
        int c = a & b, cnt = 0, lst = 0;
        for (int j = 1; j<=16; j++)
            if (c & (1<<j)) {cnt++;lst = j;}
        if (cnt ==0) cout<<"Volunteer cheated!"<<endl;
        if (cnt ==1) cout<<lst<<endl;
        if (cnt >1) cout<<"Bad magician!"<<endl;
    }
    return 0;
}
