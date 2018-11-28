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
char p[1001];

char s[1001];

cin >> s;
p[0]=s[0];
int i=1;
while(s[i]!='\0')
{
if(s[i]>=p[0])
{
for(int j=i;j>=1;j--)
{
    p[j]=p[j-1];
}

 p[0]=s[i];

}
else
{
    p[i]=s[i];
}

i++;
}

cout <<"Case #"<<w<<": ";
for(int j=0;j<i;j++)
{
   cout << p[j];
}
cout <<endl;
w++;
}

}

