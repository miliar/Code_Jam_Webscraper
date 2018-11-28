#include<iostream>
using namespace std;

int main()
{
    int  t,j;
    cin >> t;
    for(j=1;j<=t;j++){
        int n,i;
        string nn;
        cin >> n >> nn;
        int c=0;
        int cl=0;
        int y=0;

        if((nn[0]-'0')>0)  cl=(nn[0]-'0');c=0;

        for(i=1;i<=n;i++){
             int h=nn[i]-'0';
            if(h>0){
                if(cl>=i)
                {
                    cl=cl+h;

                    continue;
                }
                else {

                    y=i-cl;
                    c=c+y;
                    cl=cl+h+y;

                }
            }
        }
        cout << "Case #"<<j<<": "<<c<<endl;
    }
    return 0;


}
