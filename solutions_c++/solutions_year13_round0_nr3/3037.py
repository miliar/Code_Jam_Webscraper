#include<iostream>
#include<cmath>
using namespace std;
bool palin(int c);
int main()
{
    int test,i,j,a,b,c,counter=0,ct=0;
    float k;
    cin>>test;
    while(test--)
    {
        cin>>a>>b;
        k=1;
        while(k*k<a)
            k++;
        counter=0;
        c=k;
        while(c*c<=b)
        {
            if(palin(c) && palin(c*c))
            {
                counter++;
            }
            c++;
        }
        ct++;
    cout<<"Case #"<<ct<<": "<<counter<<"\n";
    }

}
bool palin(int c)
{
    int i,j,k;
    int arr[100];
    i=0;
    while(c>0)
    {
        arr[i]=c%10;
        c/=10;
        i++;
    }
    for(j=0,k=i-1;j<k;j++,k--)
    {
        if(arr[j]!=arr[k])
        {
            return false;
        }
    }
    return true;
}










