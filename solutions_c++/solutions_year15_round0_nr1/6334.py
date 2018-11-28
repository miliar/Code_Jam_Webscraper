#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.txt", "w", stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        int contador=0,amigos=0;
        string tm;
        int s;
        cin>>s>>tm;
        for(int i=0;i<tm.size();i++)
        {
            tm[i]-='0';
            if((int)tm[i]!=0){

                if(contador<i){
                    amigos+=(i-contador);
                    contador+=(i-contador);
                }
                contador+=(int)tm[i];
            }
        }
        cout<<"Case #"<<tc<<": "<<amigos<<endl;
    }
    return 0;
}
