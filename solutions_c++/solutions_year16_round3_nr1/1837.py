#include<bits/stdc++.h>
using namespace std;

int main()
{


int k=0;
    int t;
    cin>>t;
    priority_queue<pair<int,char> > p;
    while(t--)
    {
        k++;
        int n;
        cin>>n;
        int numb;
        for(int i=0;i<n;i++)
        {
            cin>>numb;
            p.push(make_pair(numb,(char)(65+i)));
        }
        cout<<"Case #"<<k<<": ";
        int l=0;
while(!p.empty())
{

    int n1=0;
    int n2=0;

    char c1,c2;
    n1=(p.top()).first;
 c1=(p.top()).second;
   p.pop();
   if(!p.empty())
   {


    n2=(p.top()).first;
  c2=(p.top()).second;
   p.pop();
   }
  // cout<<"hello1 :"<<n1<<" "<<c1<<endl;
   //cout<<"hello2 :"<<n2<<" "<<c2<<endl;
   if(n1==n2)
   {
       if(n1==1 && n2==1 && p.size()==1)
       {
           cout<<c1<<" "<<c2<<(p.top()).second<<" ";
           p.pop();
           break;
       }
       n1--;
       n2--;
       cout<<c1<<c2<<" ";
   }
   else if(n1>1)
   {
       n1-=2;
       cout<<c1<<c1<<" ";
   }
   else
   {


    n1--;
   cout<<c1<<" ";

   }
   if(n1!=0)
    p.push(make_pair(n1,c1));
    if(n2!=0)
        p.push(make_pair(n2,c2));
}
cout<<endl;
    }
}
