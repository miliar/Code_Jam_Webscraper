#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    int* arr,extracount,ovatingcount;
    int iter=0;
    while(t--)
    {
        int s;
        string str;
        cin >> s >> str;
        arr = new int[s+1];
        for(int i=0;i<s+1;i++)
        {
            arr[i]=str[i]-'0';
        }
        extracount = 0;
        ovatingcount = 0;
        for(int i=0;i<s+1;i++)
        {
            if(i<=ovatingcount and arr[i]!=0)
                ovatingcount+=arr[i];
            if(i>ovatingcount and arr[i]!=0)
            {
                extracount+=(i-ovatingcount);
                ovatingcount = i+arr[i];
            }
        }
        cout <<"Case #"<<iter+1<<": "<< extracount << endl;
        iter++;
        delete arr;
    }
}