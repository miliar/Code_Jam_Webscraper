#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
int test;
cin>>test;
int z = 0;
while(test--)
{
    int x,y,n;
    vector<double>a,b;
    x = 0;
    y = 0;
    cin>>n;
    double num;
    for(int i = 0;i < n;i++)
    {
        cin>>num;
		a.push_back(num);
    }
    for(int i = 0;i < n;i++)
    {
        cin>>num;
        b.push_back(num);
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    int k = 0;
     for(int i = 0;i < n;i++)
     {
        if(a[i] > b[k])
        {
            x++;
            k++;
  
        }
    }
    k = 0;
    for(int i = 0;i < n;i++)
    { 
        if(b[i] > a[k])
        {
            y++;
            k++;
        }
    }
    y = n - y;
    z++;
    cout<<"Case #"<<z<<": "<<x<<' '<<y<<endl;
}
//system("pause");
return 0;
}
