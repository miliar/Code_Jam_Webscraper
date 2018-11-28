#include<iostream>
#include<fstream>
using namespace std;
bool used[100000];

main()
{
    ifstream cin("A-large.in.txt");
    ofstream cout("input.txt");
    int64_t test,n=0,a=1e6+1;
    cin >> test;
    while(test--)
    {
        cin>>a;
        n++;
        int ok=0,result;
        int cnt=1;
        for(int i=0;i<=10;i++)
            used[i]=0;
        while(a*cnt<=1e17)
        {
            if(a*cnt==a and a*(cnt+1)==a)
            {
                ok=1;
                break;
            }
            int q=a*cnt;
            while(q)
            {
                used[q%10]=1;
                q/=10;
            }
            int ans=0;
            for(int i=0; i<=9; i++)
            {
                ans+=used[i];
            }
            if(ans==10)
            {
                result=a*cnt;
                break;
            }
            cnt++;
        }
        cout<<"Case #"<<n<<": ";
        if(ok) cout<<"INSOMNIA";
        else cout<<result;
        cout<<"\n";
    }

}
