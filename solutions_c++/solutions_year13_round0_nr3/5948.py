#include <iostream>
#include <cstdio>

using namespace std;

int root(int num)
{
    for(int i=1;i<=num/2;i++)
    {
        if(i*i==num)
        {
            return i;
        }
    }
    return 0;
}

bool check(int num)
{
    int r, mat2[100], mat1[100], b=0, s=0;
    r=root(num);
    if(num==1)
    {
        return true;
    }
    if(r==0)
    {
        return false;
    }
    else
    {
        while(r>0)
        {
            mat1[b]=r%10;
            r=r/10;
            b++;
        }
        while(num>0)
        {
            mat2[s]=num%10;
            num=num/10;
            s++;
        }
        int c=b-1;
        for(int i=0;i<b;i++)
        {
            if(mat1[i]!=mat1[c])
            {
                return false;
            }
            c--;
        }
        c=s-1;
        for(int i=0;i<s;i++)
        {
            if(mat2[i]!=mat2[c])
            {
                return false;
            }
            c--;
        }
    }
    return true;
}

int main()
{
    freopen("palindrom.in", "r", stdin);
    freopen("palindrom.out", "w", stdout);
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int a,b, rez=0;
        cin>>a>>b;
        for(int j=a;j<=b;j++)
        {
            if(check(j)==true)
            {
                rez++;
            }
        }
        cout<<"Case #"<<i+1<<": "<<rez<<endl;
    }

    return 0;
}
