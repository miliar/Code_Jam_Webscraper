
#include <iostream>
using namespace std;

int main()
{
    long long int n,k,p,r,l,len;


    cin>>n;


    for(long long int i=0;i<n;i++)
    {
        string s1;

        cin>>s1;
        //cout<<s1<<" "<<s2<<" ";
        long long int count=0;
        for(long long int j=s1.size()-1;j>=0;j--)
        {

           // cout<<s1[j]<<" ";
            if(s1[j]=='-')
            {
                count++;
               for(long long int k=j;k>=0;k--){
                   if(s1[k]=='+')
                   s1[k]='-';
                   else
                   s1[k]='+' ;

            }


        }


           // cout<<s1<<" ";

        }
        //cout<<s1<<" ";
     cout<<"Case #"<<i+1<<": "<<count<<"\n";

    }

return 0;
}
