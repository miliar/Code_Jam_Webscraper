#include <iostream>
#include <sstream>
#include <string>

using namespace std;

//Case1: -X+ -> X'++  1 action
//Case2: +X- -> ++X    2 actions
//Case3: +X+ -> X'++   2 actions
//Case4: -X- -> X++    3 actions
bool ishappy(string pans)
{
    int len=pans.length();
    bool happy=true;
    for(int i=0; i<len; i++)
        if(pans[i]=='-')
            happy=false;
    return happy;
}
int main()
{

    string input;
    int T;
    getline(cin,input);
    istringstream iss(input);
   // iss(input);
    iss>>T;
    for(int i=0;i<T;i++)
    {
       getline(cin,input);
       int actions=0;
       int len=input.length();
       char first,last;
       int fi,li;
       string temp="";
       if(len==1)
       {
           if(!ishappy(input))
            actions++;
       }
       while(!ishappy(input) & len>1)
       {
            first=input[0]; last=input[len-1];
            fi=0; li=len-1;
            for(int j=1;j<len;j++)
              {
                  if(input[j]==first)
                    fi++;
                  else
                    break;
              }
              for(int j=len-2;j>=0;j--)
              {
                  if(input[j]==last)
                    li=j;
                  else
                    break;
              }
              int totalplus=len-li+fi+1;
              temp="";
              for(int k=0;k<totalplus;k++)
                  temp+="+";
                  if(fi>li & first=='-')
                    actions++;
             else if(first=='+' & last=='+')
              {
                    actions+=2;
                    for(int k=fi+1;k<li;k++)
                    {
                        if(input[k]=='+')
                            temp="-"+temp;
                        else
                            temp="+"+temp;
                    }

              }
              else if(first=='+' & last=='-')
              {
                    actions+=2;
                    for(int k=fi+1;k<li;k++)
                        temp=temp+input[k];
              }
              else if(first=='-' & last=='+')
              {
                    actions++;
                    for(int k=fi+1;k<li;k++)
                    {
                        if(input[k]=='+')
                            temp="-"+temp;
                        else
                            temp="+"+temp;
                    }
              }
              else // first== - & last == -
              {
                  string temparr="";
                    actions+=3;
                    for(int k=fi+1;k<li;k++)
                    {
                        temparr+=input[k];
                    }
                    temp=temparr+temp;
              }
              input=temp;
              //cout<<input<<endl;
       }
       cout<<"Case #"<<i+1<<": "<<actions<<endl;

    }
    return 0;
}
