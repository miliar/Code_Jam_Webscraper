#include <iostream>

using namespace std;

int main()
{
    int t,a_count=1;
    cin>>t;
    while(t--)
    {
        int max1,count1,frnd=0;
        cin>>max1;
        char arr[max1+1];
       // for(int i=0;i<max1+1;i++)
            cin>>arr;
        count1=arr[0]-'0';
        for(int i=1;i<max1+1;i++)
        {
            //cout<<"Count1 "<<count1<<endl;
            while(count1<i)
            {
                count1++;
                frnd++;
               // cout<<"count1 "<<count1<<"- frnd "<<frnd<<endl;
            }
            count1=count1+(arr[i]-'0');
        }
        cout<<"Case #"<<a_count<<": "<<frnd<<endl;
        a_count++;
    }
    return 0;
}
