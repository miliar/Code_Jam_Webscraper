# include<iostream>
using namespace std;
long long int ways(string s)
{
    int len =  s.length();;
    long long int c = 0;
    int i;
    int p;
    int c_l=0;
    int c_r=0;
    while(true)
    {
        p=0;
       // len = s.length();

        for(i=len-1;i>=0;i--)
        {
            if(s.at(i)=='-')
                break;
            len--;
        }
        if(len==0)
            return c;
        //cout << "len : " << len << endl;
        string temp="";
        if(s.at(0)=='+')
        {
            p=0;
            for(i=1;i<len;i++)
                if(s.at(i)=='-')
                    break;
            p = i;
            for(i=1;i<=p;i++)
                temp = temp+"-";
            temp = temp + s.substr(p,len-p);
            s=temp;
            c++;
        }
        else if(s.at(0)=='-')
        {
            temp = "";
            for(i=1;i<len;i++)
                if(s.at(i)=='+')
                    break;
            c_l = i;
            if(c_l==len)
                return (c+1) ;
            for(i=len-1;i>=0;i--)
                if(s.at(i)=='+')
                    break;
            c_r = len-1-i;
            if(c_l>c_r)
            {
                for(i=len-1;i>=0;i--)
                {
                    if(s.at(i)=='-')
                        temp = temp + '+';
                    else
                        temp = temp + '-';
                }
            }
            else
            {
                for(i=0;i<len;i++)
                {
                    if(s.at(i)=='+')
                        break;
                    temp = temp +  '+';
                }
                temp = temp + s.substr(i,len-i);
            }
            s=temp;
            c++;
        }
        //cout << s << endl;
    }
    return c;
}
int main()
{
    int test,temp;
    cin >> test;
    temp=test;
    string s;
    long long int count;
    while(test>0)
    {
        cin >> s;
        count = ways(s);
        cout << "Case #" << (temp-test+1) << ": " << count << endl;
        test--;
    }
}
