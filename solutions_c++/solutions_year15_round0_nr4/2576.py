#include <iostream>
using namespace std;

int main() {
    int t;
    bool flag;
    cin >> t;
    int q=t;
    while(t--)
    {
        int x,r,c;
        cin >> x >> r >> c ;
        if(x==1)
        flag=1;
        else if(x==2)
        {
            if((r==1&&c==1)||(r==1&&c==3)||(r==3&&c==1)||(r==3&&c==3))
            flag=0;
            else
            flag=1;
        }
        else if(x==3)
        {
            if((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==4)||(r==4&&c==3)||(r==3&&c==3))
            flag=1;
            else
            flag=0;
        }
        else
        {
            if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
            flag=1;
            else
            flag=0;
        }
        
        if(flag==0)
        cout<<"Case #"<<q-t<<": "<<"RICHARD" << endl;
        else
        cout<<"Case #"<<q-t<<": "<<"GABRIEL" << endl;
    }
    
	return 0;
}
