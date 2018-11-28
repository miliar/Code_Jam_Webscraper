#include<iostream>
using namespace std;
int countOf0(int a[])
{
    int c=0;
    for(int i=0;i<10;i++)
    if(a[i]==0)
    c++;
    
    return c;
}
int main()
{
    int t;
    cin>>t;
    int caseNo=1;
    while(t-->0)
    {
        int n;
        cin>>n;
        
        if(n==0)
        {
            cout<<"Case #"<<caseNo<<": INSOMNIA"<<endl;
            caseNo++;
            continue;
        }
        
        long long int c = 1;
        int flag[10];
        for(int i=0;i<10;i++)
        flag[i]=0;
        
        long long int x;
        
        while(countOf0(flag)>0)
        {
            x=n*c;
            while(x>0)
            {
                flag[x%10]=1;
                x=x/10;
            }
            c++;
        }
        
        cout<<"Case #"<<caseNo<<": "<<(c-1)*n<<endl;
        caseNo++;
    }
    return 0;
}
