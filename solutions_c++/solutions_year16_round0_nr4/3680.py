#include<iostream>
using namespace std;
void printCounting(int n)
{
    for(int i=1;i<=n;i++)
    cout<<i<<" ";
    
    cout<<endl;
}
int main()
{
    int t;
    cin>>t;
    int caseNo=1;
    while(t-->0)
    {
        int k,c,s;
        cin>>k>>c>>s;
        if(k==s)
        {
            cout<<"Case #"<<caseNo<<": ";
            printCounting(k); //Must be followed by an endl
        }    
        caseNo++;
    }
    return 0;
}
