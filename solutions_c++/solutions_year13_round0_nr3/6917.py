#include<iostream>
#include<cstdio>

using namespace std;

int isPal(long long n)
{
    int arr[20];
    int i = 0, val, k;
    for(i=0; n!=0;i++)
    {
        val = n%10;
        n = n/10;
        arr[i]=val;
    }
    i--;
    k=i;
    for(int j=0; j<=k/2; j++,i--)
    {
        if(arr[j] != arr[i])
        return 0;
    }

    return 1;
}

int main()
{
    freopen("D:\\input.in","r",stdin);
    freopen("D:\\output.in","w",stdout);

    long long i;
    int X[50],cnt=0;
    for(i=1; i<=10000000; i++)
    {
        if(isPal(i)){
            if(isPal(i*i)){
                X[cnt++] = i*i;
            }
        }
    }

    int T,A,B,res,j,k;
    cin >> T;

    for(j=1; j<=T; j++)
    {
        cin >> A >> B;
        res = 0;
        for(k=0; k<cnt; k++)
        {
            if(A<=X[k] && X[k]<=B)
            res++;
        }
        cout << "Case #" << j << ": " << res << endl;
    }

    return 0;
}
