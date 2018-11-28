#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream input("A-large.in");
    ofstream output("output_file.in");
    long long int t,n,count,m;
    string s;

    input >> t;
    for(long long int k=1;k<=t;k++)
    {
        bool a[10]={false};
        count=0;
        input >> n;
        int i=1;
        if(n==0){output << "Case #"<< k <<": INSOMNIA" << "\n";}
        else
        {
        while(count<10)
        {
            m=i*n;
            stringstream ss;
            ss << m;
            ss >> s;
            for(long long int j=0;j<s.length();j++)
            {
                if(a[s[j]-48]==false)
                {
                    count++;a[s[j]-48]=true;
                }
            }
            i++;
        }
        output << "Case #"<< k << ": " << m << "\n";
        }
    }
}
