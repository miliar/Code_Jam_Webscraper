#include <vector>
#include <algorithm>
#include<string>
#include <iostream>

using namespace std;

int main()
{
    int numCase;
    cin >> numCase;
    int i, j;
    long long  n;
    long long ans,sum;

    int arr[10];
    for (i = 0; i < numCase; i++)
    {   int count=10;
     sum=0;
        for(j=0;j<10;j++)
            arr[j]=0;
        ans=0;
        cin>>n;
        if(n==0)
            cout << "Case #" << (i+1) << ": INSOMNIA\n";
        else
        {
        long long int a=n;
        while(a>=1){
            j=a%10;
            if(arr[j]==0)
            {    arr[j]=1;count--;
            }
            a=a/10;
        }
        while(count>0){
            sum+=n;
            ans++;
            a=sum;
            while(a>=1){
                j=a%10;
                if(arr[j]==0)
                {    arr[j]=1;count--;
                }
                a=a/10;
            }

        }



        cout << "Case #" << (i+1) << ": " << sum << endl;
        }
    }
    return 0;
}
