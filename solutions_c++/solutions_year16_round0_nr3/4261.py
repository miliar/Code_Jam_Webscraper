#include<bits/stdc++.h>
#define ii long long int

using namespace std;

string inc2(string a)
{
    string ans;
    int ll=a.length();
    int curr=ll-1;
    int carry=2;
    while(curr>=0)
    {
        int xx=(a[curr]-'0')+carry;
        ans+=(xx%2)+'0';
        char a=((xx%2)+'0');
        //cout<<"xx:"<<xx<<endl;
        carry=xx/2;
        curr--;
    }
    if(carry)
    {
        ans+='1';
    }
    string temp;
    int l=ans.length();
    for(int i=l-1;i>=0;i--)
    {
        temp+=ans[i];
    }
    return temp;
}

ii pow(ii a,ii b)
{
    ii t=1;
    for(int i=0;i<b;i++)
    {
        t*=a;
    }
    return t;
}

ii str_to_int(string x)
{
    int l=x.length();
    ii t=0;
    ii k=0;
    for(int i=l-1;i>=0;i--)
    {
        t+=((x[i]-'0')*pow((ii)10,k));
        k++;
    }
    return t;
}

bool check_prime(ii x)
{
    ii sqn=(ii)sqrt(x);
    for(ii i=2;i<=sqn;i++)
    {
        if(x%i==0)
            return 0;
    }
    return 1;
}

bool check(ii x)
{
    //printf("\n");
    for(ii base=2;base<=10;base++)
    {
        ii t=0;
        ii temp=x;
        ii k=0;
        while(temp!=0)
        {
            t+=((temp%10)*pow(base,k++));
            temp/=10;
        }
        //cout<<t<<endl;
        if(check_prime(t))
            return 0;
    }
    return 1;
}

void print_div(ii x)
{
    for(ii base=2;base<=10;base++)
    {
        ii t=0;
        ii temp=x;
        ii k=0;
        while(temp!=0)
        {
            t+=((temp%10)*pow(base,k++));
            temp/=10;
        }
        //cout<<t<<endl;
        ii sqt=(ii)sqrt(t);
        for(ii i=2;i<=sqt;i++)
        {
            if(t%i==0)
            {
                cout<<" "<<i;
                break;
            }
        }
    }
}

int main()
{
    //freopen("c.txt","w",stdout);
    int cas=1;
    int test;
    scanf("%d",&test);
    while(test--)
    {
        int n,j;
        scanf("%d %d",&n,&j);
        string x;
        x+='1';
        for(int i=0;i<n-2;i++)
        {
            x+='0';
        }
        x+='1';
        int cnt=0;
        printf("Case #%d:\n",cas++);
        while(cnt<j)
        {
            ii xx=str_to_int(x);
            if(check(xx)==1)
            {
                cout<<xx;
                /// print divisors of a
                print_div(xx);
                printf("\n");
                cnt++;
            }
            x=inc2(x);
        }
    }
    return 0;
}
