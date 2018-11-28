#include<iostream>
#include<vector>
#include<cstring>
#include<string>
#include<fstream>
using namespace std;

int conscutiveChar (string str,int n,int start)
{
    //cout<<str<<endl;
int l ,k=0,count=0,flag;
//char dup[101];
l = str.length();
if(l<n) return 0;
 for(int i=start;i<=l-n;i++)
 {flag=1;
 for(int j=i;j<i+n;j++){
      if(str[j]=='a'|| str[j]=='e' || str[j] == 'i' || str[j] == 'o' || str[j] == 'u')
      {
       flag=0;
       break;
      }
   }
    if(flag==1)
    return 1;
 }
 return 0;
}

int main()
{
 ifstream cin("A-small-attempt0.in");
 ofstream cout("A-small-attempt0.out");
 int t,n,k=0,count;
 string string,str;
 cin>>t;
 while(t--)
 {
     count=0;
    cout<<"Case #"<<++k<<": ";
    cin>>string;
    cin>>n;
   /* for(int i=0;i<=strlen(string)-n;i++)
    {
        int val =conscutiveChar(string,n,i);
        if(val)
        {
        count++;
        }
    }
    cout<<count<<endl;
    for(int i=strlen(string)-2;i>=n-1;i--)
    {
        int val =conscutiveBack(string,n,i);
        if(val)
        {
        count++;
        }
    }
    cout<<count<<endl;
    */
    int l = string.length();
    //cout<<l<<string;
    for(int i=l;i>=n;i--)
    {
        for(int j=0;j<=l-i;j++)
        {
            str = string.substr(j,i);
           // cout<<str<<endl;
            int val =conscutiveChar(str,n,0);
        if(val)
        {
        count++;
        }
        }
    }
    cout<<count<<endl;
 }

}
