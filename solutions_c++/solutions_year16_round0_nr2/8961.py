#include <iostream>
#include<string>
using namespace std;

int main() {
    int T,j=1,i=0,k,count;
    char ch,ch2;
    string str;
    cin>>T;
    while(j<=T)
    {
        count=0;
        str.clear();
        cin>>str;
        while(1)
        {
            i=0;
            for(k=0;k<str.size();++k)
            {
                if(str[k]=='-')
                break;
            }
            if(k==str.size())
            {
                cout<<"Case #"<<j<<": "<<count<<"\n";
                break;
            }
            ch=str[0];
            if(ch=='+')
            ch2='-';
            else
            ch2='+';
            while((str[i]!=ch2)&&(i!=str.size()))
            {
                if(str[i]=='-')
                str[i]='+';
                else
                str[i]='-';
                i++;
            }
            count++;
        }
      j++;  
    }
	return 0;
}