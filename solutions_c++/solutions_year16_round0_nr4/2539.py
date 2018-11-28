#include <iostream>
using namespace std;
int main()
{
int T;
cin>>T;
int K[T], C[T], S[T];
for(int i = 0; i<T; i++)
{
cin>>K[i]>>C[i]>>S[i];
}
for(int i = 0; i<T; i++)
{
if(K[i]<=S[i])
{
cout<<"Case #"<<i+1<<": ";
for(int j =0; j<K[i];j++)
cout<<j+1<<" ";
cout<<endl;
}
else
cout<<"Case #"<<": IMPOSSIBLE"<<endl;
}
}
