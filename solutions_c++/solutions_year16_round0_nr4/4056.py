#include <iostream>
int main()
{
int t;
std::cin>>t;
int k[t], c[t], s[t];
for(int i = 0; i<t; i++)
{
std::cin>>k[i]>>c[i]>>s[i];
}
for(int i = 0; i<t; i++)
{
if(k[i]<=s[i])
{
std::cout<<"Case #"<<i+1<<": ";
for(int j =0; j<k[i];j++)
std::cout<<j+1<<" ";
std::cout<<std::endl;
}
else
std::cout<<"Case #"<<": IMPOSSIBLE"<<std::endl;
}
}
