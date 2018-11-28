#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;



int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++)
    {
        long long int n;
        cin>>n;
        int c=0;
        int arr[10][1];
        bool st=false;
        if(n>0){
        for(int i=0;i<10;i++)
        {
            arr[i][0]=0;
        }
        for(int i=1;;i++)
        {
            long long int sum=0;
            sum=i*n;
            stringstream ss;
            ss<<sum;
            string str=ss.str();
         //   cout<<str<<endl;
            for(int j=0;j<str.size();j++)
            {
                if(arr[str[j]-'0'][0]==0)
                {
                    arr[str[j]-'0'][0]=1;
                    c++;
                }
                if(c>9)
                {
                    n=sum;
                    st=true;
                    break;
                }

            }
            if(st)
                break;

        }
        cout<<"Case #"<<t<<": "<<n<<endl;
        }
        else
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
    return 0;
}
