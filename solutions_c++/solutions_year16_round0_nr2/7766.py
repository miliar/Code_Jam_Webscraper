#include <iostream>
#include <string>

using namespace std;

bool check(string str,int str_len)
{
    for(int i=0;i< str_len; i++)
    {
        if(str[i]=='-')
        {
            return false;
        }
    }
    return true;
}

string str_change(string str, int str_length)
{
    if(str[0]=='+')
    {
        for(int i=0; i<str_length; i++)
        {
            if(str[i]=='+')
            {
                str[i]='-';
            }
            else break;
        }        
    }
    else
    {
        for(int i=0; i<str_length; i++)
        {
            if(str[i]=='-')
            {
                str[i]='+';;
            }
            else break;
        }
    }
    return str;
}



int main()
{
    int no_of_case;
    cin >> no_of_case;
    for(int i=0; i<no_of_case; i++)
    {
        string str;
        cin >> str;
        int length;
        length= str.length();
        int count =0;
        while(!check(str,length))
        {
            str= str_change(str,length);          
            count++;
        }
        cout << "Case #" << i+1 << ":" << " " << count << '\n';
    }    
}
