#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b) {
  if (b == 0) return a;
  return gcd(b, a%b);
}
long long int lcm(int a[], int n) {
  long long int res = 1;
  for (int i = 0; i < n; i++) {
    res = res*a[i]/gcd(res, a[i]);
  }
  return res;
}



int main()
{
int t, w;
cin >>t;
w=1;
while(t--)
{
int a[2501];
for(int i=0;i<2501;i++)
{
    a[i]=0;

}
int n;
cin >>n;
int uu=2*n*n-n;
int b[uu];
for(int i=0;i<uu;i++)
{
    cin >> b[i];
    a[b[i]]++;
}
cout <<"Case #"<<w<<": ";
for(int i=0;i<2501;i++)
{
if(a[i]%2==1)
{
cout <<i <<" ";
}

}





cout <<endl;
w++;
}

}

