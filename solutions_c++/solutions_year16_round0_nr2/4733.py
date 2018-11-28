#include <iostream>
#include<cstdio>
    using namespace std;

    int recurseCountFlips(string s,int l){
        int count=0;

        while(s[l]=='+')
        {
            l--;
        }
        if(l<0)
            return count;
        count++;
        while(s[l]=='-')
        {
            l--;
        }
        if(l<0)
            return count;
        count++;
        count += recurseCountFlips(s,l);
        return count;



    }

    int main()
    {
        int t;
        cin>>t;
        for(int k=1;k<=t;k++)
        {
            string s;
            int count=0;
            cin>>s;

            count=recurseCountFlips(s,s.length()-1);

            cout<<"Case #"<<k<<": "<<count<<endl;


        }

        return 0;
    }
