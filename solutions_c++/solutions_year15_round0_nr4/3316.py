#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int main(){
    int j,t;
    cin >> t;
    for(j=1;j<=t;j++){
        int x,r,c,a[21][21];
        string s;
        cin >> x >> r >> c;
        if((r*c)%x!=0)s.assign("RICHARD");
        else{
            if(x==1)s.assign("GABRIEL");
            else if (x==2)s.assign("GABRIEL");
            else if (x==3){
                if(c < 2 || r < 2)s.assign("RICHARD");
            }
            else if(x==4){
                if((c==2 && r==4) || (c==4 && r==2))s.assign("RICHARD");
                else if(c < 4 && r < 4)s.assign("RICHARD");
                else if(c < 2 || r < 2)s.assign("RICHARD");
            }
        }
        if(s.empty())s.assign("GABRIEL");
        cout << "Case #" << j << ": " << s << endl;
    }
    return 0;
}
