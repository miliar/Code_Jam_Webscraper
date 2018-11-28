#include <bits/stdc++.h>

using namespace std;


int main()
{
int t;
cin >> t;
int y=1;
while(t--)
{
int k,c,s;
cin >>k>>c>>s;
long long int p;
p=pow(k,c-1);




cout<<"Case #"<<y<<": ";
for(int i=0;i<k;i++)
{
cout << 1+i*p<<" ";
}

y++;
cout <<endl;
}
}
