#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("din.txt","r",stdin);
    freopen("dout.txt","w",stdout);
    int test,i,j,k,c,s;
    cin>>test;
    for(i=0;i<test;i++)
    {
        cin>>k>>c>>s;
        cout<<"Case #"<<i+1<<":";
        for(j=0;j<s;j++)
        {
            cout<<" "<<j+1;
        }
        cout<<endl;
    }
    fclose(stdout);
    return 0;
}
