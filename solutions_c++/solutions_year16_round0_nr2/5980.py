#include <iostream>
#include <cstdio>
using namespace std;
string s;
int t,caso,l,arr[105],aux,res;
int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>t;
    for (caso=1;caso<=t;caso++){
        cin>>s;
        l=s.size();
        for (int i=0;i<l;i++)
            if (s[i]=='+')
                arr[i]=1;
            else
                arr[i]=-1;
        aux=1;
        res=0;
        for (int i=l-1;i>=0;i--){
            if (arr[i]!=aux){
                aux*=-1;
                res++;
            }
        }
        cout<<"Case #"<<caso<<": "<<res<<endl;
    }
    return 0;
}
