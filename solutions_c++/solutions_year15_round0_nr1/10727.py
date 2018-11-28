#include<bits/stdc++.h>

using namespace std;

int main()
{
    int  t,j;
    cin >> t;
    for(j=1;j<=t;j++){
        int n,i;
        string str;
        cin >> n >> str;
        int c=0; int cl=0; int y=0;
        
        if((str[0]-'0')>0)  cl=(str[0]-'0');c=0;
        for(i=1;i<=n;i++){

            if((str[i]-'0')>0){
                if(cl>=i)
                {
                    cl=cl+(str[i]-'0');
                    continue;
                }
                else {

                    y=i-cl;
                    c=c+y;
                    cl=cl+(str[i]-'0')+y;
                }
            }
        }
        cout << "Case #"<<j<<": "<<c<<endl;
    }
    return 0;


}
