#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int count=1;
    while(t--)
    {
        cout<<"Case #"<<count<<": ";
        count++;
        int n;
        cin>>n;
        float a[n+10];
        float b[n+10];
        for(int i=0; i<n; i++)
        {
            cin>>a[i];
        }
        for(int i=0; i<n; i++)
        {
            cin>>b[i];
        }
        sort(a,a+n);
        sort(b,b+n);
        int mycount=0;
        //cout<<n<<endl;
        int myvar1=0;
        int myvar2=0;

        for(int i=0; i<n; i++)
        {
            if(b[myvar2]>a[myvar1])
            {
                mycount++;
                myvar1++;
                myvar2++;
            }
            else
            myvar2++;
            if(myvar2>=n)
            break;
        }
        int mycount1=0;
        int var1=0;
        int var2=0;
        for(int i=0; i<n; i++)
        {
            if(a[var1]>b[var2])
            {
                mycount1++;
                var1++;
                var2++;
            }
            else
            var1++;
            if(var1>=n)
            break;
        }

       mycount=n-mycount;
        cout<<mycount1<<" "<<mycount<<endl;
    }
    return 0;
}
