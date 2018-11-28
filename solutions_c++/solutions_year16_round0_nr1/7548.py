#include <bits/stdc++.h>
using namespace std;

long long int t;
vector <int >a;
int n1[10];
long long int cnt=1;
long long int n;

int main()
{
 
    cin>>t;
    while(t--)
    {
        cin>>n;
        long long int i=1;
        memset(n1,0,sizeof(n1));
        
        if(n==0)
        {
            cout<<"Case #"<<(cnt++)<<": "<<"INSOMNIA"<<endl;
        }
        
        else
        {
            long long int x;   
            
            while(1)
            {
              long long int temp;
              long long int temp2;
              if((int)a.size()==10)
                break;
            
                else
                {
                    temp=n*(i++);
                    //cout<<temp;
                    x=temp;
                        while(temp!=0) 
                        {
                            temp2=temp%10;
                            temp=temp/10;
                            if(n1[temp2]!=1)
                            {
                             n1[temp2]=1;
                             a.push_back(temp2);
                            }
                        }
                    
                }
            }
            cout<<"Case #"<<(cnt++)<<": "<<x<<endl;
            a.clear();
        }
        
    }
    return 0;
}
