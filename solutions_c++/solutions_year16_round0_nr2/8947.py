#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("outputb.txt","w",stdout);
    int t;
    cin>>t;
    for(int y = 1; y <= t; y++)
    {
        string str;
        string necres;
        cin>>str;
        int le = str.length();
        necres = "";
        necres.append(str.length(),'+');
        //cout<<necres<<endl;
        int count = 0;
        while(str != necres)
        {
            int till;
            for(till = str.length() - 1; str[till] == '+'; till--);
            for(int i = 0; i <= till; i++)
            {
                switch(str[i])
                {
                    case '+':
                    {
                        str[i] = '-';
                        break;
                    }
                    
                    case '-':
                    {
                        str[i] = '+';
                        break;
                    }
                }
            }
            count++;
        }
        cout<<"Case #"<<y<<": "<<count<<'\n';
    }
    
    return 0;
    
}
        
    
