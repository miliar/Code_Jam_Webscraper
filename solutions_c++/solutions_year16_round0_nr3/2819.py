#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;

long long int arr[50];

LL toBinary(LL n)
{
    LL r = 0,i=0,j;
    while(n)
    {
        //cout<<111;
        arr[i++] = n%2;
        n/=2;
    }
    LL sum = 0;
    for(j=i-1;j>=0;j--)
    {
        sum = (sum*10) + arr[j];
    }

    return sum;
}
LL arr2[50];
LL base(LL n,LL base)
{
	LL sum=0,i=0;
    while(n!=0)
    {
    	sum+=(n%10)*ceil(pow(base,i++));
    	n/=10;
	}
	return sum;
}

int isprime(LL n)
{
    LL s = sqrt(n),i;
    for(i=2;i<=s;i++)
    {
        if(n%i ==0 )
            break;
    }
    return i>s;
}
LL divisor(LL n)
{
    for(LL i=2;i<n ; i++)
    {
        if(n%i==0)
            return i;
    }
}
int main()
{
    LL i,t,o,j;
    ofstream myfile;
    myfile.open ("2.txt");
    cin>>t;

    LL arr3[20];
    LL n = 32769,u;
    LL cnt=0;
    myfile<<"Case #1: "<<"\n";
    while(t--)
    {
        cin>>o>>j;
        for(u=n; ;u+=2)
        {
            LL k=0;
            LL flg=0;
            LL number = toBinary(u);
            for(i=2;i<=10;i++)
            {
                if(!isprime(base(number,i)))
                    arr3[k++] = base(number,i);
                else
                {
                    flg=1;
                    break;
                }
            }
            if(flg==0)
            {
               cnt++;
               myfile<<number<<" ";
               for(i=0;i<9;i++)
               {
                   myfile<<divisor(arr3[i])<<" ";
               }
                myfile<<"\n";
            }
            if(cnt==j)
                break;
        }
    }
    return 0;
}

