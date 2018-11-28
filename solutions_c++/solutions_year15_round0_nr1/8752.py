#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    long long t,n,i,x,s[1001]={0},total=0,count=0,cases=0;
    string word;
    cin>>t;

    while(t--)
    {
        cases++;
        total = 0;
        count = 0;

        cin>>n;
        cin>>word;
        for(i=0;i<=n;i++)
        {
            x = word[i]-48;
            s[i]=x;
        }
        total += s[0];
        for(i=1;i<=n;i++)
        {
            if(i>total)
            {
                count += (i-total);
                total +=(i-total);
            }
            total += s[i];
        }
        cout<<"Case #"<<cases<<": "<<count<<endl;
    }
return 0;
}
