
#include <iostream>

using namespace std;


int main()
{
    int n,count;
    bool now;
    char curr;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        count=0;
        cin>>curr;
        if(curr=='-')
        {
            count++;
            now=false;
        }
        else
            now = true;
        while((curr=cin.get())!='\n')
        {
        if(curr=='-')
        {
            if(now==true)
            {
                count+=2;
                now=false;
            }
        }
        else{
            now=true;
        }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    
    return 0;
}