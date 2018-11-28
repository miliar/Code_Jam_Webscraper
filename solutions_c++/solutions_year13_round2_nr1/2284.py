#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int fun(const vector<int>& arr, int a, int i, int n, int op)
{
    if(i >= n)
        return op;

    while((a > arr[i])&&(i<n))
    {
        a += arr[i];
        i++;
    }

    if(i >= n)
        return op;

    int op1 = fun(arr, (a+a-1), i, n, op+1);
    int op2 = fun(arr, a, i+1, n, op+1);

    if(op1<op2)
    {
        return (op1);
    }
    else
    {
        return (op2);
    }
}

int main()
{
    int t;
    cin>>t;

    for(int cas=1; cas<=t; cas++)
    {
        int a, n, temp;
        vector<int> arr;

        cin>>a>>n;

        int op = 0;

        for(int i=0; i<n; i++)
        {
            cin>>temp;
            arr.push_back(temp);
        }

        if(a == 1)
        {
            cout<<"Case #"<<cas<<": "<<n<<endl;
            continue;
        }

        sort(arr.begin(), arr.end());

        op = fun(arr, a, 0, n, 0);


        cout<<"Case #"<<cas<<": "<<op<<endl;
    }

    return 0;
}
