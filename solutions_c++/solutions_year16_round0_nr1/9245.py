#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    long long int n,i,j,T,res,output[101]={};
    cin>>T;
    for(i=0;i<T;i++)
    {
    cin>>n;
    vector<long long int> numbers;
    for(j=0;j<10;j++)
    numbers.push_back(j);
    for(j=1;j<2000;j++)
    {
    res=n*j;
    long long int temp=res;
    while(temp)
    {
    long long int digit=temp%10;
    temp/=10;
    vector<long long int>::iterator pos=find(numbers.begin(),numbers.end(),digit);
    if(pos!=numbers.end())
    numbers.erase(pos);
    }
    if(numbers.size()==0)
    {
    output[i]=res;
    break;
    }
    }
    }
    for(i=0;i<T;i++)
    if(output[i]!=0)
    cout<<"Case #"<<i+1<<":  "<<output[i]<<endl;
    else
    cout<<"Case #"<<i+1<<":  "<<"INSOMNIA"<<endl;
}
