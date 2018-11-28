#include <bits/stdc++.h>

using namespace std;

int main()
{
    int x , r , c ,cases;
    cin >> cases ;
    string s1 = "GABRIEL";
    string s2 = "RICHARD";
    for (int k=0;k<cases;k++)
    {
        bool a = false ;
        cin >> x >> r >> c ;
        if (x==1) {a=true;}
        if (x==2) {
                    if ((c*r)%2==0) {a=true;}
                    else {a=false;}
                  }
        if (x==3) {
                    if (c*r==6||c*r==9) {a=true;}
                    else
                    a=false ;
                  }
        if (x==4) {
                    if (c*r==8||c*r==12||c*r==16)
                    {
                        a=true ;
                    }
                    else
                        a=false;
                  }
            if (a) {cout << "Case #"<<k+1<<": "<<s1<<endl;}
            else {cout << "Case #"<<k+1<<": "<<s2<<endl;}
    }

    return 0;
    //cout << "Case #"<<k+1<<": "<<s1<<endl;
}
