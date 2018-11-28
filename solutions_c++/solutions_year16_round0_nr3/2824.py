#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

std::vector<int> v,v1;
int a[100000]={0};

// void seive()
// {
//     int i,j;
//     a[0]=a[1]=1;
//     for(i=2;i<sqrt(100000);i++)
//     {
//         if(a[i]==0)
//         {
//             for(j=1;j*i<100000;j++)
//                 a[i*j]=1;
//             v.push_back(i);
//         }
//     }
// }

bool is_prime (long long int num)
{
    if (num <=1)
        return false;
    else if (num == 2)         
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        long long int upperLimit = static_cast<long long int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

long long int x_to_dec(int x,string str)
{
    int len=str.length(),i;
    long long int ans=0;

    for(i=0;i<len;i++)
    {
        if(str[len-1-i]=='1')
        ans+=pow(x,i);
    }

    return ans;
}

long long int find_first_factor(long long int num)
{
    int i=3;
    if(num%2==0)
        return 2;
    while(1)
    {
        if(num%i==0)
            return i;
        i+=2;
    }
}

string dec_to_bin(int num)
{
    string str;

    while(num)
    {
        if(num%2==0)
            str+='0';
        else
            str+='1';
        num/=2;
    }

    reverse(str.begin(),str.end());
    return str;
}

int main() {
    long long int t,i,n,j,num,k,num2,pf,count,cno=1;
    string str;
   // cout<<x_to_dec(2,"1001")<<endl;
    cin>>t;
    while(t--)
    {
        k=0;
        cin>>n >>j;
        num = pow(2,n-1)+1;
        num2=num;
        count=1;
        while(k<j)
        {
            str=dec_to_bin(num2);
            //cout<<"\n"<<k<<" "<<str<<endl;
            // str="100111"
            for(i=2;i<=10;i++)
            {
                num2=x_to_dec(i,str);
                //cout<<num2<<" ";
                if(is_prime(num2))
                    break;
            }
            //cout<<"<-i->"<<i<<endl;
            if(i>10)
            {
                k++;
              //  cout<<num+(count-1)*2<<" ";
                v1.push_back(num+(count-1)*2);
            }

            num2=num+(count++)*2;
        }

        //cout<<"vsize"<<v1.size()<<endl;
        cout<<"Case #"<<cno++<<":\n";
        for(i=0;i<v1.size();i++)
        {
            
            num2=v1[i];
            str=dec_to_bin(num2);
            cout<<str<<" ";

            for(k=2;k<=10;k++)
            {
                num2=x_to_dec(k,str);
                pf=find_first_factor(num2);
                cout<<pf<<" ";
            }

            cout<<endl;

        }


    }
    return 0;
}
