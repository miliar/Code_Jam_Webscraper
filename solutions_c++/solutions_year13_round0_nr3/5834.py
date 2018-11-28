#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
int size=1;
int num[101]={0};
long long A,B,MAX=1000;
bool isPalindrome(long long n)
{
    int n2=n,n3=0;
    while(n2)
    {
        n3=n3*10+n2%10;
        n2/=10;
    }
    return(n3==n);
}
void nextP(int pos)
{
    if((size%2==0 && pos >= size/2) || (size%2==1 && pos>size/2))
        return;
    num[pos]++;
    if(size!=1)
        num[size-pos-1]++;
    if(num[pos]<10)
        return;
    if(size%2==1 && pos==size/2)
    {
        size++;
        for(int i=0;i<size;i++)
        {
            num[i]=0;
        }
        num[0]=1;
        num[size-1]=1;
        return;
    }
    if(size%2==0 && pos==size/2-1)
    {
        size++;
        for(int i=0;i<size;i++)
        {
            num[i]=0;
        }
        num[0]=1;
        num[size-1]=1;
        return;
    }
    if(pos==0)
    {
        num[pos]=1;
        num[size-pos-1]=1;
    }
    else
    {
        num[pos]=0;
        num[size-pos-1]=0;
    }
    nextP(pos+1);
}
void print()
{
    for(int i=0;i<size;i++)
        cout << num[i];
    cout << endl;
}
void reset()
{
    for(int i=0;i<101;i++)
        num[i]=0;
    num[0]=1;
    size=1;
}
long long get()
{
    long long r=0;
    for(int i=0;i<size;i++)
        r=r*10+num[i];
    return r;
}

long long R()
{
    long long count=0;
    reset();
    long long n,n2;
    while(true){
        n=get();
        n2=n*n;
        nextP(0);
        if(n2>MAX)
            break;
        if(n2<=B && n2 >=A)
        {
            if(isPalindrome(n2))
            {
                count++;
            }
        }
    }
    return count;
}
long long R2()
{
    long long n,count=0;
    for(int i=A;i<=B;i++)
    {
        if(isPalindrome(i))
        {
            n=sqrt(i);
            if(n*n==i && isPalindrome(n))
                count++;
        }
    }
    return count;
}
long long R3()
{
    int y[]={1,4,9,121,484},count=0;
    for(int i=0;i<5;i++)
    {
        if(A<=y[i] && y[i]<=B)
        {
            count++;
        }
    }
    return count;
}
int main()
{
    //freopen("C-small-attempt1.in","r",stdin);
    freopen("i.in","r",stdin);
    freopen("o.txt","w",stdout);
    int T;
    cin >> T;
    int x=0;
    for(int test=1;test<=T;test++)
    {
        cin >> A >> B;
        cout << "Case #" << test << ": " << R() << endl;
    }
    return 0;
}
