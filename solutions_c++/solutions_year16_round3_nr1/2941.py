#include <iostream>
#include<utility>
#include<map>
#include <iostream>
#include <string>
#include <iostream>
#include<math.h>
#include <bits/stdc++.h>
#include <cstdlib>
#include <time.h>
#include<queue>
class node
{
public:
int a;
char c;
node(int x,char y)
{
a=x;
c=y;
}
node(){
}
bool operator< (const node& right) const { return a> right.a; }


};

using namespace std;

int main()
{
  //  cout << "Hello world!" << endl;
freopen("at2.in","r",stdin);
    freopen("output_as1","w",stdout);
    int t;
    cin>>t;
    int r=0;
    while(t--)
    {r++;
    int n,p=0;
    cin>>n;
    node *arr=new node[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i].a;
        p+=arr[i].a;
        arr[i].c=i+65;
    }

     sort(arr,arr+n);
     cout<<"Case #"<<r<<": ";
     while(p>0)
     {
     if(p-2-arr[1].a>=arr[1].a)
     {
        arr[0].a-=2;
        cout<<arr[0].c;
        cout<<arr[0].c<<" ";
        sort(arr,arr+n);
        p=p-2;

     }
     else if(arr[0].a==1 && arr[2].a==1)
     {
     cout<<arr[2].c<<" ";
     arr[2].a-=1;
     p=p-1;
     sort(arr,arr+n);
     }
     else
     {
     if(arr[1].a>0 && arr[0].a>0)
     {
     arr[0].a-=1;
     cout<<arr[0].c;
     arr[1].a-=1;
     cout<<arr[1].c<<" ";
     p=p-2;



     }else {
     if(arr[0].a>0)
     {arr[0].a-=1;
     cout<<arr[0].c<<" ";
     p=p-1;

     }
     if(arr[1].a>0)
     {arr[1].a-=1;
     cout<<arr[1].c<<" ";
     p=p-1;

     }

     sort(arr,arr+n);

     }
    }



     }

cout<<endl;

    }


    return 0;
}
