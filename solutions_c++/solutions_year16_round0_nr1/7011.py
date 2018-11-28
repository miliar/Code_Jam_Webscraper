#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream inf;

    int t=0,nt=0;
    cin>>t;
    nt=t;
    while(t--)
   {

    int vis[10]={0};
    int n=0;
    cin>>n;
    int an=n;
    if(n==0)
    {
        cout<<"Case #"<<(nt-t)<<": INSOMNIA"<<endl;
        continue;
    }
    for(int i=1;;i++)
    {
    n=an*i;
    //cout<<"here n = "<<n<<endl;
    int no=n;
    while(no>0)
    {
        int k = no%10;
        no/=10;
        vis[k]=1;
    }

    int c=0;
    for(int j=0;j<10;j++)
    {
        if(vis[j]==0)
        {
            c=1;
            break;
        }
    }

    if(c==0)
    {
        cout<<"Case #"<<(nt-t)<<": "<<n<<endl;
        break;
    }

    else
    {
        c=0;
    }
    }
   }
    // << "Hello world!" << endl;
    return 0;
}
