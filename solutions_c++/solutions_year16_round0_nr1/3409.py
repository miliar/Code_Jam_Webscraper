#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,t1;
    cin>>t;
    for(t1=1;t1<=t;t1++)
    {
        long long int n,i,j,k;
        cin>>n;
        if(n==0)
        {     
            cout<<"Case #"<<t1<<": INSOMNIA\n";
            continue;
        }
        set<char> se;
		for(i=0;i<10;i++)
			se.insert('0'+i);
        stringstream ss;
        ss << n;
        string str = ss.str();
        for(i=0;i<str.size();i++)
        {
            se.erase(str[i]);   
        }
        j=2;
        while(1)
        {
            k=j*n;
            stringstream ss;
            ss << k;
            string str = ss.str();
            for(i=0;i<str.size();i++)
            {
                se.erase(str[i]); 
                if(se.empty())
                    break;
            }
            if(se.empty())
                break;
            j++;
        }
        cout<<"Case #"<<t1<<": "<<k<<"\n";
    }    
    return 0;
}
