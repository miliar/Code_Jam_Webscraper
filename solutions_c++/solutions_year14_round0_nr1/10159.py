#include <iostream>
#include <vector>
using namespace std;

int main()
{
int t(0);
cin >> t;
int n(0),a(0);
vector<int> tab;

for(int i(1);i<=t;i++)
{
tab.clear();
cin >> n;
n--;
for(int j(0);j<16;j++)
{
cin >> a;
if(j>=n*4 && j<((n+1)*4))
tab.push_back(a);
}
int nb(0);
cin >> n;
n--;
int c(-1);
for(int j(0);j<16;j++)
{
cin >> a;
if(j>=n*4 && j<((n+1)*4))
{
for(int k(0);k<4;k++)
{
if(tab[k]==a)
{
nb++;
c=a;

}
}
}
}

if(nb==1)
{
cout << "Case #" << i <<": " << c << endl;
}
else if(nb>1)
{
cout << "Case #" << i <<": Bad magician!" << endl;
}
else
{
cout << "Case #" << i <<": Volunteer cheated!" << endl;
}
tab.clear();
}

return 0;
}
