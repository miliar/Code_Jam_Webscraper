#include<iostream>
#include<cmath>
#include<iomanip>
#include<fstream>
#include<string>
using namespace std;

int toint(string s)
{
    int n=0;
    for (int i=0;i<s.size();i++)
       n = n*2+(s[i]-'0');
    return n;
}

int main()
{
    ifstream input("a.in");
    ofstream output("a.out");
    
    int T, N;
    string s1, s2, a[100],b[100];
    input>>T;
    for (int t=1;t<=T;t++)
    {
        output << "Case #" << t << ": ";
        input>>N;
        for (int i=0;i<N;i++)
            input>>a[i];
        
        int c=0,i,j;
        for (i=0;i<N;i++)
        {
            for (j=i+1;j<N;j++)
            {
                string spaces(100,' ');
                s1=" "+a[i]+" ",s2=" "+a[j]+" ";
                int k=1,l=1;
                for (;(k<s1.size()-1||l<s2.size()-1);)
                {
                    if (s1[k]==s2[l])
                       k++,l++;
                    else
                    {
                         if (s1[k]==s1[k-1])
                         {
                            s1=s1.substr(0,k)+s1.substr(k+1);
                            //k++;
                            c++;
                         } else
                         if (s2[l]==s2[l-1])
                         {
                            s2=s2.substr(0,l)+s2.substr(l+1);
                            //l++;
                            c++;
                         } else
                           break;
                    }     
                }
                if (k<s1.size()-1||l<s2.size()-1)
                   break;
                a[i]=s1;
                a[j]=s2;
            }
            if (j<N)
               break; 
        }
        if (i<N)
           output<<"Fegla Won"<<endl;
        else
            output<<c<<endl;
    }
    system("pause");
    return 0;
}
