#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int n,m;
    int cnt=0;
    int sum=0;
    string name;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>m;
        cin>>name;
        for(int i=0;i<m+1;i++)
        {
            if(name[i]-48==0) continue;
            if(i<=cnt) cnt+=name[i]-48;
                else { sum+=i-cnt; cnt+=sum+name[i]-48; }
        }
        cout<<"Case #"<<i+1<<": "<<sum<<endl;
        sum=0;
        cnt=0;
    }
    return 0;
}
