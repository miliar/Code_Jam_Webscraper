#include<bits/stdc++.h>
using namespace std;
int main()
{

    long long t,i,j=1,Smax;
    char temp;
    cin>>t;
    while(t--)
    {
        long long answer=0,*arr,total_standing=0;
        cin>>Smax;
        arr = new long long[Smax+1];
        for(int i=0;i<=Smax;i++)
        {
            cin>>temp;
            arr[i]=temp-'0';
        }
        total_standing=arr[0];
        for(int i=1;i<=Smax;i++)
        {
            if(i>total_standing && arr[i]!=0)
            {
                answer+=(i-total_standing);
                total_standing+=answer;
            }
            total_standing=arr[i]+total_standing;
        }
        cout<<"Case #"<<j++<<": "<<answer<<endl;
    }

    return 0;
}
