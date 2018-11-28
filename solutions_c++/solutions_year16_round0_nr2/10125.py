#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int res, i=0,count = 0;
        char  ch;
        string str;
        cin>>str;
        ch=str[0];
        char top = ch;
        for(i=1;i<10 && str[i]!='\0'; i++)
        {
            if(ch!=str[i]){
                count+=1;
            }
            ch=str[i];
        }
        char bottom=ch;
        if(i==1)
        {
            if(top=='-')
                res=1;
            else
                res=0;
        }
 
        if((top=='+')&&(bottom=='-'))
            res = count + 1;
        if((top=='-')&&(bottom=='-'))
            res = count + 1;
        if((top=='+')&&(bottom=='+'))
            res = count;
        if((top=='-')&&(bottom=='+'))
            res = count;
        cout<<"Case #"<<k<<": "<< res<<endl;
    }
	return 0;
}
