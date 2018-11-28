#include <iostream>
#include <string.h>
#include <cstring>

using namespace std;

string flip(string str,int i,int k)
{
    for(int p=i,y=k;y>=p;p++,y--)
    {
        if(p!=y)
        {
            if(str[p]=='+')
                str[p]='-';
            else
                str[p]='+';
        }
         if(str[y]=='+')
                str[y]='-';
            else
                str[y]='+';
        swap(str[p],str[y]);
    }
    return str;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.in","w",stdout);
    long int t;
    cin>>t;
    long long int cases = t;
    while(t--)
    {
        string str;
        cin>>str;
        int sr=str.size()-1;
        int counter=0;
        while(sr>=0)
        {
         //   cout<<"text";
            int k=sr;
            while(str[k]=='+')
            {
                k--;
            }
            sr=k;
            if(sr>=0){
            int i=0;
            while(str[i]=='+'){
                i++;
            }
            if(i){
            str=flip(str,0,i-1);
            counter++;
            }
            str=flip(str,0,sr);
            counter++;
        }
    }
    cout<<"Case #"<<cases-t<<": ";
    cout<<counter<<endl;
}
return 0;
}
