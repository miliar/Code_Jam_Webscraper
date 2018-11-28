#include<iostream>
#include<vector>
#include<string>
#include<cstdio>

using namespace std;

main()
{
    freopen("input.txt","r",stdin);
    freopen("largeBout.txt","w",stdout);
    int T,len,cot,c=1;
    string s,y;
    cin>>T;

    while(c<=T) {
        cot=0;
        cin>>s;
        y=s;
        len=s.length();
        fill_n(y.begin(),y.length(),'+');
        while(s!=y) {
            while(s[len-1]=='+')
                len--;
            int a=len--;
            string k=s.substr(0,a);
            for(int i=0; i<a; i++) {
                if(k[i]=='+')
                    k[i]='-';
                else k[i]='+';
            }
            s.replace(0,a,k);
            cot++;
        }
        cout<<"Case #"<<c<<": "<<cot<<"\n";
        c++;
    }

}
