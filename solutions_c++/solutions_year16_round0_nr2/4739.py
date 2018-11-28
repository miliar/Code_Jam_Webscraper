#include <iostream>
#include <fstream>
#include<string>
using namespace std;
int main()
{
    string line;
    fstream myfile("B-large.in", ios_base::in);
    ofstream out;
    out.open("out.txt");
    int i=0,t;
    string s;
    myfile>>t;
    while(i<t)
    {
        myfile>>s;
        int l=s.length(),pos=0,n=0;
        // cout<<endl<<endl<<i<<"  "<<s<<endl<<endl;

       // cout<<s<<endl;
        while(pos<l)
        {

            if(s[l-pos-1]!='+')
            {
                if(s[0]=='+')
                {
                    for(int j=0; j<s.length()&&s[j]=='+'; j++)
                    {
                        s[j]='-';
                    }
                    n++;
                  //  cout<<n<<"  "<<s<<endl;
                }
                /* else                    //to be deleted
                 {
                     int j,k;
                     for( j=0; j<s.length()&&s[j]=='-'; j++)
                     {
                     }
                     for(j=k; j<s.length()&&s[j]=='+'; j++)
                     {
                     }
                     if(k-j>=2)
                     {
                         n+=2;
                         for(j=k; j<s.length()&&s[j]=='+'; j++)
                         {
                             s[j]='-';
                         }
                     }
                 }*/
                for(int j=0; j<=(l-pos-1)/2; j++)        //swap and flip
                {
                    char c=s[j];
                    s[j]=s[l-pos-1-j];
                    s[l-pos-j-1]=c;
                    if(s[j]=='+')
                    {
                        s[j]='-';
                    }
                    else
                    {
                        s[j]='+';
                    }
                    if(j!=l-pos-j-1)
                    {
                        if(s[l-pos-j-1]=='+')
                        {
                            s[l-pos-j-1]='-';
                        }
                        else
                        {
                            s[l-pos-j-1]='+';
                        }
                    }

                }
                n++;
              //  cout<<n<<"  "<<s<<endl;
            }
            pos++;
        }
        //   cout<<endl<<"finally i have got in "<<n<<"     "<<s<<endl;
        out<<"case #"<<i+1<<": "<<n<<endl;
        i++;
    }
    return 0;
}
