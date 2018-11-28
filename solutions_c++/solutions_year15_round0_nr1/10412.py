#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int shy[1001];
void convert(string str)
{
    int size=str.size();
    for(int i=0;i<size;i++)
    {
        shy[i]=str[i]-'0';
    }
}
int solve(int n)
{
    int count=0,ans=0;
    for(int i=0;i<=n;i++)
    {
        if(count>n)
        {
            break;
        }
        if(count<i&&shy[i]>0)
        {
            cout<<i<<" "<<count<<endl;
            ans+=i-count;
            count=i;
        }
        count+=shy[i];
    }
    return ans;
}
int main()
{
    ifstream read("abc.txt");
    ofstream write("ans");
    int T,Smax;
    string str;
    read>>T;
    for(int i=0;i<T;i++)
    {
        read>>Smax;
        read>>str;
        convert(str);
        write<<"Case #"<<i+1<<": "<<solve(Smax)<<endl;
    }  
    return 0;
}
