#include <iostream>
#include <math.h>
#include <stack>
#include <fstream>
using namespace std;
#include <string.h>
#include <vector>

#include <algorithm>

int flag;
string temp;
string leftt;
string swaap(string str)
{

    for(int i=0;i<str.length();i++)
    {
        if(str[i]=='+'){str[i]='-';}
        else{str[i]='+';}
    }
    reverse(str.begin(),str.end());

    return str;
}
int count(string str, int &ans)
{
    int l=str.length();
    if(l==1)
    {
        if(str[0]=='+')
        {
                //cout<<"1 "<<ans<<endl;
                return ans;
        }
        else
        {
                ans++;
                // cout<<"2 "<<ans<<endl;
                return ans;
        }
    }
    if(str[l-1]=='+')
    {
        str.erase(l-1,1);
        // cout<<"3 "<<ans<<endl;
        count(str,ans);
    }
    else
    {
        if(str[0]=='-')
        {
            str=swaap(str);
            ans++;
            //cout<<str<<endl;
            str.erase(l-1,1);
           // cout<<"4 "<<ans<<endl;
            //xcout<<str;
            count(str,ans);
        }
        else
        {
           ans++;
           for(int k=str.length()-1;k>=0;k--)
           {
               if(str[k]=='+'){flag=k;break;}
           }
           temp=str.substr(0,flag+1);
           leftt=str.substr(flag+1,str.length()-flag-1);
           temp=swaap(temp);
           str=temp+leftt;
           str=swaap(str);
           ans++;
           str.erase(l-1,1);
          // cout<<"5 "<<ans<<endl;
           count(str,ans);
        }
    }

}
int main()
{

    ifstream file("B-large.in");
    ofstream answ("final_output_large.out");
    string str;
    //cin>>str;

    //cout<<a;
    int t=0;
    while(getline(file,str,'\n'))
    {
        t++;
        int a=0;
        count(str,a);
        answ<<"Case #"<<t<<": "<<a;
        if(t!=100){answ<<endl;}

    }


}
