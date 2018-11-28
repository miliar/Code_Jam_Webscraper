#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
using namespace std;
vector<int> V;
bool test()
{
    for(int i=0;i<=9;i++)
        if(V[i]==0)
            return false;
    return true;
}

void proceed(long long int n)
{
    while(n!=0)
    {
        V[n%10]=1;
        n/=10;
    }
    //cout<<n<<endl;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    V.resize(11);
    long long int n,t,cpt;
    cin>>t;
    int k=1;
    while(t--)
    {

        cpt=0;
        for(int i=0;i<=9;i++)
            V[i]=0;
        cin>>n;
        cout<<"Case #"<<k<<": ";
        k++;
        if(n==0)
            cout<<"INSOMNIA"<<endl;
        else
        {
            do
            {
                cpt++;
                proceed(n*cpt);

            }while(!test());

            cout<<cpt*n<<endl;
        }
    }

}
